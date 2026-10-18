import json
import unittest
from copy import deepcopy
from decimal import Decimal as D
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parent))
from model import run_all,run_scenario,layer_total,TOL

class FourGCaseTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.p=json.loads((Path(__file__).parent/'assumptions.json').read_text(encoding='utf-8-sig'))
        cls.cases=run_all(cls.p)
    def near(self,a,b):self.assertLessEqual(abs(a-b),TOL)
    def test_first_cycle_hand_calculation(self):
        row=next(r for r in self.cases['baseline']['merchant_daily'] if r['merchant_id']=='S01' and r['day']==21)
        self.near(row['closing_cash'],D(32650));self.near(row['principal_repayment'],D(100000));self.near(row['fee_repayment'],D(5000))
    def test_distributor_finance_does_not_enter_merchant_cash(self):
        row=self.cases['baseline']['merchant_daily'][0]
        self.near(row['closing_cash'],D(20000));self.near(row['stock_received_cost'],D(100000))
    def test_all_merchant_daily_cash_reconciles(self):
        for case in self.cases.values():
            for r in case['merchant_daily']:self.near(r['cash_reconciliation_error'],D(0))
    def test_inventory_and_receivables_reconcile(self):
        for case in self.cases.values():
            for mid in {r['merchant_id'] for r in case['merchant_daily']}:
                rows=[r for r in case['merchant_daily'] if r['merchant_id']==mid]
                self.near(sum((r['stock_received_cost']-r['cost_of_goods_sold']-r['inventory_disposed_cost'] for r in rows),D(0)),rows[-1]['closing_inventory_cost'])
                self.near(sum((r['sales_revenue']-r['settled_sales_receipts'] for r in rows),D(0)),rows[-1]['closing_receivables'])
    def test_operating_payables_reconcile(self):
        for case in self.cases.values():
            for mid in {r['merchant_id'] for r in case['merchant_daily']}:
                rows=[r for r in case['merchant_daily'] if r['merchant_id']==mid]
                self.near(sum((r['operating_expense_accrued']-r['operating_payments'] for r in rows),D(0)),rows[-1]['closing_operating_arrears'])
    def test_merchant_net_wealth_bridge(self):
        for case in self.cases.values():
            s=case['summaries'][0]
            wealth=s['merchant_closing_cash']+s['merchant_closing_inventory_cost']+s['merchant_closing_receivables']-s['closing_operating_arrears']-s['closing_performing_principal']-s['closing_unresolved_default_principal']-s['uncollected_contract_fees']
            self.near(wealth,D(self.p['opening_cash'])*len(self.p['merchants'])+s['merchant_operating_profit']-s['household_payments'])
    def test_loan_principal_bridge(self):
        for case in self.cases.values():
            for l in case['loans']:self.near(l['principal'],l['principal_collected']+l['recovery_amount']+l['principal_remaining'])
    def test_lender_profit_cash_bridge(self):
        for case in self.cases.values():
            for s in case['summaries']:self.near(s['profit_cash_reconciliation_error'],D(0))
    def test_lender_daily_cash_bridge(self):
        for case in self.cases.values():
            for ledger in case['lender_daily'].values():
                for r in ledger:self.near(r['net_cash_reconciliation_error'],D(0))
    def test_protection_preserves_borrower_scenario(self):
        for case in self.cases.values():
            a,b=case['summaries']
            for key in ['principal_disbursed','principal_collected','fees_collected','written_off_principal','post_default_recovery','merchant_closing_cash','defaults']:self.assertEqual(a[key],b[key])
    def test_no_repeat_during_unsettled_loan_or_after_default(self):
        for case in self.cases.values():
            for mid in {l['merchant_id'] for l in case['loans']}:
                loans=[l for l in case['loans'] if l['merchant_id']==mid]
                for a,b in zip(loans,loans[1:]):
                    self.assertIsNone(a['default_day']);self.assertGreaterEqual(b['origin_day'],a['settled_day']+self.p['repeat_cooldown_days'])
    def test_guarantee_origination_budget_and_documentation(self):
        for case in self.cases.values():
            self.assertLessEqual(case['summaries'][0]['covered_originations'],D(self.p['guarantee_eligible_origination_budget']))
            self.assertFalse(any(l['guarantee_covered'] for l in case['loans'] if l['merchant_id']=='V03'))
    def test_guarantee_layers_exact_boundaries(self):
        self.near(layer_total(D(0),self.p),D(0));self.near(layer_total(D(220000),self.p),D(200000))
        self.near(layer_total(D(4440000),self.p),D(620000));self.near(layer_total(D(9000000),self.p),D(620000))
    def test_correlated_loss_uses_second_layer(self):
        c=self.cases['correlated_loss'];self.assertGreater(c['summaries'][1]['eligible_loss'],D(220000))
        self.assertGreater(sum((x['allocated_claim'] for x in c['claims']),D(0)),D(200000))
    def test_recovery_sharing_and_caps(self):
        for case in self.cases.values():
            for c in case['claims']:
                self.near(c['allocated_claim'],c['settlement_cash']+c['pre_settlement_recovery_adjustment'])
                l=next(l for l in case['loans'] if l['loan_id']==c['loan_id'])
                self.near(l['recovery_amount']*c['coverage_fraction'],c['pre_settlement_recovery_adjustment']+c['post_settlement_recovery_remittance'])
    def test_claim_delay_changes_timing_not_total_net_protection(self):
        a=self.cases['delayed_sales']['summaries'][1];b=self.cases['long_claim_delay']['summaries'][1]
        self.near(a['guarantee_cash_received']-a['recovery_remitted'],b['guarantee_cash_received']-b['recovery_remitted'])
        self.assertGreater(b['funding_cost'],a['funding_cost'])
    def test_claim_recovery_before_submission_and_acceptance(self):
        for recovery_day in [0,7,15,45]:
            p=deepcopy(self.p);p['recovery_days_after_default']=recovery_day
            c=run_scenario(p,'delayed_sales')
            self.assertTrue(all(r['accepted_unsettled_claims']>=-TOL and r['claims_submitted_pending_acceptance']>=-TOL for r in c['lender_daily']['protected']))
    def test_zero_fee_and_zero_guarantee_cap(self):
        p=deepcopy(self.p);p['fee_rate_per_cycle']='0';p['guarantee_first_layer_cap']='0';p['guarantee_second_layer_cap']='0'
        c=run_scenario(p,'delayed_sales')
        self.near(c['summaries'][1]['fees_collected'],D(0));self.near(c['summaries'][1]['guarantee_cash_received'],D(0))
    def test_late_claim_remains_receivable(self):
        p=deepcopy(self.p);p['scenarios']['delayed_sales']['claim_settlement_lag_days']=400
        c=run_scenario(p,'delayed_sales');s=c['summaries'][1]
        self.assertGreater(s['accepted_unsettled_claims'],D(0));self.near(s['guarantee_cash_received'],D(0))
    def test_guarantee_fee_closing_daily_exposure(self):
        p=deepcopy(self.p);p['merchants']=p['merchants'][:1];p['max_cycles']=1
        c=run_scenario(p,'baseline')
        self.near(c['summaries'][1]['guarantee_fees'],D(100000)*D('0.01')/365*21)
    def test_retained_loss_plus_protection_equals_gross_loss(self):
        for c in self.cases.values():
            s=c['summaries'][1]
            self.near(s['retained_credit_loss']+s['guarantee_cash_received']-s['recovery_remitted'],s['written_off_principal']-s['post_default_recovery'])
    def test_reproducible_exact_results(self):
        self.assertEqual(self.cases['delayed_sales']['summaries'],run_scenario(self.p,'delayed_sales')['summaries'])
    def test_support_cost_and_observed_input_boundary(self):
        c=self.cases['support_and_reschedule'];s=c['summaries'][0]
        self.assertGreater(s['support_cost'],D(0));self.assertEqual(s['defaults'],0)
    def test_invalid_assumptions_fail(self):
        p=deepcopy(self.p);p['fee_rate_per_cycle']='-1'
        with self.assertRaises(ValueError):run_scenario(p,'baseline')

if __name__=='__main__':unittest.main(verbosity=2)
