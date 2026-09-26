$ErrorActionPreference = 'Stop'
$workspaceRoot = [IO.Path]::GetFullPath((Join-Path $PSScriptRoot '../../../..'))
$downloadsRoot = Split-Path -Parent $workspaceRoot
$archiveRoot = Join-Path $workspaceRoot '_archive/repository_migration_2026-09-26/retired'
$validation = Get-Content -LiteralPath (Join-Path $PSScriptRoot 'validation_report.json') -Raw | ConvertFrom-Json
if (-not $validation.migration_checks_passed) { throw 'Migration validation has not passed.' }
$transfer = Get-Content -LiteralPath (Join-Path $PSScriptRoot 'transfer_manifest.json') -Raw | ConvertFrom-Json
$moves = @(
    @{ Relative = 'whitepapers/telematics-relativities'; Repository = 'bayesian-telematics-relativities'; NewRelative = 'whitepapers/telematics-relativities' },
    @{ Relative = 'publications/submissions/brian-hey-2026'; Repository = 'bayesian-telematics-relativities'; NewRelative = 'publications/submissions/brian-hey-2026' },
    @{ Relative = 'docs/research/kesonia'; Repository = 'regtech-kesonia-treasury'; NewRelative = 'docs/research/kesonia' },
    @{ Relative = 'output/kesonia_treasury_deep_review_2026-09-25'; Repository = 'regtech-kesonia-treasury'; NewRelative = 'output/kesonia_treasury_deep_review_2026-09-25' },
    @{ Relative = 'behavioural credit scoring - underwrite to collect rct'; Repository = 'behavioural credit scoring - underwrite to collect rct'; NewRelative = '' }
)
function Inside([string]$Path, [string]$Boundary) {
    $full = [IO.Path]::GetFullPath($Path)
    $prefix = [IO.Path]::GetFullPath($Boundary).TrimEnd('\')+'\'
    if (-not $full.StartsWith($prefix, [StringComparison]::OrdinalIgnoreCase)) { throw "Outside boundary: $full" }
    return $full
}
function Digest([string]$Path) { (Get-FileHash -LiteralPath ('\\?\'+[IO.Path]::GetFullPath($Path)) -Algorithm SHA256).Hash.ToLowerInvariant() }
function Write-Utf8([string]$Path, [string]$Content) {
    [void][IO.Directory]::CreateDirectory('\\?\'+[IO.Path]::GetDirectoryName($Path))
    [IO.File]::WriteAllText('\\?\'+$Path, $Content, [Text.UTF8Encoding]::new($false))
}
# Resolve every recursive move before performing any of them.
foreach ($move in $moves) {
    $move.Source = Inside (Join-Path $workspaceRoot $move.Relative) $workspaceRoot
    $move.Archive = Inside (Join-Path $archiveRoot $move.Relative) $archiveRoot
    $move.Destination = Inside (Join-Path $downloadsRoot ($move.Repository+'/'+$move.NewRelative)) $downloadsRoot
    if (-not (Test-Path -LiteralPath $move.Source)) { throw "Missing source: $($move.Source)" }
    if (Test-Path -LiteralPath $move.Archive) { throw "Archive already exists: $($move.Archive)" }
    if (-not (Test-Path -LiteralPath $move.Destination)) { throw "Missing installed destination: $($move.Destination)" }
    if (((Get-Item -LiteralPath $move.Source -Force).Attributes -band [IO.FileAttributes]::ReparsePoint) -ne 0) { throw 'Refusing junction retirement.' }
}
foreach ($entry in $transfer.files) {
    if ((Digest $entry.source) -ne $entry.source_sha256) { throw "Source changed: $($entry.source)" }
}
foreach ($property in $transfer.underwrite.inner_hashes.PSObject.Properties) {
    if ((Digest (Join-Path $transfer.underwrite.inner $property.Name)) -ne $property.Value) { throw "Inner Underwrite changed: $($property.Name)" }
}
$redirects = @()
foreach ($move in $moves) {
    New-Item -ItemType Directory -Path (Split-Path -Parent $move.Archive) -Force | Out-Null
    Move-Item -LiteralPath $move.Source -Destination $move.Archive
    foreach ($file in (Get-ChildItem -LiteralPath $move.Archive -Recurse -File -Force | Where-Object { $_.Extension -in @('.md','.html') -and $_.FullName -notmatch '\\(scratchpad|tmp|node_modules|revision_snapshots)\\' })) {
        $relative = [IO.Path]::GetRelativePath($move.Archive, $file.FullName)
        $destination = Join-Path $move.Destination $relative
        if (-not (Test-Path -LiteralPath $destination)) { continue }
        $pointer = Join-Path $move.Source $relative
        $posix = $destination.Replace('\','/')
        if ($file.Extension -eq '.md') {
            $content = "# This document has moved`n`nThe authoritative working copy is in the standalone **$($move.Repository)** repository.`n`n[Open $($file.Name)](<$posix>)`n`nThis file is a navigation pointer, not an editable mirror. The original was archived on 26 September 2026 under ``_archive/repository_migration_2026-09-26/retired/`` in Mwendo Pamoja.`n"
        } else {
            $uri = ([uri]$destination).AbsoluteUri
            $content = '<!doctype html><html lang="en"><meta charset="utf-8"><title>Document moved</title><body><h1>This document has moved</h1><p>The authoritative version is in '+[Net.WebUtility]::HtmlEncode($move.Repository)+'.</p><p><a href="'+[Net.WebUtility]::HtmlEncode($uri)+'">Open the document in its new repository</a></p><p>The original is preserved in the local migration archive.</p></body></html>'
        }
        Write-Utf8 $pointer $content
        $redirects += @{ OldPath = $pointer; NewPath = $destination }
    }
    $rootReadme = Join-Path $downloadsRoot ($move.Repository+'/README.md')
    Write-Utf8 (Join-Path $move.Source 'README.md') ("# Standalone repository`n`nContinue in [**$($move.Repository)**](<"+$rootReadme.Replace('\','/')+">).`n`nThis former location contains navigation pointers only. All working sources and their build files are owned by the sibling repository. The retired tree is preserved at ``$($move.Archive)``.`n")
}
$verified = 0
foreach ($entry in $transfer.files) {
    foreach ($move in $moves) {
        if ($entry.source.StartsWith($move.Source+'\', [StringComparison]::OrdinalIgnoreCase)) {
            $archived = Join-Path $move.Archive ([IO.Path]::GetRelativePath($move.Source, $entry.source))
            if ((Digest $archived) -ne $entry.source_sha256) { throw "Archived file differs: $archived" }
            $verified++
        }
    }
}
foreach ($property in $transfer.underwrite.inner_hashes.PSObject.Properties) {
    $archived = Join-Path (Join-Path $archiveRoot 'behavioural credit scoring - underwrite to collect rct') $property.Name
    if ((Digest $archived) -ne $property.Value) { throw "Archived Underwrite differs: $archived" }
    $verified++
}
$report = @{ Date = '2026-09-26'; Moves = $moves; NavigationPointers = $redirects; ArchivedFilesHashVerified = $verified; Passed = $true }
$report | ConvertTo-Json -Depth 8 | Set-Content -LiteralPath (Join-Path $PSScriptRoot 'retirement_report.json') -Encoding utf8
Write-Output "Archived five former working trees; verified $verified preserved files and created $($redirects.Count) navigation pointers."
