param(
    [string]$OutputName = 'Mwendo_Pamoja_Continuous_Underwriting_White_Paper_Build.pdf'
)

$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest

if ([System.IO.Path]::GetFileName($OutputName) -ne $OutputName) {
    throw 'OutputName must be a file name without directory components.'
}

$buildDirectory = $PSScriptRoot
$paperRoot = Split-Path -Parent $buildDirectory
$whitepapersRoot = Split-Path -Parent $paperRoot
$projectRoot = Split-Path -Parent $whitepapersRoot
$sourceDirectory = Join-Path $paperRoot 'parts'
$tempDirectory = Join-Path $projectRoot 'scratchpad\build\whitepaper'
$outputDirectory = Join-Path $paperRoot 'dist'
$assemblyPath = Join-Path $tempDirectory 'Mwendo_Pamoja_White_Paper_Assembly.md'
$outputPath = Join-Path $outputDirectory $OutputName
$corporateMetadata = Join-Path $buildDirectory 'corporate.yaml'
$headerPath = Join-Path $buildDirectory 'whitepaper-header.tex'
$mermaidFilter = Join-Path $buildDirectory 'mermaid.lua'

[System.IO.Directory]::CreateDirectory($tempDirectory) | Out-Null
[System.IO.Directory]::CreateDirectory($outputDirectory) | Out-Null

$parts = @(
    [pscustomobject]@{
        Label = 'Part 1'
        Title = 'Architecture of the Insurtech Product, Multi-Product Capital Stack, and the Default Cascade'
        File = 'Part_1_Product_Architecture_and_Cascades.md'
    },
    [pscustomobject]@{
        Label = 'Part 2a'
        Title = 'Advanced Predictive Modeling, Deep Temporal Representation, and Feature Engineering'
        File = 'Part_2a_Deep_Temporal_Representation_and_Feature_Engineering.md'
    },
    [pscustomobject]@{
        Label = 'Part 2b'
        Title = 'Continuous Underwriting via Hierarchical Bayesian Logistic Regression and Asymmetric Copulas'
        File = 'Part_2b_Bayesian_Underwriting_and_Asymmetric_Copulas.md'
    },
    [pscustomobject]@{
        Label = 'Part 3'
        Title = 'Joint Regulatory Capital Orchestration, Algorithmic Fairness, and Assistive Controls'
        File = 'Part_3_Regulatory_Orchestration_and_Interventions.md'
    },
    [pscustomobject]@{
        Label = 'Part 4'
        Title = 'Enterprise ERP and Telemetry'
        File = 'Part_4_Enterprise_ERP_and_Telemetry.md'
    },
    [pscustomobject]@{
        Label = 'Part 5'
        Title = 'KESONIA Pricing and Capital Orchestration'
        File = 'Part_5_KESONIA_Pricing_and_Capital_Orchestration.md'
    },
    [pscustomobject]@{
        Label = 'Part 6'
        Title = 'Implementation Roadmap and Execution'
        File = 'Part_6_Implementation_Roadmap_and_Execution.md'
    }
)

function Remove-YamlFrontMatter {
    param([string]$Text)

    $normalised = $Text -replace "`r`n", "`n"
    if (-not $normalised.StartsWith("---`n")) {
        return $normalised
    }

    $closing = $normalised.IndexOf("`n---`n", 4, [System.StringComparison]::Ordinal)
    if ($closing -lt 0) {
        throw 'A source file has an unterminated YAML front matter block.'
    }

    return $normalised.Substring($closing + 5).TrimStart("`n")
}

$builder = [System.Text.StringBuilder]::new()
[void]$builder.AppendLine('\WhitePaperCover')
[void]$builder.AppendLine()
[void]$builder.AppendLine('\WhitePaperLicensePage')
[void]$builder.AppendLine()
[void]$builder.AppendLine('\pagenumbering{roman}')
[void]$builder.AppendLine('\gdef\CurrentPart{Contents}')
[void]$builder.AppendLine('\tableofcontents')
[void]$builder.AppendLine('\clearpage')
[void]$builder.AppendLine('\pagenumbering{arabic}')
[void]$builder.AppendLine()

foreach ($part in $parts) {
    $sourcePath = Join-Path $sourceDirectory $part.File
    if (-not (Test-Path -LiteralPath $sourcePath)) {
        throw "Missing source document: $sourcePath"
    }

    $body = Remove-YamlFrontMatter -Text ([System.IO.File]::ReadAllText($sourcePath))
    $referenceHeadingReplacement = '\clearpage' + [Environment]::NewLine + '$1 $2 {.unnumbered}'
    $body = [regex]::Replace(
        $body,
        '(?m)^(#{1,6})\s+(Selected IEEE references|References)\s*$',
        $referenceHeadingReplacement
    )

    [void]$builder.AppendLine("\WhitePaperPart{$($part.Label)}{$($part.Title)}")
    [void]$builder.AppendLine()
    [void]$builder.AppendLine($body.Trim())
    [void]$builder.AppendLine()
}

$glossaryPath = Join-Path $paperRoot 'glossary.md'
if (-not (Test-Path -LiteralPath $glossaryPath)) {
    throw "Missing glossary document: $glossaryPath"
}

$glossaryBody = Remove-YamlFrontMatter -Text ([System.IO.File]::ReadAllText($glossaryPath))
[void]$builder.AppendLine('\WhitePaperPart{Reader Guide}{Interdisciplinary Field Map and Technical Glossary}')
[void]$builder.AppendLine()
[void]$builder.AppendLine($glossaryBody.Trim())
[void]$builder.AppendLine()

$utf8 = [System.Text.UTF8Encoding]::new($false)
[System.IO.File]::WriteAllText($assemblyPath, $builder.ToString(), $utf8)

$resourcePath = "$paperRoot;$projectRoot"
$pandocArguments = @(
    '--from=markdown+raw_tex+tex_math_dollars+tex_math_single_backslash+autolink_bare_uris',
    "--metadata-file=$corporateMetadata",
    "--lua-filter=$mermaidFilter",
    "--include-in-header=$headerPath",
    '--pdf-engine=xelatex',
    '--pdf-engine-opt=-halt-on-error',
    '--highlight-style=tango',
    "--resource-path=$resourcePath",
    "--output=$outputPath",
    $assemblyPath
)

Push-Location $paperRoot
try {
    & pandoc @pandocArguments
    if ($LASTEXITCODE -ne 0) {
        throw "Pandoc failed with exit code $LASTEXITCODE."
    }
}
finally {
    Pop-Location
}

if (-not (Test-Path -LiteralPath $outputPath)) {
    throw "Expected PDF was not created: $outputPath"
}

Write-Output $outputPath
