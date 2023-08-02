# $setDir = @"
#     Set-Location -Path "C:\tools"
# "@

# $javaCommand = @"
# java "-Djdk.util.jar.enableMultiRelease=false" -jar structurizr-lite-3087.war C:\git\python-experiments\C4-DSL
# "@

# $dockerCommand = @"
# docker pull structurizr/lite
# docker run -it --rm -p 8080:8080 -v C:/git/python-experiments/C4-DSL:/usr/local/structurizr structurizr/lite
# "@

# Invoke-Expression -Command $dockerCommand

$podmanCommand = @"
podman pull structurizr/lite
podman run -it --rm -p 8080:8080 -v C:/git/python-experiments/C4-DSL:/usr/local/structurizr structurizr/lite
"@

Invoke-Expression -Command $podmanCommand
