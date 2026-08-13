[CmdletBinding(SupportsShouldProcess = $true)]
param(
    [datetime]$AsOfDate = (Get-Date).Date
)

$ErrorActionPreference = 'Stop'

$repositoryRoot = Split-Path -Parent $PSScriptRoot
$tailoredRoot = Join-Path $repositoryRoot 'resumes\tailored'
$archiveRoot = Join-Path $tailoredRoot 'old'

if (-not (Test-Path -LiteralPath $tailoredRoot -PathType Container)) {
    throw "Tailored resume directory not found: $tailoredRoot"
}

$datePattern = '(?<date>\d{4}-\d{2}-\d{2})$'
$culture = [System.Globalization.CultureInfo]::InvariantCulture
$archived = [System.Collections.Generic.List[string]]::new()
$skippedCurrent = [System.Collections.Generic.List[string]]::new()
$skippedUndated = [System.Collections.Generic.List[string]]::new()

$variantDirectories = Get-ChildItem -LiteralPath $tailoredRoot -Directory |
    Where-Object { $_.Name -ne 'old' } |
    Sort-Object Name

foreach ($variantDirectory in $variantDirectories) {
    $match = [regex]::Match($variantDirectory.Name, $datePattern)
    if (-not $match.Success) {
        $skippedUndated.Add($variantDirectory.Name)
        continue
    }

    $variantDate = [datetime]::ParseExact(
        $match.Groups['date'].Value,
        'yyyy-MM-dd',
        $culture
    ).Date

    if ($variantDate -ge $AsOfDate.Date) {
        $skippedCurrent.Add($variantDirectory.Name)
        continue
    }

    $archiveDateName = $variantDate.ToString('dd-MM.yyyy', $culture)
    $dateArchiveDirectory = Join-Path $archiveRoot $archiveDateName
    $destination = Join-Path $dateArchiveDirectory $variantDirectory.Name

    if (Test-Path -LiteralPath $destination) {
        throw "Archive collision; destination already exists: $destination"
    }

    if ($PSCmdlet.ShouldProcess($variantDirectory.FullName, "Move to $destination")) {
        if (-not (Test-Path -LiteralPath $dateArchiveDirectory -PathType Container)) {
            New-Item -ItemType Directory -Path $dateArchiveDirectory -Force | Out-Null
        }
        Move-Item -LiteralPath $variantDirectory.FullName -Destination $destination
        $archived.Add($destination)
    }
}

[PSCustomObject]@{
    AsOfDate = $AsOfDate.ToString('yyyy-MM-dd', $culture)
    ArchivedCount = $archived.Count
    Archived = @($archived)
    CurrentDayCount = $skippedCurrent.Count
    CurrentDay = @($skippedCurrent)
    UndatedCount = $skippedUndated.Count
    Undated = @($skippedUndated)
} | ConvertTo-Json -Depth 4
