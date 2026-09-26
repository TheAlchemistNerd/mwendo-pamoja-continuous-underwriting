$ErrorActionPreference = 'Stop'
$workspaceRoot = [IO.Path]::GetFullPath((Join-Path $PSScriptRoot '../../../..'))
$downloadsRoot = Split-Path -Parent $workspaceRoot
$archiveRoot = Join-Path $workspaceRoot '_archive/repository_migration_2026-09-26'
$stageRoot = Join-Path $archiveRoot 'staging'
$names = @('bayesian-telematics-relativities', 'regtech-kesonia-treasury')
$underwriteRoot = Join-Path $downloadsRoot 'behavioural credit scoring - underwrite to collect rct'
$innerRoot = Join-Path $workspaceRoot 'behavioural credit scoring - underwrite to collect rct'

function Assert-Within([string]$Path, [string]$Boundary) {
    $resolved = [IO.Path]::GetFullPath($Path)
    $allowed = [IO.Path]::GetFullPath($Boundary).TrimEnd('\') + '\'
    if (-not $resolved.StartsWith($allowed, [StringComparison]::OrdinalIgnoreCase)) {
        throw "Path outside intended boundary: $resolved"
    }
    return $resolved
}
function Get-Digest([string]$Path) {
    (Get-FileHash -LiteralPath ('\\?\' + [IO.Path]::GetFullPath($Path)) -Algorithm SHA256).Hash.ToLowerInvariant()
}
function Assert-NoJunction([string]$Path) {
    if (((Get-Item -LiteralPath $Path -Force).Attributes -band [IO.FileAttributes]::ReparsePoint) -ne 0) {
        throw "Unexpected junction or symbolic link: $Path"
    }
}

$manifest = Get-Content -LiteralPath (Join-Path $PSScriptRoot 'transfer_manifest.json') -Raw | ConvertFrom-Json
$stageHashes = Get-Content -LiteralPath (Join-Path $PSScriptRoot 'staged_hashes.json') -Raw | ConvertFrom-Json -AsHashtable
foreach ($name in $names) {
    $target = Assert-Within (Join-Path $downloadsRoot $name) $downloadsRoot
    if (Test-Path -LiteralPath $target) { throw "Destination already exists: $target" }
    Assert-NoJunction (Join-Path $stageRoot $name)
}
foreach ($entry in $manifest.files) {
    if ((Get-Digest $entry.source) -ne $entry.source_sha256) { throw "Source changed after preparation: $($entry.source)" }
}
foreach ($entry in $stageHashes.GetEnumerator()) {
    if ((Get-Digest (Join-Path $stageRoot $entry.Key)) -ne $entry.Value) { throw "Staged file changed: $($entry.Key)" }
}
$oldSeries = Assert-Within (Join-Path $underwriteRoot 'source_library/series') $underwriteRoot
$newSeries = Assert-Within (Join-Path $underwriteRoot 'series') $underwriteRoot
Assert-NoJunction $underwriteRoot
Assert-NoJunction $oldSeries
if (Test-Path -LiteralPath $newSeries) { throw 'Root series already exists; reconcile manually.' }
foreach ($property in $manifest.underwrite.standalone_logical_hashes.PSObject.Properties) {
    $relative = $property.Name
    if ($relative.StartsWith('series/')) { $relative = 'source_library/' + $relative }
    if ((Get-Digest (Join-Path $underwriteRoot $relative)) -ne $property.Value) { throw "Underwrite changed: $relative" }
}

# Copy and verify the new snapshots before any source relocation.
foreach ($name in $names) {
    Copy-Item -LiteralPath (Join-Path $stageRoot $name) -Destination (Join-Path $downloadsRoot $name) -Recurse
}
foreach ($entry in $stageHashes.GetEnumerator()) {
    if ((Get-Digest (Join-Path $downloadsRoot $entry.Key)) -ne $entry.Value) { throw "Installed file differs: $($entry.Key)" }
}

# Both absolute paths were checked above. Preserve the actual working files.
Move-Item -LiteralPath $oldSeries -Destination $newSeries
foreach ($relative in $manifest.underwrite.inner_only) {
    $source = Assert-Within (Join-Path $innerRoot $relative) $innerRoot
    $target = Assert-Within (Join-Path $underwriteRoot $relative) $underwriteRoot
    if (Test-Path -LiteralPath $target) { throw "Refusing to overwrite: $target" }
    New-Item -ItemType Directory -Path (Split-Path -Parent $target) -Force | Out-Null
    Copy-Item -LiteralPath $source -Destination $target
    if ((Get-Digest $source) -ne (Get-Digest $target)) { throw "Underwrite transfer differs: $relative" }
}
$buildPath = Join-Path $newSeries 'build/build_whitepaper_pdf.ps1'
$buildText = [IO.File]::ReadAllText($buildPath)
$oldLine = '$projectRoot = Split-Path -Parent (Split-Path -Parent $seriesRoot)'
if (-not $buildText.Contains($oldLine)) { throw 'Unexpected Underwrite build-root expression.' }
[IO.File]::WriteAllText($buildPath, $buildText.Replace($oldLine, '$projectRoot = Split-Path -Parent $seriesRoot'), [Text.UTF8Encoding]::new($false))
$note = @'
# Underwrite repository reconciliation — 26 September 2026

The existing standalone repository is the authoritative working tree. The active manuscripts have been restored from `source_library/series/` to the Git-tracked `series/` layout. Frozen comparator material elsewhere in `source_library/` is preserved.

Three newer items were transferred from the ignored Mwendo integration copy: the additional pricing review, the collectability/re-verification feedback review, and its source image. Shared content was compared by SHA-256 before relocation. The standalone historical snapshots and hash list were retained, including its two additional snapshot manuscripts. The inner copy's path-specific hash list is preserved in the Mwendo archive.

The PDF build's project-root calculation now uses the parent of `series`, keeping scratch output inside this repository. No manuscript prose or research claims were rewritten by the layout repair.

Full pre-migration Git history, the original relocated series, and the retired integration copy are preserved under `C:/Users/Nevo/Downloads/insuretech & embedded finance/_archive/repository_migration_2026-09-26/`. The detailed comparison and transfer manifest are in the parent project's `docs/governance/migrations/2026-09-26/`.

Use this repository for subsequent Underwrite changes. Guest financial-material and business/blog website repositories were outside the migration's write boundary.
'@
[IO.File]::WriteAllText((Join-Path $underwriteRoot 'MIGRATION_2026-09-26.md'), $note + "`n", [Text.UTF8Encoding]::new($false))
$readme = Join-Path $underwriteRoot 'README.md'
[IO.File]::AppendAllText($readme, "`n## Repository reconciliation`n`nThe standalone repository is now the authoritative working location. See [the migration record](MIGRATION_2026-09-26.md) for the restored series layout and transferred reviews.`n", [Text.UTF8Encoding]::new($false))
Write-Output "Verified $($stageHashes.Count) staged files in two sibling folders; restored Underwrite series and transferred three items."
