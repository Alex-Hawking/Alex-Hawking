#!/bin/bash

# Replace with your Discogs username and token
USERNAME="ah33808"
TOKEN=$1

# Fetch collection data
COLLECTION_URL="https://api.discogs.com/users/$USERNAME/collection/folders/0/releases"
RESPONSE=$(curl -s -H "Authorization: Discogs token=$TOKEN" "$COLLECTION_URL")

# Parse and get a random record
RANDOM_RECORD=$(echo $RESPONSE | jq -r '.releases[] | "\(.basic_information.title) - \(.basic_information.artists[].name)"' | shuf -n 1)
DAY=$(date +%A)

cat README.md | sed "s/\\${DAY}/$DAY/g; s/\\${RANDOM_RECORD}/$RANDOM_RECORD/g" > README.md
