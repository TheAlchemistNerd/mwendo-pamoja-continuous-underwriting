# D07 Inconsistency Report: Regulatory Orchestration and Interventions

## Document role and semantic synopsis

D07 is intended to translate Mwendo Pamoja's models and interventions into bank, insurer, fairness, forbearance, reporting, and supervisory controls. It covers IFRS 9, Basel IRB, IFRS 17, Solvency II, equalized odds, premium holidays, bridge payments, fatigue routing, forbearance, EBA thresholds, ECOA, ISO 20022, and XBRL. Its aspiration to make interventions auditable is sound. Its central inconsistency is jurisdiction: Kenyan, international accounting, EU, UK-like prudential, and US fair-lending concepts are written as one binding regime.

The paper also treats accounting standards as prudential requirements, statistical thresholds as regulatory triggers, and technology payloads as recognised reporting channels. Equations contain punctuation corruption. Several actions could help drivers but may themselves modify contracts, create forbearance, discriminate, or require platform and carrier authority.

## Executive inconsistency summary

D07 requires a jurisdiction and applicability matrix before any substantive redraft. IFRS 9 applies to financial instruments of the reporting entity; IFRS 17 applies to insurance contracts of the carrier. Basel IRB applies to an approved bank under local implementation. Solvency II, EBA guidance, ECOA, and SR 11-7 can be comparative references but are not automatically Kenyan law. The Clayton parameter cannot replace Basel correlation. A one-percent NPV rule is not a universal IFRS 9 modification test. Equalized odds and MMD do not prove absence of redlining. ISO 20022 fields and a CBK real-time SupTech API must not be invented.

## Prioritised issue matrix

| Finding | Severity | Confidence | Anchor | Main impact |
|---|---|---|---|---|
| D07-I01 | Critical | High | Opening framework headings | Applicable law and comparative guidance are merged |
| D07-I02 | High | High | IFRS 9 impairment | Entity, PD measure, staging, and interventions are incomplete |
| D07-I03 | Critical | High | Basel IV A-IRB | Approval and prescribed correlations are misstated |
| D07-I04 | High | High | Basel formulas | Mathematical corruption and output-floor treatment are unreliable |
| D07-I05 | Critical | High | Forbearance and 1% NPV rule | Foreign thresholds are presented as IFRS law |
| D07-I06 | High | High | PSI and monitoring | Heuristic triggers are presented as regulator mandates |
| D07-I07 | Critical | High | IFRS 17 and Solvency II | Carrier, accounting, and prudential regimes are conflated |
| D07-I08 | Critical | High | ISO 20022 and XBRL | Message and regulator endpoint claims are unverified |
| D07-I09 | High | High | Fairness and interventions | US concepts and technical metrics do not establish Kenyan compliance |
| D07-I10 | High | Medium | Assistive ecosystem | Contract authority and adverse effects are not controlled |
| D07-I11 | Medium | High | References and terminology | Sources do not support the strength of conclusions |

## Detailed findings

### D07-I01: The document has no jurisdictional applicability map

**Anchor:** “Bank-Counterparty Regulatory Framework Integration,” “Insurtech Regulatory Framework Integration,” and “Algorithmic Equity and Fairness Frameworks.” Basel IV, IFRS, Solvency II, EBA, ECOA, and Kenyan supervision appear in one narrative without classifying authority.

**Impact:** Readers may believe EU solvency rules or US fair-lending statutes bind a Kenyan SPV, or that international accounting standards grant a lending licence. This can misdirect implementation effort and create inaccurate investor representations.

**Canonical resolution:** Begin with a matrix listing rule, jurisdiction, regulated entity, topic, legal status, local implementation, owner, and evidence. Kenyan law and CBK or Insurance Regulatory Authority requirements should lead. IFRS standards apply through reporting requirements. Basel applies through the regulated lender and local implementation. Solvency II, EBA, ECOA, and SR 11-7 are comparative unless counsel identifies direct or contractual applicability.

### D07-I02: IFRS 9 ECL is conflated with real-time underwriting

**Anchor:** “IFRS 9 Impairment Pipeline under Joint Tail Distress.” The paper suggests model scores and copula stress automatically determine stages and provisions, with limited treatment of reporting entity, contractual EIR, EAD, LGD, scenarios, SICR policy, or cure.

**Impact:** Underwriting can update frequently, but financial reporting needs controlled period-end data, approved assumptions, unbiased probability-weighted scenarios, and auditable journals [5]. Interventions change cash flows and observed outcomes and can require modification or forbearance analysis.

**Canonical resolution:** Define separate underwriting and IFRS 9 models or controlled mappings. Use `PD_P`, not risk-neutral PD, for ordinary ECL. Document staging, SICR, default, cure, write-off, restructuring, forward-looking scenarios, management overlay, validation, close calendar, approvals, and ledger reconciliation for each holder of financial assets.

### D07-I03: A-IRB status and capital relief are assumed

**Anchor:** “Basel IV Advanced IRB Capital Requirements.” The paper presents an A-IRB calculation as an available route and suggests submitting a Clayton dependence parameter can reduce the regulatory correlation `R`.

**Impact:** IRB use requires supervisory permission, long-run data, parameter governance, independent validation, and compliance with prescribed formulas and floors. The SPV is not the bank, and an internal copula cannot override regulatory correlations [8].

**Canonical resolution:** State that lender capital treatment is determined by each bank under applicable CBK rules and the Basel framework. Use HBLR and copulas for underwriting and economic capital unless approval explicitly permits a prudential use. Present capital relief only after the lender's regulatory team confirms exposure class, approach, risk weights, credit-risk mitigation, and securitisation treatment.

### D07-I04: Basel expressions and phase-in statements are unreliable

**Anchor:** Basel formulas and output-floor discussion. The source contains damaged minus signs, inequality symbols, and ranges. “Basel IV” is treated as a single directly effective code, and output-floor timing is not tied to Kenyan implementation.

**Impact:** A corrupted normal-CDF expression can produce materially wrong risk-weighted assets. Global Basel publications do not enforce themselves without local implementation and transition.

**Canonical resolution:** Re-key formulas from the current Basel Framework [8]. Add units, asset class, maturity, prescribed correlation, PD and LGD floors, scaling, and example calculations. State implementation as of a dated Kenyan legal review. Use “Basel III final reforms” where precision is needed and identify “Basel IV” as informal terminology.

### D07-I05: The one-percent NPV rule is not a universal IFRS 9 rule

**Anchor:** “Forbearance vs. Assistive Interventions” and “Accounting Integration and the 1% NPV Rule.” The paper imports EBA-style guidance and implies a one-percent NPV change controls modification accounting or default classification.

**Impact:** EBA guidance applies in its European supervisory context. IFRS 9 does not contain a universal one-percent asset modification bright line. The familiar 10% test is primarily used for financial liabilities, not as an automatic asset test. A bridge designed to avoid Stage 3 may become shadow forbearance.

**Canonical resolution:** Create an intervention accounting decision tree based on contractual change, financial difficulty, concession, default definition, EIR, modification gain or loss, derecognition analysis, and local supervisory guidance. Cite [5] and entity accounting policy. Treat foreign thresholds as comparative indicators only.

### D07-I06: PSI 0.25 is converted into a legal trigger

**Anchor:** continuous monitoring and supervisory auditing sections. The draft links a PSI threshold to retraining, regulator notice, or suspension of advanced modelling.

**Impact:** PSI depends on bins, base population, and sample size. It identifies distribution shift, not whether calibration or customer outcomes failed. No indexed primary Kenyan source establishes 0.25 as a statutory threshold.

**Canonical resolution:** Label 0.10 and 0.25 as internal monitoring conventions or contractual covenants. Define population, variables, window, minimum sample, escalation, investigation, challenger review, and approval. Monitor calibration, discrimination, uncertainty, missingness, fairness, outcomes, and data quality alongside PSI. Use SR 11-7 only as comparative governance [9].

### D07-I07: Insurance issuer, IFRS 17, and Solvency II are merged

**Anchor:** “Insurtech Regulatory Framework Integration,” “IFRS 17 Accounting Protocols,” and “Solvency II Solvency Capital Requirement.” D07 sometimes calls the technology company carrier or MGA, applies IFRS 17 broadly, and uses Solvency II as if it directly governs Kenyan capital.

**Impact:** The licensed carrier, not the technology provider or SPV, normally issues the insurance contract and applies IFRS 17 in its reporting perimeter [6]. Kenyan prudential insurance requirements must be identified separately. PAA eligibility and onerous-group treatment are also simplified.

**Canonical resolution:** Freeze entity roles. State the carrier's licence, contract issuance, claims, premium, refund, and IFRS 17 responsibilities. Determine applicable Insurance Regulatory Authority capital rules through counsel. Use Solvency II only as a stress and governance comparator if useful. Document PAA eligibility and onerous-group testing rather than assuming them.

### D07-I08: ISO 20022 and regulator telemetry are invented

**Anchor:** “Continuous Control Monitoring via ISO 20022 and XBRL Taxonomies.” The paper proposes `auth.015` and custom tags for risk premium, explainability, and EIR, with near-real-time regulator transmission.

**Impact:** ISO 20022 message definitions have governed business purposes. Custom XML tags are not standard merely because they look plausible [13]. No evidence in the corpus establishes a CBK API accepting those fields. False interoperability claims can derail procurement and regulatory engagement.

**Canonical resolution:** Rename the section “Proposed Regulatory Reporting and Evidence Interface.” Inventory actual CBK, IRA, credit-bureau, AML, and financial-report requirements. Map each to existing channel, frequency, schema, signer, and owner. Use XBRL only where the relevant filing taxonomy requires it and ISO 20022 only under an agreed implementation guide. Keep internal SHAP and EIR evidence in governed audit packages unless requested.

### D07-I09: Fairness law and fairness mathematics are conflated

**Anchor:** “Equalized Odds,” “ECOA/Disparate Impact,” and LDA testing. US ECOA concepts are presented as direct Kenyan obligations; equalized odds is treated as the solution to redlining.

**Impact:** Applicable Kenyan equality, consumer-protection, data-protection, and credit laws need specific analysis. No single metric resolves calibration, access, pricing, error costs, proxy use, or adverse action. MMD cannot guarantee equalized odds.

**Canonical resolution:** Commission a Kenyan legal assessment. Use ECOA and LDA as comparative governance only. Measure selection, pricing, limits, error rates, calibration, interventions, complaints, and appeals by legally reviewed groups. Add confidence intervals and minimum sample rules. Link automated-decision transparency and DPIA to [10], [11].

### D07-I10: Assistive actions lack contractual and outcome controls

**Anchor:** “Operationalizing the Assistive Ecosystem,” “Financial Safety Net Interventions,” and “Supervisory Auditing.” The draft assumes authority to grant premium holidays, bridge cash, alter routes, freeze draws, and reserve amounts.

**Impact:** The action may belong to the carrier, lender, platform, servicer, or customer. It may change contract cash flows, create a concession, harm income, or produce disparate effects. A fatigue-routing action may improve safety but reduce earnings.

**Canonical resolution:** For each intervention state trigger owner, approving party, customer notice and consent, amount, duration, funding source, accounting, policy consequence, override, appeal, safety escalation, and outcome measure. Use randomised or quasi-experimental evaluation where feasible. Prevent interventions from being selected solely to improve accounting stage.

### D07-I11: Evidence is often analogy rather than authority

**Anchor:** References. The paper cites international and vendor material but does not distinguish primary standards, local law, comparative guidance, and industry commentary.

**Impact:** Strong conclusions rest on sources that do not govern the relevant entity or jurisdiction.

**Canonical resolution:** Use the global IEEE index. Place [1]-[3], [5], [6], [8], [10], [11], and actual Kenyan requirements beside operative claims. Mark [9], [19], and foreign frameworks as comparative. Add an as-of date and legal-review status to every time-sensitive section.

## Dependencies, evidence gaps, and remediation sequence

D07 depends on D01 and D04 for entity and intervention roles, D05 and D06 for data and model boundaries, D08 for evidence and reporting systems, D09 for KESONIA and accounting mechanics, and D10 for governance delivery. Required evidence includes Kenyan legal opinions, licences, insurer accounting policy, lender regulatory-capital memo, ECL methodology, intervention contracts, privacy DPIA, reporting inventory, regulator correspondence, and model-validation policy.

Remediation should begin with the applicability matrix and entity perimeter. Next separate accounting, prudential, contractual, policy, and statistical rules. Rebuild IFRS 9 and IFRS 17 sections. Remove IRB capital-relief and invented reporting claims. Then define intervention governance and fairness. Finally repair formulas and sources.

## Finding-to-plan map

| Finding | Planned actions |
|---|---|
| D07-I01 | D07-P02, D07-P03 |
| D07-I02 | D07-P04 |
| D07-I03 | D07-P05 |
| D07-I04 | D07-P01, D07-P05 |
| D07-I05 | D07-P07 |
| D07-I06 | D07-P06 |
| D07-I07 | D07-P03, D07-P04 |
| D07-I08 | D07-P09 |
| D07-I09 | D07-P08 |
| D07-I10 | D07-P07, D07-P08 |
| D07-I11 | D07-P01, D07-P10 |
