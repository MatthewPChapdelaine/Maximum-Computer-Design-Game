#!/bin/bash
# Quick run script for development and testing

echo "🎮 Starting Maximum PC Builder Game..."
echo ""

# Check if python3 is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: python3 is not installed"
    echo "Please install Python 3: sudo apt-get install python3"
    exit 1
fi

# Check if tkinter is available
if ! python3 -c "import tkinter" &> /dev/null; then
    echo "❌ Error: python3-tk is not installed"
    echo "Please install Tkinter: sudo apt-get install python3-tk"
    exit 1
fi

# Run the game
python3 src/maximum_pc_game.py

exit 0
