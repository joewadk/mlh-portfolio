#!/bin/bash

echo "Killing all tmux servers..."
tmux kill-server || true # ensures it passes even if no sessions exist

#git fetch and reset
git fetch && git reset origin/main --hard

#venv
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
deactivate # exit venv before tmux session

#new detached tmux session and run flask
echo "Restarting Flask Server..."
tmux new-session -d -s "flask-server" "cd $(pwd) && source .venv/bin/activate && export FLASK_ENV=production && flask run --host=0.0.0.0 --port=5000"

echo "Flask server should be up!"
