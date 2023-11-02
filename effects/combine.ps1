# Define the output file
$outputFile = "combined.txt"

# Remove the output file if it already exists
if (Test-Path $outputFile) {
    Remove-Item $outputFile
}

# Define the list of files
# $files = @("my_error.py", "my_result.py", "return_result.py", "test_both.py")

$files = @(
    "my_error.py",
    "type_union.py",
    "my_result.py",
    "return_result.py",
    "test_both.py",
    "operations.py",
    "flatmap.py"
)

# Define the separator line with newlines
$separator = "`n" + "-" * 40 

# Loop through each file and append its content to the output file, followed by the separator
foreach ($file in $files) {
    $content = Get-Content $file
    Add-Content -Path $outputFile -Value $content
    Add-Content -Path $outputFile -Value $separator
}
