"""Full-term mobility cash model, using only the Python standard library.

Cash calculations use unrounded Decimal precision. Export rounding is a display
convention. A production contract must elect its own currency-rounding rule.
"""
from decimal import Decimal, getcontext

getcontext().prec = 40
D = Decimal
ZERO = D(0)
TOL = D("0.00000001")


def money(params, name):
    return D(str(params[name]))


def weekly_rate(annual):
    return (1 + annual) ** (D(1) / 52) - 1


def present_value(flows, annual):
    return sum((amount / (1 + annual) ** (D(week) / 52)
                for week, amount in flows), ZERO)


def validate(p, scenario):
    n = p["term_weeks"]
    if not isinstance(n, int) or n <= 0:
        raise ValueError("term_weeks must be a positive integer")
    names = ["vehicle_cost", "vehicle_terminal_value", "vehicle_sale_cost",
             "setup_cost", "opening_operator_cash", "operator_minimum_cash",
             "debt_advance", "weekly_package_due", "weekly_gross_fares",
             "weekly_energy_at_full_availability", "weekly_household_need",
             "opening_driver_wallet", "protected_driver_wallet", "target_driver_wallet",
             "insurance_cash_every_52_weeks", "weekly_routine_maintenance_cash",
             "weekly_administration_cash"]
    if any(money(p, k) < 0 for k in names):
        raise ValueError("cash assumptions must be non-negative")
    if not ZERO <= money(p, "platform_fraction") < 1:
        raise ValueError("platform_fraction must lie in [0,1)")
    if money(p, "protected_driver_wallet") > money(p, "target_driver_wallet"):
        raise ValueError("protected wallet must be at or below target")
    if money(p, "vehicle_terminal_value") > money(p, "vehicle_cost"):
        raise ValueError("terminal value exceeds the supported depreciating-asset case")
    if money(p, "vehicle_sale_cost") > money(p, "vehicle_terminal_value"):
        raise ValueError("sale cost exceeds sale value")
    initial_use = sum((money(p, k) for k in ["vehicle_cost", "setup_cost", "opening_operator_cash"]), ZERO)
    if money(p, "debt_advance") > initial_use:
        raise ValueError("debt exceeds opening funding requirement")
    for rate in ["debt_annual_effective_rate", "equity_annual_discount_rate", "driver_annual_discount_rate"]:
        if money(p, rate) < 0:
            raise ValueError("this case supports non-negative rates")
    if not isinstance(scenario["downtime_days"], int) or scenario["downtime_days"] < 0:
        raise ValueError("downtime_days must be a non-negative integer")
    if scenario["shock_start_day"] < 1 or scenario["shock_start_day"] + scenario["downtime_days"] - 1 > 7 * n:
        raise ValueError("downtime must fit within the contract")
    if not 1 <= scenario["repair_week"] <= n or D(scenario["repair_cost"]) < 0:
        raise ValueError("repair date and cost are invalid")
    waived = scenario.get("waived_weeks", [])
    if len(set(waived)) != len(waived) or any(not 1 <= w <= n for w in waived):
        raise ValueError("waiver dates must be unique contract weeks")


def run_case(p, scenario):
    validate(p, scenario)
    n = p["term_weeks"]
    m = lambda key: money(p, key)
    wallet = m("opening_driver_wallet")
    operator_cash = m("opening_operator_cash")
    principal = m("debt_advance")
    initial_equity = m("vehicle_cost") + m("setup_cost") + operator_cash - principal
    debt_rate = weekly_rate(m("debt_annual_effective_rate"))
    arrears = ZERO
    total_due = total_collected = total_waived = ZERO
    rows, flows = [], []
    owner_flows = [(0, -initial_equity)]
    funder_flows = [(0, -principal)]
    driver_flows = [(0, -wallet)]
    operating_flows = [(0, -m("vehicle_cost") - m("setup_cost"))]

    def transfer(week, payer, payee, amount, kind):
        if amount < 0:
            raise AssertionError("negative payment")
        if amount:
            flows.append({"week": week, "payer": payer, "payee": payee,
                          "amount": amount, "kind": kind})

    transfer(0, "funder", "operator", principal, "vehicle_debt_advance")
    transfer(0, "equity", "operator", initial_equity, "initial_equity")
    transfer(0, "operator", "vehicle_vendor", m("vehicle_cost"), "vehicle_purchase")
    transfer(0, "operator", "setup_supplier", m("setup_cost"), "setup")
    transfer(0, "driver_savings", "driver", wallet, "opening_wallet")
    for week in range(1, n + 1):
        start, end = 7 * (week - 1) + 1, 7 * week
        shock_start = scenario["shock_start_day"]
        shock_end = shock_start + scenario["downtime_days"] - 1
        unavailable = max(0, min(end, shock_end) - max(start, shock_start) + 1)
        availability = D(7 - unavailable) / 7
        driver_open, operator_open, principal_open, arrears_open = wallet, operator_cash, principal, arrears
        gross = m("weekly_gross_fares") * availability
        commission = gross * m("platform_fraction")
        energy = m("weekly_energy_at_full_availability") * availability
        operating_margin = gross - commission - energy
        if operating_margin < 0:
            raise ValueError("operating cash is negative; add explicit working-capital funding before running")
        wallet += operating_margin
        household_paid = min(wallet, m("weekly_household_need"))
        household_shortfall = m("weekly_household_need") - household_paid
        wallet -= household_paid
        fee_waived = m("weekly_package_due") if week in scenario.get("waived_weeks", []) else ZERO
        billed = m("weekly_package_due") - fee_waived
        due = arrears + billed
        collected = min(due, max(ZERO, wallet - m("protected_driver_wallet")))
        wallet -= collected
        arrears = due - collected
        driver_distribution = max(ZERO, wallet - m("target_driver_wallet"))
        wallet -= driver_distribution
        total_due += billed
        total_collected += collected
        total_waived += fee_waived
        transfer(week, "riders", "driver", gross, "gross_fares")
        transfer(week, "driver", "platform", commission, "platform_fee")
        transfer(week, "driver", "energy_supplier", energy, "energy")
        transfer(week, "driver", "household", household_paid, "essential_household")
        transfer(week, "driver", "operator", collected, "collected_package_payment")
        transfer(week, "driver", "driver_discretionary", driver_distribution, "driver_surplus")
        driver_flows.append((week, driver_distribution))

        # Annual premium is a dated cash payment, distinct from an allocation rate.
        insurance = m("insurance_cash_every_52_weeks") if (week - 1) % 52 == 0 else ZERO
        routine = m("weekly_routine_maintenance_cash")
        admin = m("weekly_administration_cash")
        repair = D(scenario["repair_cost"]) if week == scenario["repair_week"] else ZERO
        interest = principal * debt_rate
        repaid_principal = principal if week == n else m("debt_advance") / n
        principal -= repaid_principal
        operator_cost = insurance + routine + admin + repair
        operating_flows.append((week, collected - operator_cost))
        operator_cash += collected - operator_cost - interest - repaid_principal
        next_premium_week = (((week - 1) // 52) + 1) * 52 + 1
        premium_funding_target = m("insurance_cash_every_52_weeks") * D((week - 1) % 52) / 52 if next_premium_week <= n else ZERO
        target = ZERO if week == n else m("operator_minimum_cash") + premium_funding_target
        # Explicit sponsor equity calls fund any cash need; no hidden overdraft.
        equity_call = max(ZERO, target - operator_cash)
        operator_cash += equity_call
        terminal_driver_asset = terminal_operator_sale = terminal_sale_cost = ZERO
        transferred = False
        if week == n:
            transferred = arrears <= TOL and principal <= TOL
            if transferred:
                terminal_driver_asset = m("vehicle_terminal_value")
            else:
                terminal_operator_sale = m("vehicle_terminal_value")
                terminal_sale_cost = m("vehicle_sale_cost")
                operator_cash += terminal_operator_sale - terminal_sale_cost
                operating_flows.append((week, terminal_operator_sale - terminal_sale_cost))
                transfer(week, "vehicle_buyer", "operator", terminal_operator_sale, "vehicle_sale")
                transfer(week, "operator", "disposal_supplier", terminal_sale_cost, "sale_cost")
        equity_distribution = max(ZERO, operator_cash - target)
        operator_cash -= equity_distribution
        owner_flows.append((week, equity_distribution - equity_call))
        funder_flows.append((week, interest + repaid_principal))
        for payee, amount, kind in [("insurer", insurance, "annual_insurance_premium"),
                                   ("maintenance_supplier", routine, "routine_maintenance"),
                                   ("administration_supplier", admin, "administration"),
                                   ("repair_supplier", repair, "covered_repair"),
                                   ("funder", interest, "debt_interest"),
                                   ("funder", repaid_principal, "debt_principal"),
                                   ("equity", equity_distribution, "equity_distribution")]:
            transfer(week, "operator", payee, amount, kind)
        transfer(week, "equity", "operator", equity_call, "additional_equity")
        driver_error = driver_open + gross - commission - energy - household_paid - collected - driver_distribution - wallet
        operator_error = operator_open + collected + equity_call + terminal_operator_sale - operator_cost - interest - repaid_principal - terminal_sale_cost - equity_distribution - operator_cash
        contract_error = arrears_open + billed - collected - arrears
        principal_error = principal_open - repaid_principal - principal
        rows.append(dict(week=week, unavailable_days=unavailable, availability=availability,
                         driver_opening_cash=driver_open, gross_fares=gross, platform_fee=commission,
                         energy_cash=energy, household_paid=household_paid, household_shortfall=household_shortfall,
                         scheduled_package_fee=m("weekly_package_due"), fee_waived=fee_waived,
                         billed_fee=billed, collected_fee=collected, arrears=arrears,
                         driver_distribution=driver_distribution, driver_closing_cash=wallet,
                         operator_opening_cash=operator_open, insurance_cash=insurance,
                         maintenance_cash=routine, administration_cash=admin, repair_cash=repair,
                         debt_opening_principal=principal_open, debt_interest=interest,
                         debt_principal_paid=repaid_principal, debt_closing_principal=principal,
                         additional_equity=equity_call, equity_distribution=equity_distribution,
                         operator_closing_cash=operator_cash, vehicle_book_proxy=m("vehicle_cost") - (m("vehicle_cost") - m("vehicle_terminal_value")) * D(week) / n,
                         driver_terminal_asset=terminal_driver_asset, operator_terminal_sale=terminal_operator_sale,
                         sale_cost=terminal_sale_cost, driver_cash_error=driver_error,
                         operator_cash_error=operator_error, contractual_balance_error=contract_error,
                         principal_error=principal_error))
    driver_flows.append((n, wallet))
    asset_value = rows[-1]["driver_terminal_asset"]
    first_arrears = next((r["week"] for r in rows if r["arrears"] > TOL), None)
    cure = next((r["week"] for r in rows if first_arrears and r["week"] > first_arrears and r["arrears"] <= TOL), None)
    actor_net = {}
    for event in flows:
        actor_net[event["payer"]] = actor_net.get(event["payer"], ZERO) - event["amount"]
        actor_net[event["payee"]] = actor_net.get(event["payee"], ZERO) + event["amount"]
    errors = [abs(r[k]) for r in rows for k in ["driver_cash_error", "operator_cash_error", "contractual_balance_error", "principal_error"]]
    errors.extend([abs(actor_net.get("driver", ZERO) - wallet), abs(actor_net.get("operator", ZERO) - operator_cash), abs(sum(actor_net.values(), ZERO))])
    summary = dict(scenario=scenario["id"], term_weeks=n, unavailable_days=sum(r["unavailable_days"] for r in rows),
                   billed_fees=total_due, collected_fees=total_collected, waived_fees=total_waived,
                   final_arrears=arrears, peak_arrears=max(r["arrears"] for r in rows), first_arrears_week=first_arrears,
                   cure_week=cure, household_cash=sum((r["household_paid"] for r in rows), ZERO),
                   household_shortfall=sum((r["household_shortfall"] for r in rows), ZERO),
                   driver_cash_surplus=sum((r["driver_distribution"] for r in rows), ZERO),
                   final_driver_wallet=wallet, driver_terminal_vehicle_value=asset_value,
                   driver_cash_npv=present_value(driver_flows, m("driver_annual_discount_rate")),
                   driver_wealth_npv=present_value(driver_flows + [(n, asset_value)], m("driver_annual_discount_rate")),
                   initial_operator_equity=initial_equity, additional_equity=sum((r["additional_equity"] for r in rows), ZERO),
                   equity_distributions=sum((r["equity_distribution"] for r in rows), ZERO),
                   equity_net_cash=sum((amount for _, amount in owner_flows), ZERO),
                   equity_npv=present_value(owner_flows, m("equity_annual_discount_rate")),
                   unlevered_operating_npv=present_value(operating_flows, m("equity_annual_discount_rate")),
                   total_insurance_cash=sum((r["insurance_cash"] for r in rows), ZERO),
                   total_maintenance_cash=sum((r["maintenance_cash"] for r in rows), ZERO),
                   total_debt_interest=sum((r["debt_interest"] for r in rows), ZERO),
                   total_debt_principal=sum((r["debt_principal_paid"] for r in rows), ZERO),
                   funder_npv_at_contract_rate=present_value(funder_flows, m("debt_annual_effective_rate")),
                   debt_final_principal=principal, final_operator_cash=operator_cash,
                   vehicle_transferred=bool(asset_value), operator_terminal_sale=rows[-1]["operator_terminal_sale"],
                   maximum_reconciliation_error=max(errors))
    if summary["maximum_reconciliation_error"] > TOL:
        raise AssertionError("cash/principal invariant failed")
    return {"summary": summary, "weekly_ledger": rows, "transfers": flows,
            "actor_net_cash": actor_net, "equity_cash_flows": owner_flows,
            "funder_cash_flows": funder_flows, "driver_cash_flows": driver_flows}
