#!/bin/bash
echo "Setting up Python environment..."

python3 -m venv env
source env/bin/activate

pip install -r requirements.txt

echo "✅ Environment ready. Run 'source env/bin/activate' to start."
