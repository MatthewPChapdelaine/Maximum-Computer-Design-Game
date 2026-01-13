# Project Structure

```
Maximum-Computer-Design-Game/
│
├── src/
│   └── maximum_pc_game.py          # Main game application (900+ lines)
│
├── DEBIAN/
│   ├── control                     # Debian package metadata
│   ├── postinst                    # Post-installation script
│   └── postrm                      # Post-removal script
│
├── build-deb.sh                    # Build .deb package script
├── install.sh                      # Manual installation script
├── uninstall.sh                    # Uninstallation script
├── run-game.sh                     # Quick run script for development
│
├── maximum-pc-builder.desktop      # Desktop entry file
├── setup.py                        # Python setuptools configuration
│
├── README.md                       # Main project documentation
├── LICENSE                         # MIT License
├── CHANGELOG.md                    # Version history
├── GAME_GUIDE.md                   # Comprehensive gameplay guide
├── TESTING.md                      # Testing and installation guide
├── PROJECT_STRUCTURE.md            # This file
│
└── Maximum Performance Linux Machine Specification.md
                                    # Original specification document

# Generated During Build

build/                              # Build artifacts (created by build-deb.sh)
└── maximum-pc-builder_1.0.0/       # Package contents
    ├── DEBIAN/
    │   ├── control
    │   ├── postinst
    │   └── postrm
    ├── usr/
    │   ├── bin/
    │   │   └── maximum-pc-builder  # Launcher script
    │   └── share/
    │       ├── applications/
    │       │   └── maximum-pc-builder.desktop
    │       ├── pixmaps/
    │       │   └── maximum-pc-builder.png
    │       ├── maximum-pc-builder/
    │       │   └── maximum_pc_game.py
    │       └── doc/
    │           └── maximum-pc-builder/
    │               ├── README.md
    │               └── LICENSE

maximum-pc-builder_1.0.0.deb        # Final installable package

# User Data

~/.maximum_pc_game_save.json        # Save file (in user's home directory)
```

## File Descriptions

### Core Game Files

#### `src/maximum_pc_game.py`
Main game implementation featuring:
- Component class definition
- MaximumPCGame class with full game logic
- Tkinter GUI implementation
- 40+ game components across 8 categories
- Research system with progress tracking
- Purchase system with prerequisites
- Save/load functionality
- Game loop and resource management
- Victory condition detection

### Package Files

#### `DEBIAN/control`
Debian package metadata:
- Package name and version
- Dependencies (python3, python3-tk)
- Package description
- Maintainer information
- Architecture specification

#### `DEBIAN/postinst`
Post-installation script:
- Updates desktop database
- Updates icon cache
- Ensures proper system integration

#### `DEBIAN/postrm`
Post-removal script:
- Cleans up desktop database
- Ensures clean uninstallation

### Build & Installation Scripts

#### `build-deb.sh`
Automated .deb package builder:
- Creates build directory structure
- Copies all necessary files
- Sets proper permissions
- Builds .deb package with dpkg-deb
- Provides installation instructions

#### `install.sh`
Manual installation script (non-.deb):
- Checks dependencies
- Copies files to system directories
- Creates launcher script
- Installs desktop entry
- Updates system databases
- Works on all Linux distributions

#### `uninstall.sh`
Uninstallation script:
- Removes all installed files
- Cleans up system directories
- Updates desktop database
- Preserves user save files

#### `run-game.sh`
Development/testing script:
- Checks dependencies
- Runs game directly from source
- No installation required
- Useful for testing changes

### Desktop Integration

#### `maximum-pc-builder.desktop`
FreeDesktop.org desktop entry:
- Application name and description
- Executable path
- Icon specification
- Categories (Game, Strategy, Simulation)
- Keywords for search
- Ensures proper application menu integration

#### `setup.py`
Python setuptools configuration:
- Package metadata
- Dependencies
- Entry points
- Installation configuration
- Used by install.sh

### Documentation

#### `README.md`
Primary documentation:
- Project overview
- Feature list
- Installation instructions
- Quick start guide
- Development information
- License and credits

#### `GAME_GUIDE.md`
Comprehensive gameplay guide:
- Complete game mechanics explanation
- Strategy guides for each game phase
- Component details and progression paths
- Tips and tricks
- FAQ section
- Victory condition details

#### `TESTING.md`
Testing and troubleshooting:
- Installation methods
- Testing checklist
- Functionality verification
- Troubleshooting guide
- Known limitations
- Support information

#### `CHANGELOG.md`
Version history:
- Release notes
- Feature additions
- Bug fixes
- Planned features

#### `LICENSE`
MIT License:
- Open source license text
- Usage permissions
- Liability disclaimers

#### `Maximum Performance Linux Machine Specification.md`
Original specification:
- Hardware component specifications
- Cost estimates
- Performance metrics
- Real-world product links
- Basis for game content

## Installation Paths

When installed via .deb or install.sh:

- **Executable**: `/usr/bin/maximum-pc-builder`
- **Game Files**: `/usr/share/maximum-pc-builder/`
- **Desktop Entry**: `/usr/share/applications/maximum-pc-builder.desktop`
- **Icon**: `/usr/share/pixmaps/maximum-pc-builder.png`
- **Documentation**: `/usr/share/doc/maximum-pc-builder/`
- **Save File**: `~/.maximum_pc_game_save.json` (user's home)

## Key Features

### Component System
- 40+ components across 8 categories
- Progressive tech tree with prerequisites
- Real-world inspired specifications
- Cost range: $50 to $500,000 per component

### Resource Management
- Money (starting: $50,000)
- Research points (starting: 100)
- Power budget (dynamic based on PSU)
- Performance score (aggregate metric)

### Game Mechanics
- Real-time resource generation
- Sequential research system
- Power budget constraints
- Prerequisite enforcement
- Save/load functionality
- Victory detection

### UI Features
- Dark theme optimized for extended play
- Category-based filtering
- Real-time progress bars
- Detailed component information
- Status indicators
- Responsive buttons

## Technical Specifications

- **Language**: Python 3.8+
- **GUI Framework**: Tkinter (standard library)
- **Package Format**: Debian .deb
- **Save Format**: JSON
- **Lines of Code**: ~900 (main game file)
- **Package Size**: ~50KB (without dependencies)
- **Memory Usage**: ~50-100MB during gameplay
- **Supported Platforms**: Linux (all distributions)

## Development Workflow

1. **Edit Source**: Modify `src/maximum_pc_game.py`
2. **Test**: Run with `./run-game.sh` or `python3 src/maximum_pc_game.py`
3. **Build**: Execute `./build-deb.sh` to create package
4. **Install**: Install with `sudo dpkg -i maximum-pc-builder_1.0.0.deb`
5. **Test Installation**: Launch from application menu or terminal
6. **Distribute**: Share the .deb file

## Future Expansion Areas

Potential additions based on code structure:

- Achievement system (tracking milestones)
- Multiple save slots
- Benchmark/score attack mode
- Additional component tiers
- Sound effects and music
- Localization support
- Cloud save functionality
- Community features
- Performance statistics
- Build sharing

## Maintenance Notes

### To Update Version
1. Edit `DEBIAN/control` - Update Version field
2. Edit `setup.py` - Update version parameter
3. Update `CHANGELOG.md` - Document changes
4. Rebuild package with new version number

### To Add Components
1. Edit `src/maximum_pc_game.py`
2. Add new Component() instances in `_create_components()`
3. Update `GAME_GUIDE.md` with new component info
4. Test thoroughly
5. Rebuild package

### To Modify UI
1. Edit `_setup_ui()` method in `src/maximum_pc_game.py`
2. Test layout changes
3. Verify all screen sizes
4. Update screenshots in documentation

## Dependencies

### Runtime Dependencies
- python3 (>= 3.8)
- python3-tk

### Build Dependencies
- dpkg-deb (for .deb creation)
- chmod (for permissions)
- bash (for scripts)

### Optional Dependencies
- imagemagick (for icon creation in build-deb.sh)

## Code Organization

The main game file (`src/maximum_pc_game.py`) is organized as follows:

1. **Imports and Docstring** (lines 1-10)
2. **Component Class** (lines 12-25)
3. **MaximumPCGame Class** (lines 27-900+)
   - Initialization
   - Component creation
   - UI setup
   - Event handlers
   - Game logic
   - Save/load system
   - Victory detection

## Distribution

The project can be distributed as:
1. **.deb package** - For Debian/Ubuntu/Mint users
2. **Source code** - For developers and other Linux distributions
3. **Git repository** - For version control and collaboration
4. **Install script** - For universal Linux installation

All methods are documented and supported.
