# Change cwd:
Set-Location -Path "C:\tools"

$javaCommand = @"
java "-Djdk.util.jar.enableMultiRelease=false" -jar structurizr-lite-3087.war C:\git\python-experiments\C4-DSL
"@

Invoke-Expression -Command $javaCommand
