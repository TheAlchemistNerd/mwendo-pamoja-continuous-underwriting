# Mwendo Pamoja White Paper

The canonical white paper is assembled from the Markdown files in `parts/`, followed by `glossary.md`. The reviewed publication is stored in `dist/`.

## Build

Requirements:

- Pandoc.
- XeLaTeX with the packages referenced by `whitepaper-header.tex`.
- Mermaid CLI available to the Lua filter.
- Georgia, Arial, and Consolas, or compatible configured fonts.

From the repository root:

```powershell
powershell -ExecutionPolicy Bypass -File .\whitepapers\mwendo-pamoja\build\build_whitepaper.ps1
```

The default command creates `Mwendo_Pamoja_Continuous_Underwriting_White_Paper_Build.pdf`. To deliberately rebuild the release filename:

```powershell
powershell -ExecutionPolicy Bypass -File .\whitepapers\mwendo-pamoja\build\build_whitepaper.ps1 -OutputName Mwendo_Pamoja_Continuous_Underwriting_White_Paper_Final.pdf
```

Assembly and rendering intermediates are written to the ignored `scratchpad/build/whitepaper/` directory. References, figures, tables, equations, cover treatment, part-title pages, headers, and footers must be visually verified before replacing the reviewed release.
