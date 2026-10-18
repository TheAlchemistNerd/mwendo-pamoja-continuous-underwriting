"""Independent identities, actor balances and contract boundary tests."""
import copy
import json
import unittest
from decimal import Decimal as D
from pathlib import Path
from model import run_case, present_value, weekly_rate

P = json.loads((Path(__file__).parent / "assumptions.json").read_text(encoding="utf-8"))


class MobilityCaseTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.r = {s["id"]: run_case(P, s) for s in P["scenarios"]}

    def close(self, actual, expected, tolerance="0.00001"):
        self.assertLessEqual(abs(actual - D(str(expected))), D(tolerance))

    def test_baseline_independent_driver_budget(self):
        s = self.r["uninterrupted"]["summary"]
        self.close(s["driver_cash_surplus"], 156 * (70000 * .8 - 16000 - 12000 - 25000))
        self.close(s["collected_fees"], 156 * 25000)
        self.close(s["household_cash"], 156 * 12000)

    def test_independent_funding_interest_series(self):
        s = self.r["uninterrupted"]["summary"]
        # Equal-principal sum of opening balances = P * (N+1)/2.
        expected = D(1350000) * D(157) / 2 * weekly_rate(D("0.12"))
        self.close(s["total_debt_interest"], expected)
        self.close(s["total_debt_principal"], 1350000)
        self.close(s["funder_npv_at_contract_rate"], 0)

    def test_initial_equity_pays_actual_vehicle_and_cash_uses(self):
        s = self.r["uninterrupted"]["summary"]
        self.close(s["initial_operator_equity"], 1800000 + 30000 + 200000 - 1350000)
        self.close(s["additional_equity"], 0)

    def test_insurance_is_annual_cash_and_counted_once(self):
        rows = self.r["uninterrupted"]["weekly_ledger"]
        self.assertEqual([r["week"] for r in rows if r["insurance_cash"]], [1, 53, 105])
        self.close(sum(r["insurance_cash"] for r in rows), 390000)
        self.close(sum(r["maintenance_cash"] for r in rows), 280800)

    def test_nominal_equity_cash_reconciles_to_whole_contract(self):
        s = self.r["uninterrupted"]["summary"]
        expected = D(3900000) - 1800000 - 30000 - 390000 - 280800 - 124800 - s["total_debt_interest"]
        self.close(s["equity_net_cash"], expected)

    def test_every_actor_transfer_and_weekly_balance(self):
        for result in self.r.values():
            for r in result["weekly_ledger"]:
                for name in ["driver_cash_error", "operator_cash_error", "contractual_balance_error", "principal_error"]:
                    self.close(r[name], 0)
            net = result["actor_net_cash"]
            self.close(sum(net.values()), 0)
            self.close(net["driver"], result["summary"]["final_driver_wallet"])
            self.close(net["operator"], result["summary"]["final_operator_cash"])
            receipts = sum(e["amount"] for e in result["transfers"] if e["kind"] == "collected_package_payment")
            self.close(receipts, result["summary"]["collected_fees"])

    def test_twelve_day_shock_splits_across_two_weeks(self):
        rows = self.r["scheduled_repair"]["weekly_ledger"]
        self.assertEqual([(r["week"], r["unavailable_days"]) for r in rows if r["unavailable_days"]], [(13, 7), (14, 5)])
        self.close(sum(r["gross_fares"] for r in rows), 156 * 70000 - 12 * 10000)

    def test_driver_income_difference_has_independent_operating_identity(self):
        a, b = self.r["scheduled_repair"]["summary"], self.r["expedited_repair"]["summary"]
        saved_margin = D(10) / 7 * (70000 * D("0.8") - 16000)
        self.close(b["driver_cash_surplus"] - a["driver_cash_surplus"], saved_margin)
        self.close(a["collected_fees"], b["collected_fees"])

    def test_arrears_and_cure_are_contract_state_not_written_off_revenue(self):
        s = self.r["scheduled_repair"]["summary"]
        self.close(s["peak_arrears"], 50000)
        self.assertEqual(s["cure_week"], 32)
        self.close(s["final_arrears"], 0)
        self.close(self.r["expedited_repair"]["summary"]["peak_arrears"], 0)

    def test_repair_is_operator_paid_without_driver_debt(self):
        result = self.r["expedited_repair"]
        repair = [e for e in result["transfers"] if e["kind"] == "covered_repair"]
        self.assertEqual(len(repair), 1)
        self.assertEqual((repair[0]["payer"], repair[0]["payee"]), ("operator", "repair_supplier"))
        self.close(repair[0]["amount"], 35000)
        self.close(result["summary"]["billed_fees"], 3900000)

    def test_fee_credit_is_a_documented_waiver(self):
        plain = self.r["expedited_repair"]["summary"]
        waived = self.r["expedited_repair_fee_credit"]["summary"]
        self.close(waived["waived_fees"], 25000)
        self.close(plain["collected_fees"] - waived["collected_fees"], 25000)
        self.close(waived["driver_cash_surplus"] - plain["driver_cash_surplus"], 25000)
        self.close(plain["equity_net_cash"] - waived["equity_net_cash"], 25000)

    def test_vehicle_has_one_terminal_recipient(self):
        for result in self.r.values():
            s = result["summary"]
            self.assertTrue(s["vehicle_transferred"])
            self.close(s["driver_terminal_vehicle_value"], 450000)
            self.close(s["operator_terminal_sale"], 0)
            self.close(s["debt_final_principal"], 0)

    def test_zero_earnings_reports_shortfall_and_equity_need(self):
        scenario = copy.deepcopy(P["scenarios"][0])
        scenario.update(id="zero_earnings", shock_start_day=1, downtime_days=1092)
        result = run_case(P, scenario)
        s = result["summary"]
        self.close(s["collected_fees"], 0)
        self.close(s["final_arrears"], 3900000)
        self.close(s["household_shortfall"], 1872000 - 20000)
        self.assertGreater(s["additional_equity"], 0)
        self.assertFalse(s["vehicle_transferred"])
        self.close(s["driver_terminal_vehicle_value"], 0)
        self.close(s["operator_terminal_sale"], 450000)

    def test_zero_funding_rate_and_final_principal(self):
        p = copy.deepcopy(P)
        p["debt_annual_effective_rate"] = "0"
        s = run_case(p, p["scenarios"][0])["summary"]
        self.close(s["total_debt_interest"], 0)
        self.close(s["funder_npv_at_contract_rate"], 0)
        self.close(s["total_debt_principal"], 1350000)

    def test_wallet_floor_protects_payment_capacity(self):
        for result in self.r.values():
            for r in result["weekly_ledger"]:
                if r["collected_fee"] > 0:
                    self.assertGreaterEqual(r["driver_closing_cash"], D(10000))
                self.assertGreaterEqual(r["driver_closing_cash"], 0)

    def test_npv_has_year_fraction_and_no_repeated_terminal_asset(self):
        self.close(present_value([(52, D(110))], D("0.10")), 100)
        s = self.r["uninterrupted"]["summary"]
        self.close(s["driver_wealth_npv"] - s["driver_cash_npv"], D(450000) / D("1.1") ** 3)

    def test_unsupported_bad_inputs_fail(self):
        for field, value in [("platform_fraction", "1.01"), ("debt_advance", "9000000"), ("protected_driver_wallet", "30000")]:
            p = copy.deepcopy(P)
            p[field] = value
            with self.assertRaises(ValueError):
                run_case(p, p["scenarios"][0])

    def test_deterministic_reproduction(self):
        self.assertEqual(run_case(P, P["scenarios"][1]), self.r["scheduled_repair"])


if __name__ == "__main__":
    unittest.main()
