#!/bin/bash

echo "Shutting down docker image..."
docker compose -f docker-compose.prod.yml down || true # ensures it passes even if no sessions exist

#git fetch and reset
git fetch && git reset origin/main --hard

#rebuild the docker image
echo "Restarting Flask Server..."
docker compose -f docker-compose.prod.yml up -d --build

echo "Flask server should be up!"
