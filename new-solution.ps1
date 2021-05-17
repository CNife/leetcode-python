Param([String] $Title)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"


$Title = $Title.Trim()
$Title = $Title -replace '-', '_'

if ($Title -match '_(i{1,3})$')
{
    $Title = $Title -replace '_(i{1,3})$', "_$( $Matches[1].Length )"
}
$Title = $Title -replace '_iv$', '_4'
$Title = $Title -replace '_v$', '_5'

if ($Title.Length -lt 1) {
    throw "空的题解名"
}

$SolutionPath = "$PSScriptRoot\code\$Title.py"
Write-Output "`n" | Out-File $SolutionPath
pycharm $PSScriptRoot $SolutionPath
