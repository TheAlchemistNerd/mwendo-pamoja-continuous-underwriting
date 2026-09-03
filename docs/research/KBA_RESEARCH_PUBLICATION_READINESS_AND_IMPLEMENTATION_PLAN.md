# KBA Research Publication Readiness and Implementation Plan

**Prepared:** 2 September 2026  
**Primary opportunity:** Kenya Bankers Association Research Centre  
**Proposed research programme:** KESONIA, lifecycle underwriting, collectability, MSME credit quality, and non-performing-loan management in Kenya

**Implementation status:** Phase 1 and the canonical elements of Phase 2 have begun. The editorial enquiry, one-page concept note, five-page proposal, canonical research specification, source extraction ledger, data dictionary, source-hash baseline, and first Economic Bulletin draft are maintained in `publications/submissions/kba-lifecycle-credit/`. Phase 3 has also begun with a reproducible 2 September 2026 snapshot of CBK KESONIA, the KESONIA compounded index, commercial-bank weighted average rates, and the June 2026 KBA MSME loan-performance tables.

## 1. Executive verdict

The existing body of work contains enough original thinking, technical architecture, Kenyan market context, and policy relevance to support a strong Kenya Bankers Association research programme. It is not yet ready to be submitted unchanged as a conference research paper or KBA Working Paper. The principal gap is not conceptual depth. It is the conversion of several rich manuscripts into one disciplined research contribution with a defined question, testable hypotheses, a documented dataset, an empirical identification strategy, reproducible results, and implementable recommendations for Kenyan banks.

The strongest paper to develop is:

> **From KESONIA to Sustainable Collection: Risk-Based Pricing, MSME Credit Quality and Lifecycle Underwriting in Kenya**

An alternative, more practitioner-oriented title is:

> **Underwrite for Collection under KESONIA: A Lifecycle Framework for MSME Credit Pricing and NPL Management in Kenya**

The first title is better aligned with the 2026 KBA conference theme, “Banking Amidst Macroeconomic Policy Reforms: Emerging Risks and Opportunities.” It joins two timely questions that the current manuscripts already explore from different directions:

1. How Kenya’s revised risk-based credit-pricing framework and KESONIA benchmark are transmitted into bank and product pricing.
2. How lending institutions can design origination, monitoring, intervention, restructuring, collection, provisioning, capital, and funding as one credit lifecycle rather than as disconnected functions.

The paper should not be a shortened version of the entire Mwendo Pamoja white paper. It should be a new, independent research manuscript that draws selectively from the best parts of the existing work. The central banking contribution is that a benchmark reform becomes economically meaningful only when the lender connects the price of credit to the subsequent cash performance of the exposure. That includes payment timing, cure, modification, prepayment, delinquency migration, recovery cost, net recovery, expected credit loss, capital consumption, and funding economics.

The immediate 2026 conference route is largely closed. The official KBA call set 17 April 2026 as the proposal deadline, 15 May as the notification date, 30 June as the full-paper and policy-brief deadline, and August as the technical-review workshop. The conference is scheduled for 17 and 18 September 2026 in Nairobi. As of 2 September 2026, an unsolicited full paper should not be presented as an ordinary on-time conference submission. The appropriate immediate step is an editorial enquiry to `research@kba.co.ke` asking whether the Research Centre would consider one of four routes:

- A late methodological-session contribution, if the programme still has capacity.
- An off-cycle KBA Working Paper submission.
- A shorter contribution to the Kenya Bankers Economic Bulletin.
- Registration of the proposal for the next annual research-conference cycle.

The official call does not promise a rolling working-paper submission process or late acceptance. It says selected conference papers will be reviewed for possible publication in the KBA Working Paper Series. The enquiry should therefore ask for direction rather than assume an available route.

The current material is highly ready for a five-page research proposal and moderately ready for a policy or practitioner article. It is not yet empirically ready for a competitive full research paper. With a bank, credit-reference-bureau, fintech, digital-credit-provider, or anonymised loan-servicing dataset, it could become a strong empirical paper. Without such a partner, a carefully labelled public-data study combined with a reproducible synthetic lifecycle experiment can support a methodological contribution, but it must not be represented as evidence of borrower behaviour or causal intervention effects in Kenya.

“Underwrite for Collection” will therefore be handled through two deliberate routes. It is suitable, after a focused KESONIA and house-style adaptation, as a Kenya Bankers Economic Bulletin or comparable practitioner contribution. It will also supply the narrative motivation and policy implications for the research programme. It will not be submitted unchanged as though it were an empirical conference or Working Paper manuscript because those genres require an explicit dataset, estimation method, results, and robustness analysis.

## 2. What the official KBA call actually requires

The official [KBA 2026 Call for Papers](https://www.kba.co.ke/wp-content/uploads/2026/03/KBA-Call-for-Papers-2026-Advert-3.pdf) confirms that the 15th Annual Banking Research Conference will be held in Nairobi on 17 and 18 September 2026. It is intended to convene researchers, policymakers, and industry stakeholders around implementable policy recommendations. It also states that the conference will be hybrid, while authors of selected papers must present in person.

The call has three substantive subthemes and one methodological track:

1. Fiscal-policy reforms, including public-debt thresholds, taxation, fiscal consolidation, and the balance between domestic and external borrowing.
2. Monetary policy and bank credit-pricing dynamics, including the optimal Central Bank Rate, the transition to risk-based pricing, credit growth, financial stability, competition, digitisation, access to credit, sectoral lending, NPL-management schemes, and credit de-risking.
3. Risk identification and management, including the identification and measurement of emerging risks, bank and economic resilience, and transition pathways.
4. A methodological session focused on innovative and practical solutions to prevailing industry challenges.

The proposed KESONIA and lifecycle-underwriting paper fits the second subtheme directly. It also fits the methodological session if it includes a reproducible credit-lifecycle model and a practical implementation design. A broader version can contribute to the third subtheme by studying transition risk from benchmark repricing, borrower cash-flow pressure, concentration, collection deterioration, and portfolio resilience.

The formal first-stage requirement was not a completed paper. It was a maximum five-page proposal emailed to `research@kba.co.ke`, containing a 300 to 500-word abstract, a clear motivation, key hypotheses, and a brief methodology. This matters because the current manuscripts are much more detailed than the requested proposal. The first task is synthesis, not expansion.

The AI-generated conversation supplied with this assignment is directionally helpful but should not be treated as submission authority. It correctly identified the Research Centre’s email address and the conference’s broad purpose. Its template, however, suggests sending a final manuscript as though a standing submission window exists. The official call provides a staged and dated process. Our engagement will follow the official document and seek explicit editorial guidance for any post-deadline route.

## 3. Review of the manuscript estate

### 3.1 Underwrite for Collection

`UNDERWRITE_FOR_COLLECTION.md` is the best narrative foundation. It already expresses the paper’s most valuable industry proposition:

> A loan is successfully underwritten only when its structure, monitoring, and intervention design support sustainable collection after disbursement.

The article contributes a coherent lifecycle argument. It distinguishes a flow of new MSME lending from the stock of sector-wide NPLs; connects origination to event-time ledgers and post-disbursement monitoring; separates default probability, timing, exposure, cure, and recovery; and treats policy interventions as decisions that must be governed and evaluated. It also links realised cash outcomes to IFRS 9, economic capital, funding, and ring-fenced financing structures.

Its present strengths are accessibility, industry relevance, human-centred motivation, and a practical sequence of change. Its limitations for formal research are equally clear. It has no 300 to 500-word research abstract, formal hypotheses, described sample, estimation protocol, empirical results, identification strategy, or reproducibility package. The modelling discussion accelerates from industry narrative to advanced statistical architecture without an empirical bridge. The article should supply the motivation, conceptual framework, policy implications, and practitioner explanation for the KBA paper, not serve as the submitted research manuscript by itself.

It is also suitable for a shorter, timely Kenya Bankers Economic Bulletin article. That version could focus on the distinction between disbursement success and collection success, explain how KESONIA and risk-based pricing alter the economics of the loan after origination, and propose a lifecycle scorecard. It would need only carefully dated data, a limited number of charts, and a concise policy conclusion. The Bulletin route should be discussed with the editor because public submission length and house-style requirements are not stated in the conference call.

### 3.2 The KESONIA research series

The four KESONIA manuscripts provide the technical spine:

- Reform and enterprise architecture.
- Daily compounding and accrual mechanics.
- AI pricing and IFRS 9.
- RegTech, ERP, audit, and implementation controls.

Together they cover benchmark data, daily accruals, product pricing, funds-transfer pricing, asset-liability management, expected credit loss, event lineage, reconciliations, systems of record, and operational governance. They are particularly valuable because a KBA audience will expect the paper to connect policy reform to how banks price, account for, govern, and monitor credit.

They require a controlled technical correction before any material is reused. The revised risk-based credit-pricing model did not give way to KESONIA. KESONIA is the reference benchmark inside the revised framework. The public formula is:

```text
Total lending rate = KESONIA + K_RBCP
Total cost of credit = KESONIA + K_RBCP + fees and charges
```

The Central Bank of Kenya’s [Revised Risk-Based Credit Pricing Model](https://www.centralbank.go.ke/wp-content/uploads/2025/08/Revised-Risk-based-Credit-Pricing-Model.pdf) describes the bank-specific premium as including lending-related operating costs, shareholder return, and the borrower’s risk profile. The manuscripts sometimes compress that premium into a PD, LGD, and EAD expression. Those variables can inform the borrower-risk component, expected loss, economic capital, and pricing governance, but they do not exhaust the official definition of the premium.

The new research paper must keep the following quantities distinct:

- The applicable benchmark, normally KESONIA and, where permitted, CBR.
- The bank-specific or product-specific risk-based credit-pricing premium.
- Fees and charges that determine total cost of credit.
- Contractual compounding and accrual mechanics.
- Expected loss.
- Allocated operating cost.
- Liquidity and matched-funding cost.
- Economic-capital charge.
- Shareholder return or profit contribution.
- SPV note margin or investor required return, if structured finance is discussed.

The official [CBK KESONIA page](https://www.centralbank.go.ke/kesonia/) confirms that KESONIA is a transaction-based, volume-weighted overnight unsecured interbank rate administered by CBK. Publication of KESONIA and its compounded index began on 1 September 2025. The revised pricing framework applied to new variable-rate loans from that date and to existing variable-rate loans from 28 February 2026. This creates two policy dates for empirical design, but it does not create a clean natural experiment automatically. The post-reform period is still short, macroeconomic conditions changed concurrently, bank adoption and product repricing may differ, and public pricing records may be incomplete.

Claims in the existing series about mandatory point-in-time AI, automated supervisory APIs, cryptographic regulatory sweeps, or a single ERP regulatory source of truth must be reframed as proposed design patterns unless supported by an official interface or requirement. The empirical paper should separate what the regulation requires, what a credit contract specifies, what a bank’s internal policy chooses, and what the proposed architecture recommends.

### 3.3 Mwendo Pamoja Part 2b

The Bayesian-underwriting manuscript supplies a sophisticated modelling library: hierarchical logistic regression, Pólya-Gamma-augmented offline inference, governed P-splines, AR(1) or RW1 time effects, residualised neural representations, regularised horseshoe priors, calibration, credit-state timing, asymmetric dependence, explainability, fairness, and model governance.

Only a subset belongs in the KBA paper’s main body. The primary empirical specification should be interpretable and proportionate to the available data. A hierarchical discrete-time logistic, hazard, or multistate model can pool information across banks, products, sectors, geographies, or borrower cohorts while estimating delinquency, cure, and recovery transitions. P-splines can represent nonlinear cash-flow relationships. Pólya-Gamma augmentation may improve offline inference while preserving hierarchical pooling. These are valuable methodological contributions if the data and diagnostics support them.

The neural and copula components should be challengers or appendices. They should enter the main findings only if they demonstrably improve out-of-time calibration, net-loss prediction, or decision utility. This avoids offering complexity as a substitute for evidence. It also keeps the methodological session practical for banks that need explainable implementation pathways.

The manuscript’s feature-ownership discipline is worth retaining. Explicit borrower and account variables should have one canonical definition and owner. If learned behavioural representations are used, they should be trained out of fold and residualised against explicit variables before shrinkage. That reduces duplicated representation and makes incremental value testable.

### 3.4 Mwendo Pamoja Parts 3 and 5

Part 3 contributes the Credit Policy and Compliance Gate, intervention design, fair-treatment controls, IFRS 9 forbearance distinctions, action logging, and regulatory auditability. These concepts translate directly into a banking lifecycle architecture. The paper should distinguish prediction from policy and action:

```text
Observed information -> estimated risk -> policy constraints -> authorised action -> measured outcome
```

Part 5 is the strongest source for pricing and funding discipline. It distinguishes physical-measure PD from market-consistent valuation, customer pricing from note pricing, expected loss from capital, and bank ALM from the cash waterfall of a ring-fenced financing vehicle. It can support a concise section on how collection performance reaches finance through ECL, capital, liquidity, FTP, and, where applicable, structured-finance eligibility and covenants.

Project-specific facility amounts, tranche sizes, and claims about the Mwendo Pamoja asset pool should not be imported into a general KBA paper. Structured finance should be presented as one credit de-risking mechanism, not the universal endpoint of MSME lending. The useful transferable idea is that receivable value is determined by verifiable net cash after collection lags, cure, recoveries, workout expense, servicing, and priority of payment.

### 3.5 Other materials

The AIRCE and venture-finance abstract can contribute a paragraph on inclusive finance, ecosystem incentives, and shared value, but its HoldCo and venture narrative is secondary to the banking question.

The telematics actuarial paper should not be blended into the subject matter. Its methodological practices are nevertheless useful: measure exposure explicitly, separate frequency from severity, avoid duplicate features, use hierarchical credibility, validate posterior predictions, distinguish real-world forecasting from valuation, and connect the predictive distribution to reserves, capital, and risk transfer. In the banking paper, the analogues are exposure at default, event frequency and timing, loss severity, cure and recovery, expected credit loss, economic capital, and credit-risk transfer.

## 4. Recommended research question and contribution

The main research question should be:

> How does Kenya’s transition to KESONIA-anchored risk-based credit pricing affect pricing transmission, MSME credit access, and loan collectability, and how can a lifecycle-underwriting framework improve the connection between origination, early intervention, durable cure, and net recovery?

This is broad enough to matter to KBA but must be decomposed into questions that the selected data can answer:

1. How quickly and how completely do changes in the applicable reference rate pass into published bank-product lending rates?
2. How much cross-bank and cross-product dispersion remains in the published premium and total cost of credit?
3. Which lifecycle variables improve prediction of delinquency migration, cure, time to default, and net recovery beyond origination-only information?
4. Which early interventions generate durable cure or higher net recovery rather than merely delaying arrears?
5. How should those results feed pricing, ECL, economic capital, collection strategy, and credit de-risking without producing avoidable exclusion?

The proposed hypotheses are:

- **H1:** Changes in the applicable reference rate transmit into variable lending rates with measurable lags and material heterogeneity across bank-product combinations.
- **H2:** Published credit-pricing premiums remain materially dispersed after accounting for benchmark basis and observable product characteristics, reflecting differences in operating cost, customer risk, business model, and return requirements that require further decomposition rather than a single interpretation.
- **H3:** Properly timed lifecycle indicators add out-of-time information about delinquency, cure, and recovery beyond origination variables.
- **H4:** Targeted early interventions can improve durable cure and net recovery relative to comparable untreated accounts while maintaining fair-treatment and access constraints.

H4 requires intervention and outcome data with a defensible comparison group. If such data cannot be secured, it should become a future research proposition, not an empirical claim.

The original contribution is a lifecycle bridge. Existing discussions of KESONIA can focus on benchmark construction and loan pricing, while NPL discussions can focus on problem assets after deterioration. The proposed paper connects the two through a measurement architecture that follows the account from benchmark and premium setting through disbursement, payment behaviour, intervention, cure, default, recovery, provisioning, capital, and funding. Its methodological contribution is not simply a more complex score. It is a research design in which collectability becomes an observable, testable property of the credit product.

## 5. Data strategy

### 5.1 Public-data layer

The public-data study should build a versioned research dataset containing:

- Daily KESONIA and the official compounded index from CBK.
- CBR dates and values.
- Monthly commercial-bank weighted average lending, deposit, savings, and overdraft rates from the [CBK commercial rates series](https://www.centralbank.go.ke/commercial-banks-weighted-average-rates/).
- Bank-product reference basis, published premium, lending rate, fees, charges, and total cost of credit from the [KBA Total Cost of Credit portal](https://www.costofcredit.co.ke/site/interest-rate).
- MSME credit outstanding, NPL value, NPL accounts, gender, institution, product, and other available dimensions from the [KBA MSME Credit Dashboard](https://msmedata.kba.co.ke/) and its published methodology.
- Credit standards, demand, NPL expectations, recovery intentions, sector outlook, and risk factors from CBK Credit Officer Surveys.
- Inflation, GDP, exchange rates, fiscal indicators, Treasury yields, fuel prices, and relevant sector activity from CBK, KNBS, National Treasury, and other official sources.

Every extraction must retain source URL, retrieval date, publication date, observation date, unit, revision status, and transformation history. A frozen source snapshot should accompany the code where the source licence permits it.

The Total Cost of Credit data requires special care. The published premium is generally a bank-product quantity, not a borrower-level risk premium. Missing or “N/A” entries may be systematic. Update dates may differ across institutions. Products may have different tenors, collateral, customer segments, fees, and benchmark choices. The analysis must not infer borrower discrimination, bank efficiency, or risk quality directly from an aggregate published premium.

The KBA MSME dashboard draws on anonymised credit-reference-bureau data. Its denominators, institution coverage, account definitions, reporting lag, and treatment of restructures must be documented from the methodology. Public aggregate data can establish trends and associations. It cannot identify account-level transitions or causal intervention effects.

### 5.2 Institution-data layer

The ideal partner dataset contains anonymised account-level or well-designed cohort-level information:

- Origination date, product, initial amount, tenor, price, fees, collateral, sector, geography, and borrower segment.
- Benchmark basis, premium, reset dates, payment schedule, and modifications.
- Amount due, amount paid, payment time, days past due, arrears balance, utilisation, and exposure at default.
- Cure, durable cure, restructure, forbearance, prepayment, write-off, recovery amount, recovery date, legal cost, collection cost, and net recovery.
- Approved interventions, contact channel, timing, intensity, eligibility rule, consent basis, and outcome.
- Macroeconomic and product conditions known at each decision time.
- Model score and version, policy version, reason codes, overrides, and decision record.

The data-access proposal should minimise personal data. Direct identifiers should be removed before research access. Quasi-identifiers should be generalised where appropriate. The work should define lawful purpose, access controls, retention, disclosure review, and output aggregation under Kenya’s Data Protection Act and the partner’s governance process.

### 5.3 Synthetic fallback

If no partner dataset becomes available, construct a transparent synthetic portfolio calibrated only to published aggregates and clearly marked assumptions. Its purpose will be to test the mechanics of competing models and intervention policies, not to estimate Kenyan borrower effects. It can demonstrate:

- Payment-event reconstruction.
- Delinquency-state transitions.
- Cure and recovery lags.
- Benchmark repricing.
- ECL and capital propagation.
- Scenario stress.
- Model calibration and decision thresholds.

All synthetic parameters must be listed. Results must be labelled illustrative. No statement should imply validation on actual Kenyan MSME accounts.

## 6. Empirical and modelling design

### 6.1 Pricing transmission

Begin with transparent decomposition:

```text
Published lending rate = applicable reference rate + published K_RBCP
Published total cost of credit = lending rate + disclosed fees and charges
```

Create bank-product panels and measure rate, premium, and total-cost dispersion. Estimate pass-through using changes rather than relying only on levels:

```text
Change in product rate = bank-product effect
                       + benchmark pass-through
                       + change in published premium
                       + macroeconomic and product controls
                       + error
```

The exact specification must respect collinearity. A common daily or monthly benchmark cannot be estimated alongside unrestricted time fixed effects without an interaction or differential exposure design. Possible strategies include benchmark-choice groups, actual repricing dates, product-reset conventions, distributed lags, or bank-specific adoption timing. Each requires validation from the data.

The dates 1 September 2025 and 28 February 2026 can anchor interrupted-time-series or event-study descriptions. They should not be described as causal shocks unless the analysis establishes a credible counterfactual, stable pre-trends, adequate observations, and separation from concurrent monetary and macroeconomic changes.

### 6.2 Lifecycle credit model

Start with a transparent benchmark:

- Origination-only logistic or scorecard model.
- Discrete-time hazard model for first material delinquency or default.
- Multistate transition model for current, early arrears, late arrears, cure, restructure, default, write-off, and recovery.

Then add lifecycle evidence in controlled stages. Candidate variables include payment timing, repayment velocity, utilisation, balance volatility, income or cash-flow stability where lawfully available, days since last full payment, prior cure durability, scheduled-to-actual payment ratio, and intervention history known at the decision time.

Hierarchical effects can pool across product, institution, sector, geography, and origination vintage. Governed P-splines can represent nonlinear effects. AR(1) or RW1 effects can represent time evolution where identified. Pólya-Gamma augmentation can support efficient offline Bayesian inference without replacing the hierarchy. A residualised neural behavioural representation may be tested only after the explicit model is established and only if its incremental out-of-time value is material.

The model must distinguish:

- Probability of delinquency or default.
- Time to deterioration.
- Exposure at the event.
- Probability and timing of cure.
- Gross recovery.
- Collection and workout expense.
- Discounted net recovery.

This supports an economically meaningful objective:

```text
Expected cash loss = probability-weighted exposure loss
                   - discounted net recoveries
                   + collection and workout costs
```

Model development should use vintage and out-of-time splits, not random row splits that leak future account information. Features must be reconstructed point in time. Post-event information and post-intervention variables must not enter an earlier score.

### 6.3 Intervention evaluation

Prediction alone does not show that an intervention works. The paper should define each action, eligible population, decision rule, timing, cost, and outcome. Preferred evidence is a randomised or carefully governed phased rollout. Where randomisation is unavailable, use a defensible quasi-experimental design such as staggered adoption, matched comparison, propensity weighting, doubly robust estimation, or a regression discontinuity around a genuinely enforced threshold.

Measure durable outcomes rather than contact volume:

- Cure within a stated horizon.
- Re-default after cure.
- Net recovery present value.
- Customer hardship or complaint indicators.
- Modification performance.
- Access and approval effects.
- Differential outcomes across protected or vulnerable groups where lawful and appropriate.

### 6.4 Validation

Report discrimination and calibration, but do not stop there. The validation set should include:

- Log loss or deviance.
- Brier score.
- Calibration intercept and slope.
- Observed-to-expected default, cure, and recovery.
- Precision-recall measures for rare events.
- Vintage stability and covariate shift.
- Prediction-interval or posterior-predictive coverage.
- Incremental value over the origination-only model.
- Expected cash-loss error.
- Intervention value net of cost.
- Fair-treatment and access outcomes.
- Sensitivity of ECL and capital to model uncertainty.

## 7. Proposed full-paper structure

The target should be an 8,000 to 11,000-word research paper, adjusted to KBA’s eventual guidance:

1. **Abstract, 300 to 350 words.** State the question, data, method, principal results, contribution, and policy implication.
2. **Kenyan motivation, 800 to 1,000 words.** Explain benchmark reform, MSME credit access, and asset-quality pressure. Keep lending flows and NPL stocks in their correct denominators.
3. **Institutional framework, 800 words.** Explain KESONIA, revised RBCPM, published premium, fees, repricing dates, and credit-lifecycle responsibilities.
4. **Literature and policy context, 900 to 1,100 words.** Cover monetary-policy pass-through, risk-based pricing, relationship and behavioural information, delinquency transitions, cure, recovery, ECL, and de-risking.
5. **Research questions and hypotheses, 300 to 500 words.** State only claims that the data can test.
6. **Data, 900 to 1,200 words.** Describe public and partner sources, coverage, construction, missingness, ethics, and limitations.
7. **Method, 1,200 to 1,600 words.** Present pricing pass-through, lifecycle transitions, hierarchy, intervention identification, and robustness. Move detailed computation to appendices.
8. **Results, 1,200 to 1,600 words.** Report economically interpretable effects, uncertainty, and diagnostics.
9. **Banking implications, 700 to 900 words.** Translate results into pricing, collections, IFRS 9, capital, FTP, product design, and fair treatment.
10. **Policy recommendations, 500 to 700 words.** Propose implementable measures for banks, KBA, CBK, data partners, and industry utilities.
11. **Limitations and research agenda, 300 to 500 words.** State data and identification boundaries constructively.
12. **Conclusion, 300 to 400 words.** Return to the collectability thesis.
13. **Technical appendices.** Include compounding, P-splines, Pólya-Gamma inference, transition equations, robustness tests, data dictionary, and synthetic assumptions where relevant.

The main body should tell a banking story. Equations must serve that story. Advanced methods should appear when they change an inference or decision, not merely because they are available in the manuscript estate.

## 8. Five-page proposal to prepare first

Prepare the formal proposal even though the deadline has passed. It becomes the attachment for an editorial enquiry and the starting document for the next cycle.

**Page 1:** Title, 300 to 500-word abstract, keywords, author, affiliation, email, and a concise statement of contribution.

**Page 2:** Motivation and Kenyan institutional setting, including the revised RBCPM, KESONIA adoption dates, MSME credit context, and why collection outcomes belong in pricing and risk design.

**Page 3:** Research questions and three or four hypotheses. Distinguish questions answerable with public data from questions requiring institution data.

**Page 4:** Data and methodology, including pricing-transmission analysis, lifecycle transition model, intervention identification, and validation.

**Page 5:** Expected outputs, implementable policy value, data requirements, ethics, limitations, timeline, and selected references.

The abstract should not promise empirical findings before the dataset is built. If the enquiry is made before partner data is secured, use language such as “the study will estimate” and specify the public-data component already available.

## 9. Implementation work programme

### Phase 1: Editorial enquiry and route confirmation, 2 to 5 working days

- Send a concise enquiry to the KBA Research Centre.
- State that the 2026 deadlines are understood to have passed.
- Provide the proposed title, question, relevance to the monetary-policy and credit-pricing subtheme, and current stage.
- Ask about the late methodological session, off-cycle Working Paper Series, Economic Bulletin, and next conference cycle.
- Offer the five-page proposal; do not attach the entire white-paper collection.
- Attend or register for the September conference if appropriate, using it to refine the research question and identify potential data collaborators.

Suggested subject:

```text
Research enquiry: KESONIA, MSME credit quality and lifecycle underwriting
```

### Phase 2: Canonical research specification, 1 week

- Freeze the research question, hypotheses, estimands, outcomes, and target audience.
- Create a source-to-paper extraction ledger for every reused paragraph, equation, diagram, and citation.
- Adopt the official KESONIA and RBCPM terminology.
- Separate regulatory requirements, contractual mechanics, bank policy, and proposed architecture.
- Define the data dictionary and point-in-time rules.
- Write the five-page proposal.

### Phase 3: Public dataset and descriptive study, 2 to 4 weeks

- Download and validate official CBK, KBA, KNBS, and Treasury data.
- Archive dated source snapshots and metadata.
- Construct KESONIA, CBR, bank-product pricing, total-cost, market-rate, and MSME-credit panels.
- Reconcile frequency, dates, units, benchmark basis, and missing values.
- Produce descriptive charts for benchmark transmission, premium dispersion, rate dispersion, credit growth, and asset quality.
- Document what the public data can and cannot identify.

### Phase 4: Partner-data acquisition, 3 to 10 weeks in parallel

- Prepare a two-page data-partnership note for banks, fintechs, DCPs, CRBs, and industry bodies.
- Specify minimum viable fields and preferred account-level fields.
- Establish data protection, confidentiality, output review, and publication terms.
- Obtain an anonymised sample or a secure analytical environment.
- Decide whether the intervention analysis is experimental, quasi-experimental, or descriptive.

### Phase 5: Empirical modelling, 3 to 6 weeks

- Estimate transparent pricing-transmission models.
- Build origination-only benchmark models.
- Build lifecycle transition and recovery models.
- Add hierarchy and nonlinearities incrementally.
- Evaluate optional neural representations only against the approved explicit baseline.
- Test calibration, temporal stability, fairness, net recovery, ECL, and capital consequences.
- Complete sensitivity and robustness analyses.

### Phase 6: Manuscript and policy brief, 2 to 4 weeks

- Draft the paper around results, not around the order of the source manuscripts.
- Produce a two to four-page policy brief.
- Produce one implementation diagram and a limited number of clear empirical figures.
- Complete internal technical, banking, legal, data-governance, and editorial review.
- Check originality, prior-publication, and AI-assistance disclosure requirements for the chosen outlet.

### Phase 7: Reproducibility and submission, 1 to 2 weeks

- Freeze data and code versions.
- Generate all tables and charts from reproducible scripts.
- Run reference, equation, and cross-reference checks.
- Prepare anonymous and identified variants if required.
- Validate Word and PDF rendering.
- Submit only through the route confirmed by KBA.

## 10. Immediate engagement package

The first contact package should contain:

- A short email of approximately 180 to 250 words.
- A one-page concept note, or the five-page proposal if already complete.
- A short professional biography.
- Links to public practitioner work only if helpful.

The message should not claim that the paper is under review, selected, or eligible for the closed conference. It should say that the author has developed a related body of research and is seeking the most appropriate KBA route.

The Kenya Bankers Economic Bulletin is the most realistic near-term editorial adaptation. A proposed article could be titled:

> **Underwrite for Collection: What KESONIA-Era Credit Pricing Means after Disbursement**

That article would preserve the human and industry narrative, use a small set of official charts, and present a practical lifecycle scorecard. It should not substitute for the empirical working paper. The Bulletin article can introduce the question, while the working paper supplies the methods and evidence. Before publication, confirm with KBA how prior public articles affect working-paper originality and disclosure.

## 11. Risks and controls

**Closed 2026 cycle:** Seek guidance now and prepare for an off-cycle or 2027 route. Do not force an ordinary submission into a closed process.

**Insufficient empirical data:** Complete the public-data study, pursue a partner dataset, and label any synthetic demonstration accurately.

**Over-broad question:** Freeze a primary outcome set. Treat access, pricing, collectability, and intervention as connected modules, not four unrelated papers.

**Short post-KESONIA history:** Use descriptive and distributed-lag analysis, acknowledge concurrent changes, and avoid causal language without a counterfactual.

**Public pricing-data limitations:** Preserve update dates, benchmark basis, product definitions, fees, and missingness. Do not treat published premium as a borrower-level risk coefficient.

**Technical overreach:** Keep the transparent benchmark and lifecycle model in the main paper. Put Pólya-Gamma, alternative splines, neural residualisation, and copula stress in appendices or challengers unless they materially improve results.

**Regulatory overstatement:** Cite CBK, KBA, legislation, and official methodology for formal requirements. Label proposed systems and controls as recommendations.

**Feature leakage and duplicated representation:** Enforce point-in-time construction, one owner for each explicit feature, cross-fitting, residualisation, and out-of-time testing.

**Intervention-selection bias:** Prefer randomised or phased deployment. If observational, state the assignment mechanism and use a credible adjustment strategy.

**Publication overlap:** Maintain a disclosure register showing which material appeared in LinkedIn articles, white papers, proposals, and submissions. Rewrite and cite earlier public work where required. Obtain the outlet’s answer before simultaneous or derivative publication.

## 12. Readiness assessment

The following scores are editorial judgments, not statistical measurements:

| Component | Current readiness | Main work remaining |
|---|---:|---|
| Central industry thesis | 9/10 | Convert into testable contribution |
| Fit with KBA 2026 theme | 9/10 | Use official terminology and narrower scope |
| Five-page proposal | 7/10 | Draft abstract, hypotheses, data, and method |
| Bulletin article | 8/10 | Add KESONIA framing, official charts, and house style |
| Conceptual working paper | 8/10 | Consolidate and remove project-specific material |
| Empirical full paper | 4/10 | Build dataset, estimates, results, and robustness |
| Institution-data study | 2/10 | Secure partner and governance approvals |
| Methodological prototype | 6/10 | Implement reproducible baseline and synthetic fallback |
| Reproducibility package | 3/10 | Data pipeline, code, tests, and documentation |
| Ordinary 2026 conference submission | 1/10 | Formal deadlines have passed; seek exceptional guidance |
| Off-cycle or 2027 competitive submission | 7/10 | Complete empirical programme and peer review |

The work is ready to open a serious conversation with the KBA Research Centre. It is ready to become a strong proposal and a timely Bulletin article. Its full research-paper readiness depends on empirical execution.

## 13. Definition of done

The KBA research programme will be ready for formal submission when:

- KBA has confirmed the appropriate publication or conference route.
- The paper answers one primary question and a controlled set of hypotheses.
- Every regulatory and benchmark statement is sourced to an official publication.
- KESONIA, CBR, the published premium, total cost of credit, expected loss, funding cost, capital, and profit are defined separately.
- Lending flows, outstanding balances, NPL stocks, and NPL ratios use their correct periods and denominators.
- The data dictionary, observation window, missingness, and transformations are documented.
- The empirical design distinguishes association from causal effect.
- All model inputs are point-in-time correct and free of post-outcome leakage.
- Origination, delinquency, cure, restructure, default, and recovery are defined operationally.
- Model comparisons use out-of-time or out-of-vintage validation.
- Intervention effects are supported by an appropriate comparison design.
- Results include calibration, uncertainty, net recovery, and decision consequences.
- Recommendations are implementable by banks, KBA, data partners, and policymakers.
- The manuscript has undergone independent banking, quantitative, regulatory, and editorial review.
- Code and permitted data are reproducible from a frozen release.
- Prior publication and AI-assisted drafting are disclosed according to the selected outlet’s rules.
- The final Word and PDF files pass visual, citation, equation, table, and accessibility checks.

## 14. Recommended decision

Proceed on two coordinated tracks.

First, contact the KBA Research Centre now with a disciplined concept note and ask for the appropriate route. Adapt “Underwrite for Collection” into a concise Economic Bulletin article that connects KESONIA-era pricing to lifecycle collection and NPL prevention.

Second, build the empirical working paper for off-cycle review or the next conference. Use public KBA and CBK data for the benchmark and pricing-transmission layer, while pursuing an anonymised institutional dataset for delinquency, cure, intervention, and recovery. Preserve the hierarchical Bayesian and AI architecture as a governed methodological extension, but let the evidence determine which components enter the principal results.

This route converts the project’s existing depth into a focused Kenyan banking contribution. It preserves the strongest ideas from the manuscripts while giving KBA what its research programme asks for: a clear policy question, credible evidence, practical methodology, and recommendations that institutions can implement.

## 15. Core official sources for the next stage

- Kenya Bankers Association, [Call for Papers: 15th Annual Banking Research Conference](https://www.kba.co.ke/wp-content/uploads/2026/03/KBA-Call-for-Papers-2026-Advert-3.pdf).
- Kenya Bankers Association, [Call for Papers page](https://www.kba.co.ke/call-for-papers/).
- Central Bank of Kenya, [KESONIA official page and published series](https://www.centralbank.go.ke/kesonia/).
- Central Bank of Kenya, [Revised Risk-Based Credit Pricing Model](https://www.centralbank.go.ke/wp-content/uploads/2025/08/Revised-Risk-based-Credit-Pricing-Model.pdf).
- Kenya Bankers Association, [Position on the CBK Consultative Paper on Risk-Based Credit Pricing](https://www.kba.co.ke/wp-content/uploads/2025/05/KBA-POSITION-ON-CBK-CONSULTATIVE-PAPER-ON-RISK-BASED-CREDIT-PRICING.pdf).
- Kenya Bankers Association, [Total Cost of Credit portal](https://www.costofcredit.co.ke/site/interest-rate).
- Kenya Bankers Association, [MSME Credit Dashboard](https://msmedata.kba.co.ke/).
- Central Bank of Kenya, [Commercial Banks’ Weighted Average Rates](https://www.centralbank.go.ke/commercial-banks-weighted-average-rates/).
- Central Bank of Kenya, [Bank Supervision and Banking Sector Reports](https://www.centralbank.go.ke/reports/bank-supervision-and-banking-sector-reports/).
