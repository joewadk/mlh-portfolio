#!/bin/bash

URL="http://localhost:5000/api/timeline" #url to be called later

NAME="Testuser"
EMAIL="testscript@mlh"
CONTENT="Hi. This is a test post from bash"

echo "Posting a timeline entry"
curl -s -X POST "$URL" \
	-d "name=$NAME" \
	-d "email=$EMAIL" \
	-d "content=$CONTENT" > /dev/null #dont need the output so throw away
echo "Getting timeline entry"
RESPONSE=$(curl -s -X GET "$URL")


if echo "$RESPONSE" | grep -Fq "$CONTENT"; then
	echo "Content matches!"
else
	echo "Content does not match!"
	exit 1
fi
