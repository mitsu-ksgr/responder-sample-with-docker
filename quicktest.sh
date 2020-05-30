#!/bin/bash
#
# quick test
#
set -eu

URL="http://localhost:8080"

echo "---------- Responder Sample App ----------"
echo "URL: ${URL}"

echo -e "\n\nTest: '/'"
curl ${URL}

echo -e "\n\nTest: '/hello/mitsu'"
curl "${URL}/hello/mitsu"

echo -e "\n\nTest: '/hello/mitsu/json'"
curl "${URL}/hello/mitsu/json"

echo -e "\n\nTest: '/hello/mitsu/html'"
curl "${URL}/hello/mitsu/html"

echo -e "\n\nTest: '/416'"
curl -D - "${URL}/416"

echo -e "\n\nTest: '/pizza'"
curl -D - "${URL}/pizza"


echo -e "\n\nTest: '/incoming'"
curl -X POST -d "" "${URL}/incoming"

echo -e "\n\nTest: '/file'"
curl -X POST -F 'file=@Dockerfile' "${URL}/file"

echo -e "\n\n\ndone."

