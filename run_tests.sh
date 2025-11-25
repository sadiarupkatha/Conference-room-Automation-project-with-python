#!/bin/bash
# Linux/Mac script to run tests

echo "Setting up test environment..."
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
echo ""
echo "Running tests..."
pytest --html=reports/report.html --self-contained-html
echo ""
echo "Test report generated at reports/report.html"

