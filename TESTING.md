# Installation and Testing Guide

## Quick Start

### Option 1: Build and Install .deb Package (Recommended for Debian/Ubuntu/Mint)

```bash
# Navigate to the project directory
cd Maximum-Computer-Design-Game

# Make build script executable
chmod +x build-deb.sh

# Build the .deb package
./build-deb.sh

# Install the package
sudo dpkg -i maximum-pc-builder_1.1.0.deb

# If there are dependency issues
sudo apt-get install -f

# Launch the game
maximum-pc-builder
```

### Option 2: Manual Installation (All Linux Distros)

```bash
# Navigate to the project directory
cd Maximum-Computer-Design-Game

# Make install script executable
chmod +x install.sh

# Run installation script
./install.sh

# Launch the game
maximum-pc-builder
```

### Option 3: Run from Source (Development/Testing)

```bash
# Navigate to the project directory
cd Maximum-Computer-Design-Game

# Make run script executable
chmod +x run-game.sh

# Run directly
./run-game.sh

# Or run Python directly
python3 src/maximum_pc_game.py
```

## Prerequisites

### Required Dependencies
- Python 3.8 or higher
- python3-tk (Tkinter)

### Install Dependencies

**Ubuntu/Debian/Linux Mint:**
```bash
sudo apt-get update
sudo apt-get install python3 python3-tk
```

**Fedora:**
```bash
sudo dnf install python3 python3-tkinter
```

**Arch Linux:**
```bash
sudo pacman -S python tk
```

**openSUSE:**
```bash
sudo zypper install python3 python3-tk
```

## Testing Checklist

### Pre-Installation Tests
- [ ] Verify Python 3.8+ is installed: `python3 --version`
- [ ] Verify Tkinter is available: `python3 -c "import tkinter"`
- [ ] Check available disk space: `df -h` (need ~10MB)

### Installation Tests
- [ ] Scripts are executable: `ls -l *.sh`
- [ ] Build script completes without errors
- [ ] .deb package is created
- [ ] Package installs successfully
- [ ] Desktop file is installed: `ls /usr/share/applications/maximum-pc-builder.desktop`
- [ ] Binary is in PATH: `which maximum-pc-builder`

### Game Launch Tests
- [ ] Game launches from terminal: `maximum-pc-builder`
- [ ] Game launches from application menu
- [ ] Window opens with correct title
- [ ] UI elements are visible and properly formatted
- [ ] Dark theme is applied correctly

### Functionality Tests

#### Basic UI Tests
- [ ] All status bars display correctly (Money, Research, Performance, Power)
- [ ] Component list populates
- [ ] Category filter works
- [ ] Component selection works
- [ ] Details panel updates on selection
- [ ] Buttons are visible

#### Resource Tests
- [ ] Starting money is $50,000
- [ ] Starting research points are 100
- [ ] Starting power budget is 2000W
- [ ] Starting performance score is 0
- [ ] Passive income increases money
- [ ] Passive research increases research points
- [ ] Buying the 750W PSU does not drop the power budget (stays >= 2000W)

#### Research Tests
- [ ] Can select unresearched component
- [ ] Research button enables for valid components
- [ ] Research button disables during active research
- [ ] Progress bar updates during research
- [ ] Research completes after specified time
- [ ] Component marked as researched after completion
- [ ] Notification appears on research completion
- [ ] Only one research active at a time
- [ ] Research is blocked when research points are less than the cost
- [ ] Research points are deducted on research start (1 point per second of research time)

#### Purchase Tests
- [ ] Purchase button enables for researched, affordable components
- [ ] Purchase deducts correct amount of money
- [ ] Component marked as owned after purchase
- [ ] Performance score increases
- [ ] Power consumption updates
- [ ] Purchase blocked if insufficient funds
- [ ] Purchase blocked if insufficient power
- [ ] Success notification appears

#### Prerequisite Tests
- [ ] Cannot research component without prerequisites
- [ ] Warning appears if prerequisites not met
- [ ] Can research after prerequisites are owned
- [ ] Tech tree progression works correctly

#### Save/Load Tests
- [ ] Can save game
- [ ] Save file created at `~/.maximum_pc_game_save.json`
- [ ] Can load saved game
- [ ] All state restored correctly (money, components, research)
- [ ] Active research resumes correctly
- [ ] Auto-save writes the save file silently (every ~30 seconds)
- [ ] Auto-save triggers on window close

#### Achievement Tests
- [ ] Achievement unlock popup appears when a milestone is reached
- [ ] Achievements window opens via the "🏆 Achievements" button
- [ ] Achievements window lists all 15 achievements
- [ ] Achievement progress is tracked and persisted

#### Reset Tests
- [ ] Reset confirmation dialog appears
- [ ] Reset returns to initial state
- [ ] All components unmarked
- [ ] Resources reset to starting values

#### Victory Tests
- [ ] Game detects ultimate build completion
- [ ] Victory accepts alternate CPU (AMD EPYC 9754 or Intel Xeon Platinum 8592+)
- [ ] Victory accepts alternate GPU (NVIDIA H200 Octo or NVIDIA B200 Quad)
- [ ] Victory message displays with correct stats
- [ ] Can continue playing after victory
- [ ] Victory state persists after save/load

### Performance Tests
- [ ] Game loop runs smoothly (no lag)
- [ ] UI remains responsive during research
- [ ] No memory leaks during extended play
- [ ] Research timers are accurate

### Edge Case Tests
- [ ] Cannot purchase unresearched components
- [ ] Cannot research already researched components
- [ ] Cannot exceed power budget
- [ ] Handles negative money gracefully (shouldn't happen)
- [ ] Multiple rapid button clicks handled correctly
- [ ] Window resize works properly

## Uninstallation Tests

### Using Package Manager
```bash
# For .deb installation
sudo apt-get remove maximum-pc-builder

# Verify removal
which maximum-pc-builder  # Should return nothing
ls /usr/share/applications/maximum-pc-builder.desktop  # Should not exist
```

### Using Uninstall Script
```bash
chmod +x uninstall.sh
./uninstall.sh

# Verify removal
which maximum-pc-builder
```

### Manual Cleanup
```bash
# Remove save file if desired
rm ~/.maximum_pc_game_save.json
```

## Troubleshooting

### Game Won't Launch
**Issue**: Command not found
- **Solution**: Check PATH or use full path `/usr/bin/maximum-pc-builder`

**Issue**: Python error on launch
- **Solution**: Verify Python 3.8+ is installed: `python3 --version`

**Issue**: Tkinter import error
- **Solution**: Install python3-tk: `sudo apt-get install python3-tk`

### UI Issues
**Issue**: Window too small or text cut off
- **Solution**: Resize window manually, minimum recommended: 1200x800

**Issue**: Colors look wrong
- **Solution**: Verify display supports 24-bit color

### Gameplay Issues
**Issue**: Research not progressing
- **Solution**: Ensure game window has focus and game loop is running

**Issue**: Can't purchase component
- **Solution**: Check money, power budget, and prerequisites

**Issue**: Save file not loading
- **Solution**: Check file exists and has valid JSON: `cat ~/.maximum_pc_game_save.json`

### Build Issues
**Issue**: .deb build fails
- **Solution**: Check dpkg-deb is installed: `sudo apt-get install dpkg`

**Issue**: Permission denied on scripts
- **Solution**: Make scripts executable: `chmod +x *.sh`

## Known Limitations

- Single research queue (only one component at a time)
- No sound effects or music
- No multiplayer or leaderboards
- Save file is plain JSON (not encrypted)
- Auto-save interval is fixed (every ~30 seconds, not configurable)

## Performance Requirements

- **Minimum**: 
  - CPU: Any modern x86_64 processor
  - RAM: 100MB free
  - Disk: 10MB free
  - Display: 1024x768 minimum

- **Recommended**:
  - CPU: Dual-core 1GHz+
  - RAM: 256MB free
  - Disk: 50MB free
  - Display: 1920x1080 or higher

## Support

If you encounter issues:

1. Check this testing guide for solutions
2. Review the GAME_GUIDE.md for gameplay help
3. Check the README.md for general information
4. Open an issue on GitHub with:
   - Linux distribution and version
   - Python version
   - Error messages
   - Steps to reproduce

## Verification Commands

Quick verification after installation:

```bash
# Check installation
which maximum-pc-builder
ls -l /usr/share/applications/maximum-pc-builder.desktop
ls -l /usr/share/maximum-pc-builder/maximum_pc_game.py

# Test launch
maximum-pc-builder --version 2>/dev/null || echo "Game binary exists"

# Check dependencies
python3 --version
python3 -c "import tkinter; print('Tkinter OK')"

# List package files (if installed via .deb)
dpkg -L maximum-pc-builder
```

## Success Criteria

Installation is successful when:
- ✅ Game launches without errors
- ✅ UI displays correctly
- ✅ All game mechanics function
- ✅ Save/load works
- ✅ Can progress through tech tree
- ✅ Victory condition works

Enjoy building your Maximum PC! 🚀
