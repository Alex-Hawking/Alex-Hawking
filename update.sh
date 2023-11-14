#!/bin/bash

# Replace with your Discogs username and token
USERNAME="ah33808"
TOKEN=$1

cat README_template.md > README.md

# Fetch collection data
COLLECTION_URL="https://api.discogs.com/users/$USERNAME/collection/folders/0/releases"
RESPONSE=$(curl -s -H "Authorization: Discogs token=$TOKEN" "$COLLECTION_URL")

# Parse and get a random record
RANDOM_RECORD=$(echo $RESPONSE | jq -r '.releases[] | "\(.basic_information.title) - \(.basic_information.artists[].name)"' | shuf -n 1)

echo $RANDOM_RECORD

DAY=$(date +%A)

# Replace placeholders in a temporary file
sed "s/\${DAY}/$DAY/g" README.md > README_tmp.md
sed "s/\${RANDOM_RECORD}/$RANDOM_RECORD/g" README_tmp.md > README.md

# Clean up the temporary file
rm README_tmp.md