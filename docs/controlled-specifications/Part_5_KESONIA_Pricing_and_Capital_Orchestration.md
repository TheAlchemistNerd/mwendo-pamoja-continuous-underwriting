---
title: "Implementation Documentation: KESONIA Pricing, SPV Cash Flows, and Capital Orchestration"
author: "Nevil Maloba"
date: "24 August 2026"
status: "Controlled financial-methodology specification; commercial terms remain subject to diligence and execution"
---

# Purpose and Financial Boundary

This chapter connects the Central Bank of Kenya's KESONIA-based customer-pricing framework to product cash flows, SPV funding, debt service, reserves, the priority of payments, investor returns, accounting interfaces, and stress testing. It keeps five economically different quantities separate:

`CREDIT_RISK_MODEL_AND_LOSS_ARCHITECTURE_SPECIFICATION.md` governs the path from calibrated borrower posterior through timing, EAD, cure, recovery, refund, dependence, and monthly cohort cash. This chapter governs how those cash flows enter pricing, ALM, reserves, tranches, and the waterfall.

1. the reference rate used in a customer contract;
2. the customer's risk-based pricing premium and fees;
3. the coupon or yield promised to an SPV investor;
4. the legal entity's internal cost of funds or hurdle rate; and
5. regulatory capital or transaction credit enhancement.

The primary transaction is a USD-equivalent 9 million SPV capitalisation, but the operating, receivable, bank-account, reserve, waterfall, and debt-service currency is KES. USD amounts are presentation translations unless an executed document creates a USD obligation. Any actual cross-currency funding requires a separate hedge, basis, collateral, counterparty, and accounting analysis.

All rates, fees, taxes, costs, and recovery assumptions must carry an as-of date, source, units, payment frequency, day-count convention, and evidence status. Unsupported constants must not be embedded in code.

# Controlled Notation

| Symbol | Definition | Boundary |
|---|---|---|
| \(r_i\) | Published KESONIA fixing applicable to observation day \(i\) | Official overnight reference rate |
| \(d_i\) | Calendar days for which fixing \(r_i\) applies | Contract convention |
| \(D\) | Annual day-count denominator | Contract convention |
| \(K_{\mathrm{RBCP}}\) | Customer risk-based credit-pricing premium | Customer lending rate |
| \(m_A\), \(m_B\) | Class A and Class B SPV note margins | Investor liability pricing |
| \(f_j\) | Customer fee or charge \(j\) | Total cost of credit |
| \(EL\) | Expected loss under defined horizon and measure | Pricing and risk input |
| \(OpEx\) | Allocated operating and servicing cost | Commercial input |
| \(CoC\) | Economic cost of capital or target return | Commercial input |
| \(K_{\mathrm{cap}}\) | Regulatory capital amount | Lender prudential calculation |
| \(OC_t\) | Overcollateralisation ratio at time \(t\) | SPV covenant |
| \(CRA_t\) | Cash reserve account balance at time \(t\) | SPV liquidity support |
| \(PD_{\mathbb P}\) | Real-world probability of default | Underwriting, ECL, and stress input |
| \(PD_{\mathbb Q}\) | Risk-neutral probability, if separately calibrated | Optional valuation input only |

The letter \(K\) is not reused for regulatory capital, note margins, expected loss, or customer price. This avoids a major source of formula and implementation ambiguity.

# Rate and Cash-Flow Taxonomy

| Rate or amount | Payer | Recipient | Applies to | Calculation owner |
|---|---|---|---|---|
| KESONIA fixing | Reference only | Reference only | Variable-rate benchmark | Official source and calculation agent |
| Customer lending rate | Driver or borrower | Legal lender or receivable owner | Loan or premium-finance balance | Lender pricing policy |
| Fees and charges | Driver or borrower | Contractually entitled entity | Defined service or transaction | Product and finance |
| Asset cash yield | Receivable pool | SPV | Interest, finance charge, and permitted fee cash | SPV model |
| Class A coupon | SPV | Class A noteholders | Class A outstanding principal | Calculation agent |
| Class B coupon | SPV | Class B noteholders | Class B outstanding principal | Calculation agent |
| Servicing fee | SPV | Servicer | Collections or receivable balance as contracted | Servicing agreement |
| Hedge cost | SPV or funding party | Hedge counterparty | Only an executed hedge | Treasury |
| FTP charge | Internal business unit | Internal treasury | Internal performance allocation | Institution-specific ALM policy |
| Discount or hurdle rate | Valuation user | Not a contractual cash flow | NPV, bid, or investment decision | Finance or investor |

The deterministic model must trace every reported margin to actual cash inflows and outflows. A weighted average cost of capital is not itself a debt-service payment.

# Customer Pricing under the CBK Framework

As of 24 August 2026, the revised CBK model states that it took effect on 1 September 2025 for new variable-rate loans and on 28 February 2026 for existing variable-rate loans after the transition period. Product counsel and the licensed lender must still confirm scope, later amendments, and the treatment of any fixed-rate, exempt, restructured, or legacy contract.

For a new variable-rate customer facility within the scope of the revised CBK risk-based credit-pricing model, the controlled representation is:

$$
R_{\mathrm{customer},t}=\mathrm{KESONIA}_t+K_{\mathrm{RBCP},t}.
$$

The total cost of credit additionally reflects disclosed fees and charges:

$$
TCC_t=\mathrm{KESONIA}_t+K_{\mathrm{RBCP},t}+\sum_j f_{j,t},
$$

where the second expression is a conceptual rate-and-charge decomposition, not a substitute for the legally required customer disclosure method.

The revised CBK model describes \(K_{\mathrm{RBCP}}\) as incorporating lending-related costs, the bank's return to shareholders, and the borrower's risk profile. The programme may use validated model outputs within the borrower-risk component, but a posterior PD is not the whole premium.

A controlled internal decomposition can be:

$$
K_{\mathrm{RBCP},i}
=
k_{\mathrm{funding}}
+k_{\mathrm{liquidity}}
+k_{\mathrm{operating}}
+k_{\mathrm{expected\ loss},i}
+k_{\mathrm{capital}}
+k_{\mathrm{profit}}
+k_{\mathrm{other}},
$$

subject to lender approval and the official framework. Components must not be double counted. For example, if servicing cost is included in operating cost, it cannot also appear as an unexplained borrower-risk uplift.

The HLR supplies calibrated \(PD_{\mathbb P}\), credible intervals, and approved segment information. Expected loss for a horizon can be represented as:

$$
EL_i=PD_{\mathbb P,i}\times LGD_i\times EAD_i,
$$

with consistent units and horizon. Converting \(EL_i\) to an annualised premium requires a cash-flow calculation that recognises amortisation, timing, recovery, costs, and target return. It is not achieved by adding a lifetime default percentage directly to an annual rate.

The Credit Policy and Compliance Gate can cap, reject, or refer a proposed price based on affordability, product limits, legal requirements, data quality, uncertainty, and customer-treatment policy.

# KESONIA Compounding Specification

## Contract conventions

The executed contract and calculation-agent procedure must define:

- source and publication time;
- Kenya business-day calendar;
- observation period and interest period;
- lookback, observation shift, lockout, or payment delay;
- day-count denominator;
- treatment of weekends and holidays;
- rounding at fixing, factor, rate, and cash levels;
- negative or missing fixing treatment;
- corrections and republications;
- temporary non-publication procedure;
- permanent cessation and fallback;
- margin application;
- compounding floor, if any; and
- notice and dispute procedure.

No code default becomes a contract term.

## Compounded factor

For \(n\) applicable daily fixings, the unannualised compounded KESONIA factor is:

$$
F_{\mathrm{KESONIA}}
=
\prod_{i=1}^{n}
\left(1+r_i\frac{d_i}{D}\right)-1.
$$

If annualisation is required for disclosure or reporting:

$$
R_{\mathrm{annualised}}
=
F_{\mathrm{KESONIA}}\frac{D}{\sum_{i=1}^{n}d_i}.
$$

Where the note margin is non-compounded and accrues simply:

$$
F_{\mathrm{coupon}}
=
F_{\mathrm{KESONIA}}
+m\frac{\sum_i d_i}{D}.
$$

Interest cash for opening principal \(N\), absent intraperiod principal changes, is:

$$
I=N\times F_{\mathrm{coupon}}.
$$

If principal changes during the period, the engine must partition exposure by effective date or use a daily accrual ledger. The calculation agent cannot apply the closing principal to the whole period.

## Safe computational method

Products over many observations may be computed as:

$$
F_{\mathrm{KESONIA}}
=
\exp\left[
\sum_{i=1}^{n}\log\left(1+r_i d_i/D\right)
\right]-1.
$$

Production logic should use numerically stable log-one-plus and exponential-minus-one equivalents where available. Before calculating, it must validate:

- one applicable fixing for each calendar-day span;
- no overlapping or missing spans;
- \(d_i>0\);
- valid units, such as decimal rather than percentage;
- \(1+r_i d_i/D>0\);
- approved fallback use; and
- source hash and calendar version.

An illustrative SQL pattern is:

~~~sql
SELECT
    contract_id,
    interest_period_id,
    EXP(SUM(LN(1.0 + rate_decimal * calendar_days / day_count_denominator))) - 1.0
        AS kesonia_factor
FROM validated_daily_observations
GROUP BY contract_id, interest_period_id;
~~~

This is a calculation pattern, not deployable production SQL. The implementation must include database-specific functions, precision, calendars, late corrections, tests, access controls, and independent calculation.

# SPV Capital Structure

The primary illustrative capitalisation is:

| Class | USD-equivalent amount | Percentage | Economic role |
|---|---:|---:|---|
| Class A senior notes | 6.75 million | 75 percent | Senior debt |
| Class B mezzanine notes | 1.35 million | 15 percent | Subordinated debt |
| Class C first-loss equity | 0.90 million | 10 percent | Residual and first-loss capital |
| Total SPV capital | 9.00 million | 100 percent | Primary transaction |

An optional HoldCo facility of USD 1 million is outside the SPV waterfall. Together they form a consolidated USD 10 million funding view, not a single commingled liability.

## Note pricing

The canonical Class A coupon is:

$$
R_{A,t}=\mathrm{Compounded\ KESONIA}_t+m_A.
$$

The Class B coupon is:

$$
R_{B,t}=\mathrm{Compounded\ KESONIA}_t+m_B,
$$

or an explicitly agreed fixed rate. Margins, floors, step-ups, payment dates, day count, and fallback remain negotiable. A 91-day Treasury-bill yield can appear as a comparison benchmark, but it is not the default contractual rate in the canonical model.

## Advance rate and overcollateralisation

Advance rate and OC answer different questions. If total SPV capital of USD 9 million corresponds to a 75 percent advance rate, the illustrative eligible-receivable requirement is:

$$
\mathrm{Eligible\ Receivables}_0
=
\frac{9.00}{0.75}
=12.00\ \mathrm{million\ USD\ equivalent}.
$$

Debt-note OC is:

$$
OC_t
=
\frac{\mathrm{Eligible\ Receivables}_t}
{\mathrm{Class\ A}_t+\mathrm{Class\ B}_t}.
$$

At inception, using USD-equivalent amounts:

$$
OC_0
=
\frac{12.00}{6.75+1.35}
=148.15\%.
$$

The contractual minimum is 125 percent. The finance documents must define eligible balance, haircuts, delinquency exclusions, dilution, concentration excess, accrued interest, FX translation, and timing. This ratio does not guarantee principal repayment.

# Product-Cohort Asset Model

The model uses 36 monthly periods and separate origination cohorts for:

- insurance-premium finance;
- microloans; and
- revolving credit.

For product \(p\), cohort \(c\), and month \(t\):

$$
B_{p,c,t}^{\mathrm{close}}
=
B_{p,c,t}^{\mathrm{open}}
+O_{p,c,t}
+D_{p,c,t}
-P_{p,c,t}
-PP_{p,c,t}
-WO_{p,c,t}
+A_{p,c,t},
$$

where \(O\) is origination, \(D\) is an additional revolving draw, \(P\) is scheduled or collected principal, \(PP\) is prepayment, \(WO\) is write-off, and \(A\) is an approved adjustment. Each term is used only where relevant to the product.

Cash interest must follow the contract rate, balance timing, non-accrual policy, and actual collection. Defaults and recoveries are separate events:

$$
\mathrm{Net\ Credit\ Loss}_{p,c,t}
=
\mathrm{Defaulted\ Principal}_{p,c,t}
-\mathrm{Cash\ Recoveries}_{p,c,t}.
$$

The model does not apply one portfolio loss rate to every cohort regardless of age. It uses product-specific default timing, cure, prepayment, recovery haircut, and recovery lag.

IPF recoveries from cancellation or unearned premium are modelled as contractual receivables subject to insurer confirmation, administrative costs, timing, and assignment rights. They are not assumed to be immediately liquid.

# SPV Cash Flow and Waterfall

Available funds include only cash actually received in controlled SPV accounts, subject to the finance-document definition:

$$
\mathrm{Available\ Funds}_t
=
\mathrm{Opening\ Cash}_t
+\mathrm{Principal\ Collections}_t
+\mathrm{Interest\ and\ Fee\ Collections}_t
+\mathrm{Recoveries}_t
+\mathrm{Permitted\ Reserve\ Releases}_t
+\mathrm{Other\ Permitted\ Receipts}_t.
$$

The proposed priority of payments is:

1. taxes and statutory costs properly payable by the SPV;
2. trustee, bank, calculation-agent, and capped senior expenses;
3. servicing fee and approved servicing advances;
4. Class A interest;
5. Class A scheduled or required principal;
6. Class B interest, subject to deferral terms;
7. Class B principal;
8. cash reserve account replenishment;
9. additional senior or Class B sweep required by a trigger;
10. permitted subordinated amounts; and
11. Class C residual distribution.

The exact order must be harmonised with the term sheet and executed documents. Equity distribution is blocked if senior interest or principal is unpaid, OC or reserve is below target, early amortisation is active, a cure is outstanding, or another distribution stopper applies.

## Cash reserve account

The base reserve target is three months of defined Class A and Class B debt service:

$$
CRA_t^{\mathrm{target}}
=
3\times
\mathrm{Monthly\ Defined\ Debt\ Service}_t.
$$

The model separately reports opening reserve, required reserve, deposits, releases, investment income, eligible balance, shortfall, cure, and closing reserve. Reserve cash is liquidity support, not an offset to expected loss unless documents and accounting establish that treatment.

# Return and Coverage Metrics

Metrics are computed from actual modeled cash flows:

- Class A and Class B yield or IRR;
- Class C money multiple and IRR;
- weighted average asset yield;
- net interest margin after servicing, losses, hedge, and operating costs;
- debt-service coverage ratio;
- interest coverage;
- minimum cash;
- reserve coverage;
- OC headroom;
- cumulative loss by class;
- weighted average life; and
- early-amortisation month.

A monthly DSCR is:

$$
DSCR_t
=
\frac{\mathrm{Cash\ Available\ for\ Debt\ Service}_t}
{\mathrm{Class\ A\ and\ B\ Debt\ Service\ Due}_t}.
$$

The numerator and denominator must be defined once and used consistently. Cash swept to principal cannot also be counted as ending cash or equity distribution.

WACC can be used as a valuation or investment hurdle:

$$
WACC
=
w_A r_A(1-\tau_A)
+w_B r_B(1-\tau_B)
+w_C r_C,
$$

only if the tax effects, weights, and required returns are supportable. It is not injected into the waterfall as a fictional expense, and it does not replace class-specific return calculations.

# Fees, Taxes, Costs, and FX

The model contains explicit assumption rows for:

- origination, administration, late, platform, and servicing fees;
- excise duty, VAT, withholding tax, income tax, stamp duty, and other possible taxes;
- legal, trustee, audit, bank, data, model, and insurance-administration costs;
- hedge premium, basis, collateral, settlement, and counterparty charges; and
- expected tax deductibility.

Each row is labelled confirmed, legal opinion pending, commercial quote pending, illustrative, or not applicable. No 3 percent origination fee, 20 percent excise rate, 30 percent tax rate, or hedge cost is treated as settled without current Kenyan tax advice and executed commercial terms.

If USD reporting is required:

$$
\mathrm{USD\ Equivalent}_t
=
\frac{\mathrm{KES\ Amount}_t}{FX_{\mathrm{KES/USD},t}}.
$$

Translation does not create cash. FX gains and losses, hedge cash flows, and covenant conversion rules are separately modelled when relevant.

# IFRS 9 Interfaces

## Effective interest rate

At initial recognition, the approved effective interest rate discounts estimated contractual cash flows, including relevant integral fees and transaction costs, to the instrument's initial carrying amount. The accounting model must not reset the EIR merely because an internal pilot phase changes.

For a floating-rate instrument, periodic re-estimation of cash flows to reflect movements in the market rate is treated according to the instrument's terms and IFRS 9 policy. The compounding engine provides contract cash flows; accounting determines interest recognition.

## Modification and derecognition

When terms change, accounting evaluates contractual authority, financial difficulty, qualitative changes, and applicable quantitative evidence. If the asset is modified without derecognition, the reporting entity applies its approved IFRS 9 method, including any required recalculation using the appropriate original effective rate and recognition of a modification gain or loss. If derecognition occurs, the old asset and new asset are accounted for accordingly.

The system keeps distinct:

- ordinary KESONIA rate reset under original terms;
- exercise of an existing contractual option;
- administrative correction;
- non-derecognising modification;
- derecognition and new asset;
- forbearance due to financial difficulty; and
- write-off.

The liability modification analysis for SPV notes is separate from the asset analysis.

# IFRS 17, Prudential Capital, and SPV Protection

IFRS 17 applies to the insurer's insurance contracts within scope. It does not measure the lender's premium-finance receivable or the SPV notes. The insurer owns the IFRS 17 methodology and supplies contractually agreed premium, cancellation, refund, and claims information.

Regulatory capital belongs to each regulated institution's prudential calculation. SPV subordination, OC, reserves, and cash sweeps are transaction protections. They do not automatically reduce a lender's risk-weighted assets or insurer capital requirement.

Investor-protection claims are conditional:

- Class A principal loss is a model result under specified scenarios;
- first-loss equity absorbs losses only to the extent actually funded and available;
- recoveries depend on enforceable rights and timing;
- cash reserves can be depleted;
- early amortisation can reduce but not eliminate risk; and
- model uncertainty and operational failure remain relevant.

# FTP, Valuation, and Interest-Rate Stress

Matched-maturity funds transfer pricing is optional and institution-specific. It may allocate a reference funding curve, liquidity premium, optionality, basis, capital, and overhead to a product, but it is not a customer invoice or SPV waterfall item unless contractually charged.

The implementation must not use Microsoft application-lifecycle documentation as evidence for asset-liability management. A specialist treasury or ALM capability may be selected after fit-gap review.

Real-world \(PD_{\mathbb P}\) is used for forecasting and expected loss. A risk-neutral \(PD_{\mathbb Q}\) is used only for market-consistent valuation when it is calibrated to suitable market prices under an approved methodology. An arbitrary drift adjustment is not sufficient.

Interest-rate stress for the SPV includes:

- parallel and nonparallel KESONIA shifts;
- delayed customer reset relative to note reset;
- floors and caps;
- basis between asset and liability conventions;
- prepayment and utilisation response;
- collection delay;
- reserve investment yield; and
- hedge performance and collateral.

The term "IRRBB" is reserved for a bank's regulatory interest-rate-risk-in-the-banking-book framework. The SPV can measure earnings and economic-value sensitivity without representing itself as a bank.

# Deterministic Scenarios

The controlled scenario set is:

| Scenario | IPF default | Microloan default | Revolver default | Recovery and timing | Policy response |
|---|---:|---:|---:|---|---|
| Base | 3.2 percent | 4.5 percent | Explicit assumption | Base recovery, lag, and prepayment | Normal eligibility |
| Mild shock | 6.8 percent | 9.1 percent | Increased assumption | Lower or slower recovery | Tighter limits and purchases |
| Severe contagion | 14.5 percent | 22.0 percent | Severe assumption | Tail recovery delay | Early amortisation if trigger met |
| User case | User input | User input | User input | User input | Formula-driven |

These are illustrative until supported by a portfolio tape. The model must state whether a percentage is monthly, annual, vintage cumulative, lifetime, or point-in-time.

Sensitivity grids include:

- default versus recovery;
- KESONIA versus customer repricing lag;
- advance rate versus OC;
- Class B margin versus servicing cost;
- origination ramp versus NPL;
- collection lag versus minimum cash;
- reserve months versus debt survival; and
- FX versus reported DSCR where an FX obligation exists.

# Monte Carlo Extension

Simulation extends the same cohort schedules and waterfall used in the deterministic model. It does not replace them with a simplified loss shortcut.

For each path:

1. draw macroeconomic and platform states;
2. generate calibrated product and cohort marginal defaults;
3. draw dependent uniform variables from an approved copula;
4. set default when the dependent draw falls below the relevant marginal PD;
5. simulate EAD, prepayment, utilisation, cure, recovery amount, and recovery lag;
6. simulate KESONIA and any basis or FX factor under a documented real-world process;
7. run exact contractual eligibility, reserve, waterfall, and trigger logic;
8. store class cash flows, principal loss, interest shortfall, WAL, DSCR, OC, reserve, and trigger month; and
9. reconcile each path's cash and balances.

Clayton, survival Clayton, Gumbel, Student-t, Gaussian, or a vine structure are candidates. Family and parameters are selected through data fit, tail diagnostics, out-of-time validation, and stress plausibility. A dependence parameter is not inferred from an asset-level default rate.

Simulation controls include fixed and random seeds, convergence diagnostics, parameter-uncertainty runs, independent code review, deterministic edge cases, and reproduction from a locked manifest. Outputs show distributions and confidence ranges, not only a favourable percentile.

# Model Governance and Publication Controls

The finance model must contain:

- assumption owner, source, as-of date, unit, and status;
- source, derived, illustrative, stress, and output labels;
- formula version and release hash;
- no external workbook links;
- no hidden constants in code;
- conventional formulas without implicit-intersection at-sign syntax;
- cash, receivable, debt, reserve, and waterfall checks;
- scenario and sensitivity propagation tests;
- independent model review; and
- a source and change log.

The project may state that a class suffers no principal loss in a named scenario only after the locked model calculates that result. The statement must identify scenario, horizon, assumptions, version, and limitations.

# Acceptance Criteria

This pricing and capital design is accepted only when:

- customer price, fees, SPV coupons, FTP, WACC, and regulatory capital are distinct;
- \(K_{\mathrm{RBCP}}\), \(K_{\mathrm{cap}}\), \(m_A\), \(m_B\), \(EL\), \(OpEx\), and \(CoC\) are not conflated;
- KESONIA compounding matches executed conventions and an independent calculator;
- missing, corrected, weekend, holiday, and cessation cases pass;
- the 9 million capital stack and optional 1 million HoldCo overlay reconcile;
- advance-rate and OC denominators are explicit;
- all KES cash flows reconcile before any USD translation;
- product cohorts roll forward;
- available cash is allocated once through the waterfall;
- note balances, reserve, OC, and debt service roll forward;
- tax, fees, costs, and hedging are source-labelled;
- IFRS 9 rate reset, modification, derecognition, and ECL are separate;
- IFRS 17 remains with the insurer;
- lender prudential capital is not claimed as an SPV benefit;
- deterministic and simulation models share contractual logic;
- every path and scenario balances; and
- investor-protection language is conditional on calculated results.

# References

1. Central Bank of Kenya, "Revised Risk-Based Credit Pricing Model," Aug. 2025. Available: https://www.centralbank.go.ke/wp-content/uploads/2025/08/Revised-Risk-based-Credit-Pricing-Model.pdf
2. Central Bank of Kenya, "Issuance of a Revised Risk-Based Credit Pricing Model," Aug. 2025. Available: https://www.centralbank.go.ke/uploads/press_releases/2044081907_Press%20Release%20-%20Issuance%20of%20a%20Revised%20Risk-Based%20Credit%20Pricing%20Model.pdf
3. Central Bank of Kenya, "Kenya Shilling Overnight Interbank Average." Available: https://www.centralbank.go.ke/
4. IFRS Foundation, "IFRS 9 Financial Instruments." Available: https://www.ifrs.org/issued-standards/list-of-standards/ifrs-9-financial-instruments/
5. IFRS Foundation, "IFRS 17 Insurance Contracts." Available: https://www.ifrs.org/issued-standards/list-of-standards/ifrs-17-insurance-contracts/
6. Basel Committee on Banking Supervision, "The Basel Framework." Available: https://www.bis.org/baselframework/
