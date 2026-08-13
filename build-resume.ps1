<#
.SYNOPSIS
Builds the root resume, refreshes portfolio assets, validates the portfolio,
and commits/pushes the assets to trigger the GitHub Pages workflow.

.EXAMPLE
.\build-resume.ps1

.EXAMPLE
.\build-resume.ps1 -SkipPush

.EXAMPLE
.\build-resume.ps1 -SkipGit
#>

param(
    [string]$PortfolioPath = "D:\Development\portfolio",
    [string]$CommitMessage = "Update portfolio resume assets",
    [switch]$SkipGit,
    [switch]$SkipPush
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

function Invoke-CheckedCommand {
    param(
        [Parameter(Mandatory = $true)]
        [string]$Command,

        [Parameter(Mandatory = $true)]
        [string[]]$Arguments,

        [Parameter(Mandatory = $true)]
        [string]$WorkingDirectory
    )

    Push-Location -LiteralPath $WorkingDirectory
    try {
        & $Command @Arguments
        if ($LASTEXITCODE -ne 0) {
            throw "$Command failed with exit code $LASTEXITCODE."
        }
    }
    finally {
        Pop-Location
    }
}

function Assert-CommandExists {
    param([Parameter(Mandatory = $true)][string]$Name)

    if (-not (Get-Command $Name -ErrorAction SilentlyContinue)) {
        throw "Required command '$Name' was not found in PATH."
    }
}

$ResumeDirectory = $PSScriptRoot
$ResumeTex = Join-Path $ResumeDirectory "resume.tex"
$ResumePdf = Join-Path $ResumeDirectory "resume.pdf"
$TempDirectory = Join-Path $ResumeDirectory "tmp\pdfs\portfolio-resume"
$TempPreviewPrefix = Join-Path $TempDirectory "resume-page-1"
$TempPreview = "$TempPreviewPrefix.png"

$PortfolioPublic = Join-Path $PortfolioPath "public"
$PortfolioPdf = Join-Path $PortfolioPublic "Kunal_Maheshwari_Resume.pdf"
$PortfolioPreviewDirectory = Join-Path $PortfolioPublic "resume-pages"
$PortfolioPreview = Join-Path $PortfolioPreviewDirectory "resume-page-1.png"

Assert-CommandExists "pdflatex"
Assert-CommandExists "pdfinfo"
Assert-CommandExists "pdftoppm"
Assert-CommandExists "npm.cmd"
Assert-CommandExists "git"

if (-not (Test-Path -LiteralPath $ResumeTex -PathType Leaf)) {
    throw "Resume source was not found: $ResumeTex"
}

if (-not (Test-Path -LiteralPath $PortfolioPath -PathType Container)) {
    throw "Portfolio repository was not found: $PortfolioPath"
}

if (-not (Test-Path -LiteralPath (Join-Path $PortfolioPath ".git") -PathType Container)) {
    throw "Portfolio path is not a Git repository: $PortfolioPath"
}

New-Item -ItemType Directory -Path $TempDirectory -Force | Out-Null
New-Item -ItemType Directory -Path $PortfolioPreviewDirectory -Force | Out-Null

Write-Host "[1/4] Compiling resume.tex..."
Invoke-CheckedCommand `
    -Command "pdflatex" `
    -Arguments @("-interaction=nonstopmode", "-halt-on-error", "-output-directory=$ResumeDirectory", $ResumeTex) `
    -WorkingDirectory $ResumeDirectory

if (-not (Test-Path -LiteralPath $ResumePdf -PathType Leaf)) {
    throw "Expected PDF was not generated: $ResumePdf"
}

$PdfInfo = & pdfinfo $ResumePdf
if ($LASTEXITCODE -ne 0) {
    throw "pdfinfo failed with exit code $LASTEXITCODE."
}

$PageLine = $PdfInfo | Where-Object { $_ -match "^Pages:\s+(\d+)\s*$" } | Select-Object -First 1
if (-not $PageLine) {
    throw "Could not determine the generated PDF page count."
}

$PageCount = [int]([regex]::Match($PageLine, "^Pages:\s+(\d+)\s*$").Groups[1].Value)
if ($PageCount -lt 1 -or $PageCount -gt 2) {
    throw "The resume must remain within the readable 1-2 page policy, but the generated PDF has $PageCount pages."
}

Write-Host "[2/4] Rendering the portfolio preview PNG..."
if (Test-Path -LiteralPath $TempPreview) {
    Remove-Item -LiteralPath $TempPreview -Force
}

Invoke-CheckedCommand `
    -Command "pdftoppm" `
    -Arguments @("-png", "-r", "180", "-f", "1", "-l", "1", "-singlefile", $ResumePdf, $TempPreviewPrefix) `
    -WorkingDirectory $ResumeDirectory

if (-not (Test-Path -LiteralPath $TempPreview -PathType Leaf)) {
    throw "Expected preview PNG was not generated: $TempPreview"
}

Write-Host "[3/4] Updating portfolio assets and validating the build..."
Copy-Item -LiteralPath $ResumePdf -Destination $PortfolioPdf -Force
Copy-Item -LiteralPath $TempPreview -Destination $PortfolioPreview -Force

$SourcePdfHash = (Get-FileHash -Algorithm SHA256 -LiteralPath $ResumePdf).Hash
$PortfolioPdfHash = (Get-FileHash -Algorithm SHA256 -LiteralPath $PortfolioPdf).Hash
if ($SourcePdfHash -ne $PortfolioPdfHash) {
    throw "The copied portfolio PDF does not match the generated resume PDF."
}

$SourcePreviewHash = (Get-FileHash -Algorithm SHA256 -LiteralPath $TempPreview).Hash
$PortfolioPreviewHash = (Get-FileHash -Algorithm SHA256 -LiteralPath $PortfolioPreview).Hash
if ($SourcePreviewHash -ne $PortfolioPreviewHash) {
    throw "The copied portfolio preview does not match the rendered PNG."
}

Remove-Item -LiteralPath $TempPreview -Force

Invoke-CheckedCommand `
    -Command "npm.cmd" `
    -Arguments @("run", "build") `
    -WorkingDirectory $PortfolioPath

if ($SkipGit) {
    Write-Host "Resume assets were built and copied. Git commit and push were skipped because -SkipGit was supplied."
    return
}

Write-Host "[4/4] Committing portfolio resume assets..."
Push-Location -LiteralPath $PortfolioPath
try {
    $ResumeAssetPaths = @(
        "public/Kunal_Maheshwari_Resume.pdf",
        "public/resume-pages/resume-page-1.png"
    )

    $PreviouslyStagedFiles = @(
        & git diff --cached --name-only --no-renames --no-ext-diff --no-textconv --
    )
    if ($LASTEXITCODE -ne 0) {
        throw "Could not inspect the existing Git index."
    }

    $UnexpectedStagedFiles = @(
        $PreviouslyStagedFiles | Where-Object { $_ -notin $ResumeAssetPaths }
    )
    if ($UnexpectedStagedFiles.Count -gt 0) {
        throw "The portfolio repository has unrelated staged changes: $($UnexpectedStagedFiles -join ', '). Commit or unstage them before running this script."
    }

    & git add -- $ResumeAssetPaths
    if ($LASTEXITCODE -ne 0) {
        throw "git add failed with exit code $LASTEXITCODE."
    }

    # Git for Windows may invoke astextplain for PDFs unless text conversion is
    # disabled. That helper can fail to fork even though the staged files are valid.
    & git diff --cached --quiet --no-ext-diff --no-textconv -- $ResumeAssetPaths
    $DiffExitCode = $LASTEXITCODE

    if ($DiffExitCode -eq 0) {
        Write-Host "No resume asset changes were detected. Nothing to commit or push."
        return
    }

    if ($DiffExitCode -ne 1) {
        throw "git diff failed with exit code $DiffExitCode."
    }

    & git commit -m $CommitMessage
    if ($LASTEXITCODE -ne 0) {
        throw "git commit failed with exit code $LASTEXITCODE."
    }

    if ($SkipPush) {
        Write-Host "Commit created. Push skipped because -SkipPush was supplied."
        return
    }

    $CurrentBranch = (& git branch --show-current).Trim()
    if ($LASTEXITCODE -ne 0 -or -not $CurrentBranch) {
        throw "Could not determine the current Git branch."
    }

    & git push origin $CurrentBranch
    if ($LASTEXITCODE -ne 0) {
        throw "git push failed with exit code $LASTEXITCODE."
    }

    Write-Host "Resume assets pushed successfully. GitHub Pages deployment should start automatically."
}
finally {
    Pop-Location
}
