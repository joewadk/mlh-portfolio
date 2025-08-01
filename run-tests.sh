
#!/bin/bash
set -e
echo "Running tests..."
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m unittest discover -v tests
echo "All tests passed! Yippie!!!"
