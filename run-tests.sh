#!/bin/bash
set -e
echo "Running tests..."
python -m unittest discover -v tests
echo "All tests passed! Yippie!!!"