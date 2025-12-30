#!/bin/bash
# Automated virtual environment setup script for Linux/Mac

echo "===================================="
echo "Python Like MATLAB - Environment Setup"
echo "===================================="
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "[ERROR] Python3 is not installed."
    echo "Please install Python 3.7 or higher."
    exit 1
fi

echo "[1/3] Python version check completed"
python3 --version
echo ""

# Create virtual environment
if [ -d "venv" ]; then
    echo "[INFO] Virtual environment already exists."
    read -p "Do you want to delete the existing environment and recreate it? (y/N): " -n 1 -r
    echo ""
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        echo "[INFO] Removing existing virtual environment..."
        rm -rf venv
    else
        echo "[INFO] Using existing virtual environment"
    fi
fi

if [ ! -d "venv" ]; then
    echo "[2/3] Creating virtual environment..."
    python3 -m venv venv
    if [ $? -ne 0 ]; then
        echo "[ERROR] Failed to create virtual environment."
        exit 1
    fi
    echo "[SUCCESS] Virtual environment created successfully."
    echo ""
fi

# Activate virtual environment and install packages
echo "[3/3] Installing packages..."
source venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "[ERROR] Failed to install packages."
    exit 1
fi

echo ""
echo "===================================="
echo "Installation completed successfully!"
echo "===================================="
echo ""
echo "To activate the virtual environment:"
echo "    source venv/bin/activate"
echo ""
echo "Run MATLAB-style interpreter:"
echo "    python matlab_interpreter.py"
echo ""
echo "Run simple MATLAB REPL:"
echo "    python matlab_repl.py"
echo ""
echo "Run Jupyter Notebook:"
echo "    jupyter notebook examples/"
echo ""
