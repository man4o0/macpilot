#!/bin/bash

echo "🍎 Installing macpilot..."

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

chmod +x macpilot.py
sudo ln -s $(pwd)/macpilot.py /usr/local/bin/macpilot

echo "✅ Installed successfully!"
echo ""

