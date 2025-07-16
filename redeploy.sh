#!/bin/bash

echo "Killing all systemctl servers..."
sudo systemctl stop myportfolio || true # ensures it passes even if no sessions exist

#git fetch and reset
git fetch && git reset origin/main --hard

#venv
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
deactivate # exit venv before restarting systemctl service

#restart systemctl and run flask server
echo "Restarting Flask Server..."
sudo systemctl daemon-reload
sudo systemctl restart myportfolio
sudo systemctl enable myportfolio

echo "Flask server should be up!"
