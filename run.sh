#!/bin/bash

echo "=========================================="
echo "      SETTING UP & STARTING BUGING        "
echo "=========================================="

# 1. Check if python3 is installed
if ! command -v python3 &> /dev/null
then
    echo "[!] Python3 is not installed. Please install Python3 first."
    exit
fi

# 2. Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "[*] Creating virtual environment (venv)..."
    python3 -m venv venv
fi

# 3. Activate virtual environment
echo "[*] Activating virtual environment..."
source venv/bin/activate

# 4. Install requirements automatically
echo "[*] Installing required dependencies..."
pip install --upgrade pip > /dev/null 2>&1
pip install -r requirements.txt

# 5. Run the scanner tool
echo "[+] Setup complete! Starting scanner..."
echo "=========================================="
python3 scanner.py
