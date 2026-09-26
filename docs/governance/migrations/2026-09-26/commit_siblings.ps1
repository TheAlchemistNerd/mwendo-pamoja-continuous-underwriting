$ErrorActionPreference = 'Stop'
$workspaceRoot = [IO.Path]::GetFullPath((Join-Path $PSScriptRoot '../../../..'))
$downloadsRoot = Split-Path -Parent $workspaceRoot
function Run-Git([string]$Directory, [string[]]$Arguments) {
    & git -C $Directory @Arguments
    if ($LASTEXITCODE -ne 0) { throw "git failed in $Directory" }
}
$commits = @()
foreach ($name in @('bayesian-telematics-relativities','regtech-kesonia-treasury')) {
    $repository = Join-Path $downloadsRoot $name
    $initialized = Test-Path -LiteralPath (Join-Path $repository '.git')
    if ($initialized) {
        & git -C $repository rev-parse --verify HEAD 2>$null | Out-Null
        if ($LASTEXITCODE -eq 0) { throw "Repository already has a commit: $repository" }
        $branch = & git -C $repository symbolic-ref --short HEAD
        if ($branch -ne 'codex/repository-separation') { throw 'Unexpected initial branch.' }
    }
    foreach ($required in @('README.md','MIGRATION.md','MIGRATION_MANIFEST.json','MIGRATION_VALIDATION.json')) {
        if (-not (Test-Path -LiteralPath (Join-Path $repository $required))) { throw "Missing $required in $repository" }
    }
    if (-not $initialized) { Run-Git $repository @('init','-b','codex/repository-separation') }
    Run-Git $repository @('config','core.autocrlf','false')
    Run-Git $repository @('config','core.longpaths','true')
    # Both repositories are new, purpose-built snapshots with no prior index or user work.
    $paths = @('.gitignore','README.md','MIGRATION.md','MIGRATION_MANIFEST.json','MIGRATION_VALIDATION.json','SOURCE_HISTORY.txt')
    if ($name -eq 'bayesian-telematics-relativities') { $paths += @('whitepapers','publications') }
    else { $paths += @('docs','output') }
    Run-Git $repository (@('add','--')+$paths)
    # Preserve imported source bytes, including existing line endings and Markdown
    # hard breaks. Whitespace normalization is outside this snapshot migration.
    Run-Git $repository @('commit','-m','Establish standalone research repository from verified working snapshot')
    $commits += @{ Repository = $repository; Commit = (& git -C $repository rev-parse HEAD); Branch = (& git -C $repository branch --show-current) }
}
$underwriteRoot = Join-Path $downloadsRoot 'behavioural credit scoring - underwrite to collect rct'
$staged = & git -C $underwriteRoot diff --cached --name-only
if ($staged) { throw 'Underwrite contains pre-existing staged changes; scoped commit refused.' }
Run-Git $underwriteRoot @('switch','-c','codex/repository-separation')
$underwritePaths = @('README.md','MIGRATION_2026-09-26.md','series/build/build_whitepaper_pdf.ps1',
    'series/research/ADDITIONAL_PRICING_REVIEW_AND_CONTENT_PLAN_2026-09-25.md',
    'series/research/COLLECTABILITY_FEEDBACK_AND_CONTINUOUS_REVERIFICATION_2026-09-25.md',
    'series/research/feedback_sources/underwrite_collection_reader_feedback_2026-09-25.jpg')
Run-Git $underwriteRoot (@('add','--')+$underwritePaths)
Run-Git $underwriteRoot @('commit','-m','Reconcile standalone Underwrite layout and preserve new research feedback')
$commits += @{ Repository = $underwriteRoot; Commit = (& git -C $underwriteRoot rev-parse HEAD); Branch = (& git -C $underwriteRoot branch --show-current) }
$commits | ConvertTo-Json -Depth 4 | Set-Content -LiteralPath (Join-Path $PSScriptRoot 'sibling_commits.json') -Encoding utf8
Write-Output 'Created three scoped local commits. No remote was created or pushed.'
