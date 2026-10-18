"""Deterministic daily merchant/lender/guarantee model; Python standard library.

Decimal precision is retained throughout; CSV rounding is presentation only.
A cycle starts on day d, sales on d+1, and original payment is due at d+tenor.
Guarantee allocation order is default day, merchant id, cycle (explicit tie rule).
"""
from copy import deepcopy
from decimal import Decimal, getcontext

getcontext().prec = 40
D = Decimal
Z = D(0)
TOL = D('0.00000001')


def dec(x):
    return D(str(x))


def m(p, key):
    return dec(p[key])


def validate(p):
    if p['runoff_days'] <= p['operating_days']:
        raise ValueError('runoff must follow operating period')
    for k in ['opening_cash','minimum_operating_cash','daily_operating_need','daily_household_need',
              'initial_limit','minimum_limit','maximum_limit','fee_rate_per_cycle','annual_funding_rate',
              'guarantee_annual_fee','guarantee_eligible_origination_budget','guarantee_first_layer_width',
              'guarantee_first_layer_cap','guarantee_second_layer_width','guarantee_second_layer_cap']:
        if m(p,k) < 0:
            raise ValueError(k + ' must be non-negative')
    for k in ['normal_sell_through','inventory_salvage_fraction_of_cost']:
        if not Z <= m(p,k) <= 1:
            raise ValueError(k + ' must be in [0,1]')
    if not m(p,'minimum_limit') <= m(p,'initial_limit') <= m(p,'maximum_limit'):
        raise ValueError('limit bounds are inconsistent')
    if p['guarantee_capacity_reinstatement']:
        raise ValueError('this teaching contract elects no capacity reinstatement')
    for k in ['first','second']:
        if not Z < m(p,'guarantee_'+k+'_layer_width') or m(p,'guarantee_'+k+'_layer_cap') > m(p,'guarantee_'+k+'_layer_width'):
            raise ValueError('guarantee layers must have positive widths and caps <= width')
    if len({x['id'] for x in p['merchants']}) != len(p['merchants']):
        raise ValueError('merchant identifiers must be unique')


def trading_terms(p, s, merchant, cycle):
    terms = dict(markup=m(p,'normal_markup_on_cost'), sales_days=p['normal_sales_days'],
                 lag=p['normal_settlement_lag'], sell_through=m(p,'normal_sell_through'), affected=False)
    if cycle < s['shock_start_cycle'] or s['mode'] == 'none':
        return terms
    if s['mode'] == 'severe':
        terms.update(markup=D('0.10'),sales_days=32,lag=6,sell_through=D('0.20'),affected=True)
    elif s['mode'] == 'margin':
        terms.update(markup=D('0.08'), sales_days=23, lag=3, affected=True)
        if merchant['segment'] == 'vulnerable':
            terms.update(sell_through=D('0.70'))
    elif merchant['segment'] == 'delayed':
        terms.update(sales_days=31, lag=5, affected=True)
    elif merchant['segment'] == 'vulnerable':
        terms.update(sales_days=32, lag=6, sell_through=D('0.42'), affected=True)
    if s['support'] and terms['affected']:
        terms.update(sales_days=24, lag=3, sell_through=D('0.92'), markup=D('0.25'))
    return terms


def repeat_limit(p, cash, previous):
    """Deterministic cash gate, based only on a settled previous cycle."""
    if previous is None:
        return m(p,'initial_limit'), 'initial approved teaching limit'
    if previous['default_day'] is not None or previous['settled_day'] is None:
        return Z, 'await settlement or default review'
    if cash < m(p,'minimum_operating_cash'):
        return Z, 'rebuild operating cash'
    proposed = previous['principal']
    if previous['settled_day'] <= previous['original_due_day'] and cash >= m(p,'minimum_operating_cash') + m(p,'increase_cash_buffer'):
        proposed = min(m(p,'maximum_limit'), proposed + m(p,'limit_increment'))
    # Last cycle's observed inventory conversion and cash timing inform the forecast.
    receipt_fraction = min(D(1), max(Z, dec(p['tenor_days']-previous['lag'])/previous['sales_days']))
    while proposed >= m(p,'minimum_limit'):
        expected_cash = cash + proposed * previous['sell_through'] * (1+previous['markup']) * receipt_fraction
        needs = dec(p['tenor_days'])*(m(p,'daily_operating_need')+m(p,'daily_household_need'))
        if expected_cash-needs-proposed*(1+m(p,'fee_rate_per_cycle')) >= m(p,'minimum_operating_cash'):
            return proposed, 'cash-gated repeat approval'
        proposed -= D(1000)
    return Z, 'forecast cash below required operating floor'


def merchant_run(p, s, merchant):
    cash=m(p,'opening_cash'); inventory=Z; receivables=Z; operating_arrears=Z
    active=None; loans=[]; rows=[]; receipts={}; sales={}; next_day=0; ever_default=False
    for day in range(p['runoff_days']+1):
        start_cash=cash; stock_received=sales_revenue=cogs=receipt=operating=household=shortfall=Z
        principal_paid=fee_paid=recovery=salvage=inventory_disposed=Z
        operating_accrual=household_gap=Z
        origination=fee_accrual=default_principal=unearned_fee_cancelled=Z
        support_cost=default_cost=recovery_cost=Z
        # Settled receipts precede discretionary repayment and repeat origination decisions.
        receipt=receipts.pop(day,Z); receivables-=receipt; cash+=receipt
        if day in sales:
            cogs,sales_revenue,sale_lag=sales.pop(day)
            inventory-=cogs; receivables+=sales_revenue
            settle=day+sale_lag
            if settle == day:
                receipt+=sales_revenue; receivables-=sales_revenue; cash+=sales_revenue
            else:
                receipts[settle]=receipts.get(settle,Z)+sales_revenue
        if 0 < day <= p['operating_days']:
            operating_accrual=m(p,'daily_operating_need');operating_arrears+=operating_accrual
            operating=min(cash,operating_arrears);cash-=operating;operating_arrears-=operating
            household=min(cash,m(p,'daily_household_need'));cash-=household
            household_gap=m(p,'daily_household_need')-household
            shortfall=max(Z,operating_accrual-operating)+household_gap
        if day > p['operating_days'] and operating_arrears>0:
            operating=min(cash,operating_arrears);cash-=operating;operating_arrears-=operating
        if active is not None:
            loan=active
            if day > loan['origin_day'] and loan['default_day'] is None and loan['fee_accrued'] < loan['contract_fee']:
                increment=min(loan['contract_fee']-loan['fee_accrued'],loan['contract_fee']/dec(p['tenor_days']))
                loan['fee_accrued']+=increment; fee_accrual=increment
            if day >= loan['due_day'] and loan['default_day'] is None:
                available=max(Z,cash-m(p,'minimum_operating_cash'))
                # Principal-first collection: elected product allocation convention.
                principal_paid=min(available,loan['principal_remaining']); available-=principal_paid
                fee_paid=min(available,loan['fee_remaining']); cash-=principal_paid+fee_paid
                loan['principal_remaining']-=principal_paid;loan['fee_remaining']-=fee_paid
                loan['principal_collected']+=principal_paid; loan['fees_collected']+=fee_paid
                if loan['principal_remaining']+loan['fee_remaining'] < TOL:
                    loan['principal_remaining']=loan['fee_remaining']=Z
                    loan['settled_day']=day
                    next_day=max(loan['origin_day']+p['scheduled_cycle_days'],day+p['repeat_cooldown_days'])
                    active=None
                elif day >= loan['due_day']+p['default_days_past_due']:
                    loan['default_day']=day; loan['written_off_principal']=loan['principal_remaining']
                    loan['default_fee_uncollected']=loan['fee_remaining']
                    default_principal=loan['written_off_principal'];ever_default=True
                    default_cost=m(p,'default_collection_cost')
                    loan['recovery_day']=day+p['recovery_days_after_default']
            if loan['default_day'] is not None and day == loan['recovery_day']:
                inventory_disposed=inventory
                salvage=inventory_disposed*m(p,'inventory_salvage_fraction_of_cost')
                inventory=Z;cash+=salvage
                arrears_payment=min(cash,operating_arrears);cash-=arrears_payment;operating_arrears-=arrears_payment;operating+=arrears_payment
                recovery=min(max(Z,cash-m(p,'minimum_operating_cash')),loan['principal_remaining'])
                cash-=recovery;loan['principal_remaining']-=recovery;loan['recovery_amount']=recovery
                recovery_cost=m(p,'recovery_collection_cost') if recovery>0 else Z
                # Recovery event is a dated negotiated workout; residual debt remains reported.
                active=None
        decision=''; approved=Z
        if active is None and not ever_default and len(loans)<p['max_cycles'] and day>=next_day and day<=p['origination_cutoff_day'] and not sales and not receipts:
            approved,decision=repeat_limit(p,cash,loans[-1] if loans else None)
            if approved>0:
                cycle=len(loans)+1; terms=trading_terms(p,s,merchant,cycle)
                extension=s['due_extension_days'] if terms['affected'] else 0
                loan=dict(merchant_id=merchant['id'],segment=merchant['segment'],cycle=cycle,
                          loan_id=f"{merchant['id']}-C{cycle:02d}", origin_day=day,original_due_day=day+p['tenor_days'],
                          due_day=day+p['tenor_days']+extension,principal=approved,principal_remaining=approved,
                          contract_fee=approved*m(p,'fee_rate_per_cycle'),fee_remaining=approved*m(p,'fee_rate_per_cycle'),
                          fee_accrued=Z,principal_collected=Z,fees_collected=Z,written_off_principal=Z,
                          default_fee_uncollected=Z,settled_day=None,default_day=None,recovery_day=None,recovery_amount=Z,
                          eligibility_documented=merchant['guarantee_eligible'],support_cost=Z,**terms)
                if s['support'] and terms['affected']:
                    support_cost=m(p,'support_cost_per_affected_loan');loan['support_cost']=support_cost
                loans.append(loan);active=loan;origination=approved;stock_received=approved;inventory+=approved
                total_cost=approved*terms['sell_through'];daily_cost=total_cost/dec(terms['sales_days'])
                for t in range(1,terms['sales_days']+1):
                    cost=daily_cost if t<terms['sales_days'] else total_cost-daily_cost*(terms['sales_days']-1)
                    sales[day+t]=(cost,cost*(1+terms['markup']),terms['lag'])
        performing=sum((l['principal_remaining'] for l in loans if l['default_day'] is None),Z)
        default_outstanding=sum((l['principal_remaining'] for l in loans if l['default_day'] is not None),Z)
        unpaid_fee=sum((l['fee_remaining'] for l in loans),Z)
        loan_service=m(p,'servicing_cost_per_open_loan_day') if active is not None and active['default_day'] is None else Z
        row=dict(scenario='',merchant_id=merchant['id'],segment=merchant['segment'],day=day,cycle=len(loans),
                 opening_cash=start_cash,distributor_disbursement=origination,stock_received_cost=stock_received,
                 sales_revenue=sales_revenue,cost_of_goods_sold=cogs,settled_sales_receipts=receipt,
                 operating_payments=operating,operating_expense_accrued=operating_accrual,closing_operating_arrears=operating_arrears,household_payments=household,household_consumption_shortfall=household_gap,essential_payment_shortfall=shortfall,
                 principal_repayment=principal_paid,fee_repayment=fee_paid,fee_accrual=fee_accrual,
                 principal_written_off=default_principal,post_default_recovery=recovery,salvage_cash=salvage,
                 inventory_disposed_cost=inventory_disposed,closing_cash=cash,closing_inventory_cost=inventory,
                 closing_receivables=receivables,performing_principal=performing,unresolved_default_principal=default_outstanding,
                 unpaid_contract_fee=unpaid_fee,servicing_cost=loan_service,support_cost=support_cost,
                 collection_cost=default_cost+recovery_cost,repeat_decision=decision)
        residual=cash-(start_cash+receipt+salvage-operating-household-principal_paid-fee_paid-recovery)
        if abs(residual)>TOL:raise AssertionError('merchant cash reconciliation')
        if min(cash,inventory,receivables)<-TOL:raise AssertionError('negative merchant balance')
        row['cash_reconciliation_error']=residual
        latest=loans[-1] if loans else None
        row['days_past_due']=max(0,day-latest['due_day']) if latest and latest['principal_remaining']+latest['fee_remaining']>TOL and latest['settled_day'] is None else 0
        row['state']=('default/workout' if latest and latest['default_day'] is not None else 'arrears' if row['days_past_due']>0 else 'settled' if latest and latest['settled_day'] is not None else 'performing')
        row['contract_due_balance']=(latest['principal_remaining']+latest['fee_remaining']) if latest and day>=latest['due_day'] else Z
        rows.append(row)
    return rows,loans


def layer_total(loss,p):
    first=min(loss,m(p,'guarantee_first_layer_width'))*m(p,'guarantee_first_layer_cap')/m(p,'guarantee_first_layer_width')
    second=min(max(Z,loss-m(p,'guarantee_first_layer_width')),m(p,'guarantee_second_layer_width'))*m(p,'guarantee_second_layer_cap')/m(p,'guarantee_second_layer_width')
    return first+second


def guarantee_run(p,s,loans):
    covered=Z; cumulative_loss=Z; events=[];covered_loans=[];claims=[]
    for loan in sorted(loans,key=lambda l:(l['origin_day'],l['merchant_id'],l['cycle'])):
        eligible=(loan['eligibility_documented'] and loan['origin_day']<=p['guarantee_origination_cutoff_day'] and
                  covered+loan['principal']<=m(p,'guarantee_eligible_origination_budget'))
        loan['guarantee_covered']=eligible
        loan['guarantee_exclusion_reason']=('' if eligible else 'documentation, origination cutoff or cumulative inclusion budget')
        if eligible:covered+=loan['principal'];covered_loans.append(loan)
    for loan in sorted((l for l in covered_loans if l['default_day'] is not None),key=lambda l:(l['default_day'],l['merchant_id'],l['cycle'])):
        loss=loan['written_off_principal']; claim=layer_total(cumulative_loss+loss,p)-layer_total(cumulative_loss,p)
        cumulative_loss+=loss
        submission=loan['default_day']+p['guarantee_submission_lag_days']
        acceptance=submission+p['guarantee_acceptance_lag_days']
        settlement=acceptance+s['claim_settlement_lag_days']
        covered_fraction=claim/loss if loss else Z
        recovery_share=loan['recovery_amount']*covered_fraction
        recovery_day=loan['recovery_day']
        # Recovery before settlement reduces cash claim; later recovery is remitted at recovery.
        pre_adjust=recovery_share if recovery_day is not None and recovery_day<=settlement else Z
        paid=claim-pre_adjust
        claim_row=dict(loan_id=loan['loan_id'],merchant_id=loan['merchant_id'],default_day=loan['default_day'],eligible_loss=loss,
                       cumulative_eligible_loss=cumulative_loss,allocated_claim=claim,coverage_fraction=covered_fraction,
                       submitted_day=submission,accepted_day=acceptance,settled_day=settlement,
                       pre_settlement_recovery_adjustment=pre_adjust,settlement_cash=paid,
                       post_settlement_recovery_remittance=recovery_share-pre_adjust,recovery_day=recovery_day)
        claims.append(claim_row)
        for state,day,amount in [('submitted',submission,claim),('accepted',acceptance,claim),('settled',settlement,paid)]:
            events.append(dict(day=day,loan_id=loan['loan_id'],state=state,amount=amount))
        if pre_adjust:
            events.append(dict(day=recovery_day,loan_id=loan['loan_id'],state='pre_settlement_recovery_adjustment',amount=pre_adjust))
        elif recovery_share:
            events.append(dict(day=recovery_day,loan_id=loan['loan_id'],state='recovery_remitted',amount=recovery_share))
    return covered,claims,sorted(events,key=lambda e:(e['day'],e['loan_id'],e['state']))


def lender_run(p, s, rows, loans, claims, events, protection):
    cash=Z;borrowing=Z;output=[];pending=Z;unaccepted=Z
    claim_by_day={}
    for event in events:claim_by_day.setdefault(event['day'],[]).append(event)
    daily={}
    for row in rows:daily.setdefault(row['day'],[]).append(row)
    covered_ids={l['loan_id'] for l in loans if l['guarantee_covered']}
    for day in range(p['runoff_days']+1):
        batch=daily[day];total=lambda key:sum((r[key] for r in batch),Z)
        disb=total('distributor_disbursement');principal=total('principal_repayment');fees=total('fee_repayment')
        recover=total('post_default_recovery');writeoff=total('principal_written_off')
        service=total('servicing_cost');collection=total('collection_cost');support=total('support_cost')
        origin_cost=sum((m(p,'origination_cost') for r in batch if r['distributor_disbursement']>0),Z)
        guarantee_fee=Z
        if protection:
            # Fee on closing performing principal each day, including origin day and excluding fully repaid/default day.
            for r in batch:
                loan_id=f"{r['merchant_id']}-C{r['cycle']:02d}"
                if loan_id in covered_ids:
                    guarantee_fee+=r['performing_principal']*m(p,'guarantee_annual_fee')/dec(p['day_count_denominator'])
        funding_cost=borrowing*m(p,'annual_funding_rate')/dec(p['day_count_denominator'])
        received=remitted=submitted=accepted=adjustment=Z
        if protection:
            for e in claim_by_day.get(day,[]):
                if e['state']=='submitted':submitted+=e['amount']
                elif e['state']=='accepted':accepted+=e['amount']
                elif e['state']=='settled':received+=e['amount']
                elif e['state']=='pre_settlement_recovery_adjustment':adjustment+=e['amount']
                elif e['state']=='recovery_remitted':remitted+=e['amount']
        pending=unaccepted=Z
        if protection:
            for c in claims:
                adjustment_to_date=c['pre_settlement_recovery_adjustment'] if c['recovery_day'] is not None and c['recovery_day']<=day else Z
                net_claim=c['allocated_claim']-adjustment_to_date
                if c['accepted_day']<=day<c['settled_day']:pending+=net_claim
                if c['submitted_day']<=day<c['accepted_day']:unaccepted+=net_claim
        opening_net=cash-borrowing
        operating_flow=principal+fees+recover+received-disb-service-collection-support-origin_cost-guarantee_fee-remitted
        closing_net=opening_net+operating_flow-funding_cost
        cash=max(Z,closing_net);borrowing=max(Z,-closing_net)
        profit=fees-service-collection-support-origin_cost-guarantee_fee-funding_cost-writeoff+recover+received-remitted
        output.append(dict(day=day,protection=protection,principal_disbursed=disb,principal_collected=principal,
                           fees_collected=fees,fees_accrued=total('fee_accrual'),written_off_principal=writeoff,
                           post_default_recovery=recover,claim_submitted=submitted,claim_accepted=accepted,
                           guarantee_cash_received=received,recovery_remitted=remitted,pre_settlement_recovery_adjustment=adjustment,
                           claims_submitted_pending_acceptance=unaccepted,accepted_unsettled_claims=pending,
                           guarantee_fees=guarantee_fee,servicing_cost=service,collection_cost=collection,origination_cost=origin_cost,
                           support_cost=support,funding_cost=funding_cost,closing_cash=cash,closing_funding=borrowing,
                           net_cash=closing_net,cash_flow_before_funding_cost=operating_flow,
                           performing_principal=total('performing_principal'),unresolved_default_principal=total('unresolved_default_principal'),
                           lender_profit=profit,net_cash_reconciliation_error=closing_net-opening_net-operating_flow+funding_cost))
        if min(cash,borrowing,pending,unaccepted)<-TOL:raise AssertionError('negative lender/claim balance')
    return output


def run_scenario(p, name):
    validate(p);s=p['scenarios'][name];rows=[];loans=[]
    for merchant in p['merchants']:
        r,l=merchant_run(p,s,merchant)
        for row in r:row['scenario']=name
        rows.extend(r);loans.extend(l)
    covered,claims,events=guarantee_run(p,s,loans)
    outputs={};summaries=[]
    last_rows=[r for r in rows if r['day']==p['runoff_days']]
    merchant_sum=lambda key:sum((r[key] for r in rows),Z)
    last_sum=lambda key:sum((r[key] for r in last_rows),Z)
    for protection in [False,True]:
        ledger=lender_run(p,s,rows,loans,claims,events,protection);outputs['protected' if protection else 'unprotected']=ledger
        total=lambda key:sum((r[key] for r in ledger),Z)
        written=total('written_off_principal');recovery=total('post_default_recovery')
        profit=total('lender_profit');performing=ledger[-1]['performing_principal'];net_cash=ledger[-1]['net_cash']
        # Principal loss recognises write-off; residual performing principal bridges profit and cash.
        reconciliation=profit-(net_cash+performing)
        if abs(reconciliation)>TOL:raise AssertionError('profit/cash/principal bridge')
        summary=dict(scenario=name,label=s['label'],protection=protection,loans_originated=len(loans),repeat_loans=len(loans)-len(p['merchants']),
                     principal_disbursed=total('principal_disbursed'),principal_collected=total('principal_collected'),fees_collected=total('fees_collected'),
                     fees_accrued=total('fees_accrued'),uncollected_contract_fees=sum((l['fee_remaining'] for l in loans),Z),
                     written_off_principal=written,post_default_recovery=recovery,closing_performing_principal=performing,
                     closing_unresolved_default_principal=last_sum('unresolved_default_principal'),
                     merchant_closing_cash=last_sum('closing_cash'),merchant_closing_inventory_cost=last_sum('closing_inventory_cost'),
                     merchant_closing_receivables=last_sum('closing_receivables'),
                     merchant_operating_profit=merchant_sum('sales_revenue')-merchant_sum('cost_of_goods_sold')-merchant_sum('operating_expense_accrued')-merchant_sum('fee_accrual')-merchant_sum('inventory_disposed_cost')+merchant_sum('salvage_cash'),
                     household_shortfall=merchant_sum('household_consumption_shortfall'),household_payments=merchant_sum('household_payments'),
                     operating_expense_accrued=merchant_sum('operating_expense_accrued'),closing_operating_arrears=last_sum('closing_operating_arrears'),
                     defaults=sum(l['default_day'] is not None for l in loans),
                     late_cures=sum(l['settled_day'] is not None and l['settled_day']>l['original_due_day'] for l in loans),
                     settlements_after_approved_due=sum(l['settled_day'] is not None and l['settled_day']>l['due_day'] for l in loans),
                     covered_originations=covered,eligible_loss=sum((c['eligible_loss'] for c in claims),Z),
                     claims_submitted=total('claim_submitted'),claims_accepted=total('claim_accepted'),
                     guarantee_cash_received=total('guarantee_cash_received'),recovery_remitted=total('recovery_remitted'),
                     accepted_unsettled_claims=ledger[-1]['accepted_unsettled_claims'],
                     submitted_unaccepted_claims=ledger[-1]['claims_submitted_pending_acceptance'],
                     guarantee_fees=total('guarantee_fees'),funding_cost=total('funding_cost'),servicing_cost=total('servicing_cost'),
                     collection_cost=total('collection_cost'),origination_cost=total('origination_cost'),support_cost=total('support_cost'),
                     retained_credit_loss=written-recovery-total('guarantee_cash_received')+total('recovery_remitted'),
                     lender_profit=profit,peak_funding=max(r['closing_funding'] for r in ledger),closing_funding=ledger[-1]['closing_funding'],
                     closing_lender_cash=ledger[-1]['closing_cash'],profit_cash_reconciliation_error=reconciliation)
        summaries.append(summary)
    return dict(name=name,parameters=deepcopy(s),merchant_daily=rows,loans=loans,claims=claims,guarantee_events=events,
                lender_daily=outputs,summaries=summaries)


def run_all(p):
    return {name:run_scenario(p,name) for name in p['scenarios']}
