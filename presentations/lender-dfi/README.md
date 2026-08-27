# Lender and DFI Presentation

`source/build_deck.mjs` contains the 18-slide presentation generator. It uses the OpenAI artifact runtime and writes local output to `build-output/` unless `MWENDO_DECK_OUTPUT_DIR` is set.

The previous PPTX remains in the ignored local archive because it has not passed the desired visual-quality threshold. No deck is currently designated as a release.

A PPTX may be promoted to `release/` only after:

- numerical outputs tie to the approved workbook;
- all 18 slides render without clipping or overlap;
- diagrams and charts remain readable at normal presentation size;
- source notes support every substantive claim;
- terminology matches the white paper and controlled baseline; and
- the complete deck passes visual inspection rather than only automated shape checks.
