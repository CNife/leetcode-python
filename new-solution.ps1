Param([String] $Title)

$Title = $Title.Trim()
$Title = $Title -replace '-', '_'

if ($Title -match '_(i{1,3})$')
{
    $Title = $Title -replace '_(i{1,3})$', "_$( $Matches[1].Length )"
}
$Title = $Title -replace '_iv$', '_4'
$Title = $Title -replace '_v$', '_5'

$SolutionPath = "$PSScriptRoot\code\$Title.py"
Write-Host "`n" > $SolutionPath
pycharm $SolutionPath
