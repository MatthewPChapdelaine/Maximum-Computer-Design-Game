#!/bin/bash
# Quick Start Script for Maximum PC Builder
# This script helps new users get started quickly

echo "╔═══════════════════════════════════════════════════════════╗"
echo "║     Maximum Performance PC Builder - Quick Start         ║"
echo "╚═══════════════════════════════════════════════════════════╝"
echo ""

# Check if already installed
if command -v maximum-pc-builder &> /dev/null; then
    echo "✓ Game is already installed!"
    echo ""
    echo "Choose an option:"
    echo "  1) Launch the game"
    echo "  2) View documentation"
    echo "  3) Uninstall"
    echo "  4) Exit"
    echo ""
    read -p "Enter choice [1-4]: " choice
    
    case $choice in
        1)
            echo "Launching game..."
            maximum-pc-builder
            exit 0
            ;;
        2)
            echo ""
            echo "Documentation files:"
            echo "  README.md - Main documentation"
            echo "  GAME_GUIDE.md - Gameplay guide"
            echo "  TESTING.md - Installation & testing"
            echo ""
            read -p "Which file to view? [README/GAME_GUIDE/TESTING]: " doc
            case $doc in
                GAME_GUIDE)
                    less GAME_GUIDE.md 2>/dev/null || cat GAME_GUIDE.md
                    ;;
                TESTING)
                    less TESTING.md 2>/dev/null || cat TESTING.md
                    ;;
                *)
                    less README.md 2>/dev/null || cat README.md
                    ;;
            esac
            exit 0
            ;;
        3)
            ./uninstall.sh
            exit 0
            ;;
        *)
            echo "Goodbye!"
            exit 0
            ;;
    esac
fi

# Not installed - show installation options
echo "Game is not installed yet."
echo ""
echo "Choose installation method:"
echo "  1) Build and install .deb package (Debian/Ubuntu/Mint)"
echo "  2) Manual installation (All Linux distros)"
echo "  3) Run from source (No installation)"
echo "  4) View documentation first"
echo "  5) Exit"
echo ""
read -p "Enter choice [1-5]: " choice

case $choice in
    1)
        echo ""
        echo "Building .deb package..."
        echo ""
        
        # Check for dpkg-deb
        if ! command -v dpkg-deb &> /dev/null; then
            echo "Error: dpkg-deb not found. Installing..."
            sudo apt-get update && sudo apt-get install -y dpkg
        fi
        
        # Make executable and build
        chmod +x build-deb.sh
        ./build-deb.sh
        
        if [ $? -eq 0 ]; then
            echo ""
            echo "Package built successfully!"
            echo ""
            read -p "Install now? [Y/n]: " install_now
            
            if [[ $install_now != "n" && $install_now != "N" ]]; then
                echo "Installing..."
                sudo dpkg -i maximum-pc-builder_1.0.0.deb
                
                if [ $? -ne 0 ]; then
                    echo "Fixing dependencies..."
                    sudo apt-get install -f -y
                fi
                
                echo ""
                echo "✓ Installation complete!"
                echo "Launch with: maximum-pc-builder"
                echo "Or find it in your application menu."
            fi
        else
            echo "Build failed. Please check error messages above."
        fi
        ;;
    
    2)
        echo ""
        echo "Running manual installation..."
        echo ""
        
        # Check dependencies first
        if ! command -v python3 &> /dev/null; then
            echo "Error: Python 3 is required."
            echo "Install with: sudo apt-get install python3 python3-tk"
            exit 1
        fi
        
        if ! python3 -c "import tkinter" 2>/dev/null; then
            echo "Error: Tkinter is required."
            echo "Install with: sudo apt-get install python3-tk"
            exit 1
        fi
        
        chmod +x install.sh
        ./install.sh
        
        if [ $? -eq 0 ]; then
            echo ""
            echo "✓ Installation complete!"
            echo "Launch with: maximum-pc-builder"
        fi
        ;;
    
    3)
        echo ""
        echo "Running from source..."
        echo ""
        
        # Check dependencies
        if ! command -v python3 &> /dev/null; then
            echo "Error: Python 3 is required."
            exit 1
        fi
        
        if ! python3 -c "import tkinter" 2>/dev/null; then
            echo "Error: Tkinter is required."
            echo "Install with: sudo apt-get install python3-tk"
            exit 1
        fi
        
        chmod +x run-game.sh
        ./run-game.sh
        ;;
    
    4)
        echo ""
        echo "Opening README.md..."
        echo ""
        less README.md 2>/dev/null || cat README.md
        echo ""
        echo "Press Enter to continue..."
        read
        $0  # Restart script
        ;;
    
    *)
        echo "Goodbye!"
        exit 0
        ;;
esac

exit 0
