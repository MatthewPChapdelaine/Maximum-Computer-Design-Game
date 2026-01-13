#!/bin/bash
# Uninstallation script

echo "Uninstalling Maximum PC Builder..."

# Remove files
sudo rm -f /usr/bin/maximum-pc-builder
sudo rm -rf /usr/share/maximum-pc-builder
sudo rm -f /usr/share/applications/maximum-pc-builder.desktop
sudo rm -f /usr/share/pixmaps/maximum-pc-builder.png

# Update desktop database
if command -v update-desktop-database &> /dev/null; then
    sudo update-desktop-database
fi

echo ""
echo "✓ Uninstallation complete!"
echo ""
echo "Your save file remains at: ~/.maximum_pc_game_save.json"
echo "Delete it manually if you want to remove your saved games."
echo ""
