# Active work and current-manuscript errata

## What remains after retiring the rough notes

| Priority | Work item | Completion evidence | Owner document |
|---|---|---|---|
| 1 | Obtain permitted provider data and freeze releases | Access/terms record, dictionary version, file checksums and reproducible sample manifest | R2/R3/R5 P1 |
| 1 | Validate longitudinal panels and implement vintage/state definitions | Cohort coverage, code mapping, gaps/exits, label maturity, counts at risk and agreed denominators | Addendum V; R5 P3–P5 |
| 1 | Resolve manuscript equations that conflict with the intended definitions | Checked derivation and updated manuscript/build | Errata below |
| 2 | Run registered hierarchy, prior-conflict and timing/cure comparisons | Development pilots, locked holdouts, estimates and uncertainty, all comparisons reported | R1–R3 |
| 2 | Quantify information delay and safe fallback | Simulated known-truth comparison and later partner workflow study | Addendum F; RQ1/RQ8 |
| 2 | Reconcile cash amounts, timing and economic measures | Cash/loss reconciliation with no double counting; transparent funding assumptions | RQ5/RQ7/RQ8 |
| 3 | Test origination integrity and intervention delivery | Authorised partner extract, clear estimand, assignment/confounding evidence and customer outcomes | Addendum G/I |
| 3 | Operationalise option inventory and treasury scenarios | Actual contract fields and paired fixed/behavioural scenario results | Addendum O/D |

These priorities order execution; they do not imply all partner-dependent studies must be squeezed into the first manuscript. The framework paper may present derivations and simulation with clear external-validation limits.

## Current manuscript conflicts found during this review

### E1. Telematics companion derivations contain obsolete guarantees

`whitepapers/telematics-relativities/Mathematical_Derivations.md` §§3–5 still says residualisation enforces tariff neutrality and equalized odds, and that noncentering completely removes scale dependence. The root copy was identical. The main paper §§4.2 and 7 provides better calibration and update treatment.

**Disposition:** archive the root duplicate; mark the retained companion as a historical draft with a prominent warning and direct readers to the main paper and this correction ledger. A future rebuilt mathematical appendix must use explicit normalisation, conditional assumptions, recursive sufficient statistics and appropriate computation diagnostics. The main paper's current user edits are preserved.

### E2. Underwrite Part 2b: scale–Cholesky order

The random-slope equation in §3 uses $L_\Omega D\,z$, where $L_\Omega$ is described as a correlation Cholesky factor and $D$ contains marginal scales. If the intended covariance is $D\Omega D$, the transformation must be $D L_\Omega z$:

$$\operatorname{Cov}(D L_\Omega z)=D L_\Omega L_\Omega^T D=D\Omega D.$$

The displayed order instead gives $L_\Omega D^2L_\Omega^T$, which is generally different. This was already identified by R4; the checked manuscript still contains it. **Open manuscript correction**, not a newly completed fix. The Underwrite source is kept read-only in this audit.

### E3. Mwendo Part 5: earnings-at-risk sign

Section 4.2 defines $EaR_{12m}=NII_{base}-NII_{shock}$ and later describes a material negative EaR as a reason for action. Under that loss-positive definition, an adverse earnings shortfall is positive. **Open editorial correction:** change the narrative to positive EaR, or consistently redefine every sign and limit. The addendum uses the loss-positive convention.

### E4. Mwendo Part 2b: recovery cost ownership

Section 4's cash-loss expression subtracts an amount described as *net ordinary recovery* and separately adds collection/recovery cost. M0 §8 describes gross recovery, cost and delay as separate components. Define $R$ as gross receipts with $C$ added separately, or use net recovery and exclude the already-netted costs from $C$. **Open interface clarification:** reconcile the manuscript, model specification and eventual loss dataset before implementation.

### E5. Source freshness needs an operational control

Point-in-time feature construction is already strong. A separate pre-disbursement revalidation control and its evaluation were not comparably explicit. **Addressed at protocol level by addendum F; implementation and evidence remain open.**

### E6. Vintage analysis needed a dedicated contract

Temporal cohorts and lifecycle analysis existed, but the reporting denominators, first-crossing curves and cure distinction needed consolidation. **Addressed at protocol level by addendum V; empirical exhibits remain open.**

## Retirement boundaries

The continuous-underwriting DOCX, smaller exploratory logistic note and actuarial fragments are historical sources, not the next paper drafts. The previously audited *So picking…* DOCX remains at its existing root path because the current research package uses it as an active provenance source. Its continued presence is intentional.

The DCP positioning note remains active and is moved into `docs/research/industry-engagement/`. The two Underwrite project directories and existing output/build folders are not classified as litter merely from their names. No project directory is deleted. Diagnostic dumps and superseded root notes are archived with hashes.

The relevant screenshots are conceptual prompts. Their conclusions do not become requirements, current laws, empirical facts or instructions to contact anyone.

<!-- ADDITIONAL_MATERIAL_2026_09_23 -->

## Additional work register — 23 September 2026

The [supplement](06_ADDITIONAL_MATERIAL_REVIEW_2026-09-23.md) records the new evidence and protocols. All rows below are planned; no empirical completion is claimed.

| Priority | Action | Required completion evidence |
|---|---|---|
| 1 | Define RR/AR/PV availability and economic targets | Field-level source/clock map; unavailable-field register; reconciled exposure, proceeds and loss definitions |
| 1 | Freeze MC acceptance and PM applicability | Held-out comparison/cost plan; entity/asset/framework scope; appropriate benchmark target |
| 2 | Test public-panel components actually observed | Mature longitudinal labels; loss/timing and calibration results; feature-outage sensitivity; negative findings |
| 3 | Validate detailed recovery readiness, trade workflows and purpose | Authorised partner histories; independent evidence checks; censoring/selection analysis |
| 3 | Evaluate executed actions | Assigned owner/deadline, policy and execution histories, causal design and customer/cash outcomes |

The screenshots qualify several claims: missing transaction evidence is not proof of misuse; insured cover is not cash; overdue/disputed balances must not be double counted; a severity increase alone is not a staging rule; greater model complexity is not automatically beneficial. E1–E6 above retain their stated status.
