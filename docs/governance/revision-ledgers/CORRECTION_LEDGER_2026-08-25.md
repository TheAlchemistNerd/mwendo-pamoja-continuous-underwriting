# Mwendo Pamoja White Paper Targeted Correction Ledger

Date: 25 August 2026

Preservation rule: The 25 August 2026 pre-correction sources, build files, and canonical PDF are retained in `revision_backups/2026-08-25_pre_targeted_whitepaper_corrections` with a SHA-256 manifest. This pass uses section-anchored edits and does not reset or clean the existing Git worktree.

| ID | Source area | Correction | Type | Validation |
|:---|:---|:---|:---|:---|
| WP-C01 | Part 1, Figure 2 | Add adaptive full-page figure treatment while preserving all diagram content | PDF layout | Passed: largest unclipped portrait render inspected at full resolution; labels and relationships retained |
| WP-C02 | Part 2a, body and references | Rebuild IEEE sequence from first appearance and remove unused or duplicate entries | Citation | Passed: body first appearances and reference definitions both run sequentially from [1] to [15], with no missing or orphaned entries |
| WP-C03 | Part 2a, Figures 1 and 2 | Correct figure order, adjacent references, and full-page sizing | Editorial and layout | Passed: captions, adjacent text, PDF text, and full-page renders agree on Figures 1 and 2 |
| WP-C04 | Part 2a, low-frequency ingestion | Replace BLS with CBK, World Bank, and IMF sources and revision lineage | Technical | Passed: source and PDF text name CBK, World Bank, and IMF; the BLS wording is absent |
| WP-C05 | Part 1 and dependent Part 4 sentence | Distinguish premium, premium funding, IPF finance receivable, and eligible SPV transfer | Legal-structural | Passed: Part 1 treatment, Figure 1, Part 4 dependency, and Kenyan primary-source references agree |
| WP-C06 | Parts 2b and 5 | Move physical-versus-pricing measure discussion and abridged structural bridge into Part 5 | Mathematical and editorial | Passed: Part 2b retains its underwriting bridge; Part 5 Section 6.1 and Appendix A contain the pricing and valuation treatment |
| WP-C07 | Parts 3 and 4 | Replace defensive pre-conclusion text with constructive adapter and assurance language | Editorial | Passed: legacy sentence is absent from source and extracted PDF text; replacement passages render cleanly |
| WP-C08 | Part 4, Sections 3.2 and 4.1 | Add contract-led fit-gap process and native, external, and hybrid ECL configuration | Accounting and technical | Passed: both sections and the ECL equation were inspected at full resolution |
| WP-C09 | Part 5, Section 15 | Add SPV cash-flow ladder, matched-funding attribution, OFSAA fit, and tangible IRRBB case | Treasury and technical | Passed: formulas, Oracle citations, IRRBB definition, and worked repricing use case render without clipping |
| WP-C10 | Parts 1-6 references | Ensure every numbered reference begins as a separate Markdown paragraph | Editorial | Passed: automated scan found a blank paragraph boundary before every numbered reference in all seven parts |
| WP-C11 | Part 5 appendices | Add structural valuation bridge and retitle prototype as deterministic planning model | Mathematical and editorial | Passed: Appendices A and B each begin on a separate page; legacy Monte Carlo labels are absent |
| WP-C12 | Part 6 headings | Reset internal numbering from 1 through 11 and renumber subsections | Editorial | Passed: Part 6 starts at Section 1 and ends at Section 11; dependent subsection numbering is consistent |
| WP-C13 | Selected figures | Add `fullpage` and `landscape` Mermaid layout attributes only where requested | PDF layout | Passed: all targeted Mermaid diagrams render on dedicated pages without clipping; Part 6 Figures 1 and 3 are legible landscape pages |
| WP-C14 | Markdown callouts | Render NOTE and IMPORTANT blockquotes as native PDF boxes | PDF layout | Passed: blue NOTE and gold IMPORTANT boxes inspected; no literal callout markers remain in extracted PDF text |
| WP-C15 | Part 5, Figure 2 and Tables 1-2 | Separate caption blocks and make tables portable, concise Pandoc tables | PDF layout | Passed: Figure 2 caption begins on its own line; both tables are Pandoc table nodes and captions remain with their tables |
| WP-C16 | Part 3 terminal pages | Increase footer safety and inspect the paragraph previously reported on page 83 | PDF layout | Passed: reflowed terminal Part 3 page inspected at full resolution with clear separation above the footer |
| WP-C17 | Parts 1-6 references | Begin every part-level References section on a new PDF page | PDF layout | Passed: seven References headings render at the top of seven separate pages |
| WP-C18 | Parts 1-6 headings | Normalize all substantive sections to self-contained, part-local hierarchical numbering | Editorial | Passed: source hierarchy, contents pages, cross-references, and representative body pages verified |
| WP-C19 | White-paper cover | Add `nevillemaloba@gmail.com` as the author contact without placing it in running furniture | Editorial and PDF layout | Passed: white cover text inspected at full resolution; running headers and footers remain unchanged |

## Directly consulted primary sources

- Republic of Kenya, *Insurance Act*, sec. 156.
- Republic of Kenya, *Capital Markets Act*, Part IVB.
- Republic of Kenya, *Capital Markets (Asset-Backed Securities) Regulations*.
- Central Bank of Kenya publications and KESONIA material.
- Oracle Financial Services ALM, FTP, integration, and cash-flow-engine documentation.
- Basel Committee on Banking Supervision, BCBS 368.
- IFRS Foundation, IFRS 9 project summary.

The corrected PDF was rendered to 155 page images after the numbering and reference-pagination pass. Every contact sheet and each listed high-risk page was inspected before the validation statuses above were closed.
