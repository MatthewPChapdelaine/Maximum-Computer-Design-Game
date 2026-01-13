#!/bin/bash
# Installation script for systems that can't use .deb packages

set -e

echo "Installing Maximum PC Builder..."

# Check for Python 3
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is required but not installed."
    echo "Please install Python 3 first:"
    echo "  Ubuntu/Debian: sudo apt-get install python3 python3-tk"
    echo "  Fedora: sudo dnf install python3 python3-tkinter"
    echo "  Arch: sudo pacman -S python tk"
    exit 1
fi

# Check for Tkinter
if ! python3 -c "import tkinter" 2>/dev/null; then
    echo "Error: Tkinter is required but not installed."
    echo "Please install Tkinter:"
    echo "  Ubuntu/Debian: sudo apt-get install python3-tk"
    echo "  Fedora: sudo dnf install python3-tkinter"
    echo "  Arch: sudo pacman -S tk"
    exit 1
fi

# Create installation directories
sudo mkdir -p /usr/share/maximum-pc-builder
sudo mkdir -p /usr/share/applications
sudo mkdir -p /usr/share/pixmaps

# Copy game files
echo "Copying game files..."
sudo cp src/maximum_pc_game.py /usr/share/maximum-pc-builder/
sudo chmod 644 /usr/share/maximum-pc-builder/maximum_pc_game.py

# Create launcher script
echo "Creating launcher..."
sudo tee /usr/bin/maximum-pc-builder > /dev/null << 'EOF'
#!/bin/bash
python3 /usr/share/maximum-pc-builder/maximum_pc_game.py "$@"
EOF
sudo chmod 755 /usr/bin/maximum-pc-builder

# Install desktop file
echo "Installing desktop entry..."
sudo cp maximum-pc-builder.desktop /usr/share/applications/
sudo chmod 644 /usr/share/applications/maximum-pc-builder.desktop

# Create simple icon if imagemagick is available
if command -v convert &> /dev/null; then
    echo "Creating icon..."
    convert -size 256x256 xc:transparent \
        -font "DejaVu-Sans-Bold" -pointsize 48 -fill '#00ff00' \
        -gravity center -annotate +0+0 "MAX\nPC" \
        /tmp/maximum-pc-builder.png 2>/dev/null || true
    
    if [ -f /tmp/maximum-pc-builder.png ]; then
        sudo mv /tmp/maximum-pc-builder.png /usr/share/pixmaps/maximum-pc-builder.png
        sudo chmod 644 /usr/share/pixmaps/maximum-pc-builder.png
    fi
fi

# Update desktop database
if command -v update-desktop-database &> /dev/null; then
    sudo update-desktop-database
fi

echo ""
echo "✓ Installation complete!"
echo ""
echo "You can now run the game by:"
echo "  1. Searching for 'Maximum PC Builder' in your application menu"
echo "  2. Running 'maximum-pc-builder' in a terminal"
echo ""
