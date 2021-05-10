#Requires -Version 7

$ErrorActionPreference = "Stop"

$env:PYTHONPATH = $PSScriptRoot

Get-ChildItem $PSScriptRoot\code\*.py | ForEach-Object -Parallel {
    python $_.FullName
    if ($LASTEXITCODE -ne 0) {
        throw "$_.FullName failed"
    }
}

python -m black .
if ($LASTEXITCODE -ne 0) {
    throw "format failed"
}
