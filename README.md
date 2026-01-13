# Maximum Performance PC Builder 🖥️⚡

A strategic RPG-style game for Linux where you build the ultimate high-performance workstation! Inspired by real-world maximum performance PC specifications, this game challenges you to research, plan, and construct a technological masterpiece.

![Game Type](https://img.shields.io/badge/Genre-Strategy%20RPG-blue)
![Platform](https://img.shields.io/badge/Platform-Linux-orange)
![License](https://img.shields.io/badge/License-MIT-green)

## 🎮 Game Features

- **Progressive Research System**: Unlock advanced components through strategic research
- **Resource Management**: Balance your budget with game currency representing real money
- **Strategic Planning**: Plan your build path to achieve technological supremacy
- **Progress Bars**: Watch your research and builds progress in real-time
- **Component Categories**:
  - 💻 CPUs (from budget to 128-core EPYC/Xeon monsters)
  - 🧠 RAM (16GB to 24TB DDR5 configurations)
  - 💾 Storage (500GB SSDs to 1PB+ RAID arrays)
  - 🎨 GPUs (budget cards to 8x NVIDIA H200 setups)
  - 🔧 Infrastructure (motherboards, networking, cooling, power)
- **Save/Load System**: Continue your journey anytime
- **Ultimate Goal**: Build the $1M+ maximum performance Linux machine!

## 📦 Installation

### Quick Install (Recommended)

Download and install the `.deb` package:

```bash
# Clone the repository
git clone https://github.com/MatthewPChapdelaine/Maximum-Computer-Design-Game.git
cd Maximum-Computer-Design-Game

# Build the package
chmod +x build-deb.sh
./build-deb.sh

# Install
sudo dpkg -i maximum-pc-builder_1.0.0.deb

# Fix any dependency issues (if needed)
sudo apt-get install -f
```

### Launch the Game

After installation, you can launch the game:

- From Applications Menu: Look for "Maximum PC Builder" in the Games category
- From Terminal: `maximum-pc-builder`
- From Desktop: The application will appear in your application launcher

### Prerequisites

- Linux distribution (Ubuntu, Linux Mint, Debian, etc.)
- Python 3.8 or higher
- python3-tk (Tkinter)

## 🎯 How to Play

### Getting Started

1. **Start with Basic Components**: Begin with budget CPUs, RAM, and storage
2. **Research New Technology**: Use research points to unlock advanced components
3. **Manage Your Budget**: Start with $50,000 in game currency
4. **Watch Your Power**: Each component draws power - upgrade PSUs as needed
5. **Follow Prerequisites**: Advanced components require basic ones first

### Game Mechanics

- **Passive Income**: Earn money and research points over time
- **Research**: Click components and start research to unlock them
- **Purchase**: Buy researched components to add them to your build
- **Progress Bars**: Watch research complete in real-time
- **Performance Score**: Track your overall system performance

### Tips & Strategy

- Start with infrastructure (motherboard, PSU) to support advanced components
- Research multiple tiers before purchasing to plan your upgrade path
- Balance spending between CPU, RAM, storage, and GPU based on your goals
- Don't forget cooling and power - high-end components need serious infrastructure!
- Save your game regularly to preserve progress

### Ultimate Goal

Build the complete Maximum Performance Linux Machine featuring:
- AMD EPYC 9754 (128 cores, 256 threads)
- 24TB DDR5-6400 RAM
- 1PB NVMe RAID Array
- 8x NVIDIA H200 GPUs (1.128TB VRAM, 12 PFLOPS)
- Dual-socket server platform
- 100Gb networking
- 24kW power infrastructure

## 🛠️ Development

### Running from Source

```bash
# Clone the repository
git clone https://github.com/MatthewPChapdelaine/Maximum-Computer-Design-Game.git
cd Maximum-Computer-Design-Game

# Run directly
python3 src/maximum_pc_game.py
```

### Building the Package

```bash
# Make build script executable
chmod +x build-deb.sh

# Build the .deb package
./build-deb.sh

# The package will be created as maximum-pc-builder_1.0.0.deb
```

### Project Structure

```
Maximum-Computer-Design-Game/
├── src/
│   └── maximum_pc_game.py       # Main game code
├── DEBIAN/
│   ├── control                   # Package metadata
│   ├── postinst                 # Post-installation script
│   └── postrm                   # Post-removal script
├── build-deb.sh                 # Build script
├── setup.py                     # Python setup configuration
├── maximum-pc-builder.desktop   # Desktop entry file
├── LICENSE                      # MIT License
└── README.md                    # This file
```

## 🎨 Screenshots

The game features:
- Clean, dark-themed UI optimized for extended play
- Real-time status bars showing money, research points, performance, and power
- Detailed component information with prerequisites and specs
- Category filtering for easy navigation
- Progress bars for research tracking
- Color-coded status indicators

## 🔧 Technical Details

- **Language**: Python 3
- **GUI Framework**: Tkinter (built into Python)
- **Package Format**: Debian .deb
- **Dependencies**: python3, python3-tk
- **Save Location**: `~/.maximum_pc_game_save.json`

## 📚 Game Design Philosophy

This game is designed to:
- Inspire strategic thinking about PC component selection
- Teach real-world hardware relationships and dependencies
- Provide engaging progression mechanics
- Demonstrate the complexity of building ultimate performance systems
- Make learning about hardware fun and interactive

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new components
- Improve game balance
- Add features
- Enhance UI/UX

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Based on the "Maximum Performance Linux Machine Specification" article
- Component specifications inspired by real hardware
- Built with Python and Tkinter
- Claude AI assisted in document creation

## 📞 Support

For issues, questions, or suggestions:
- Open an issue on GitHub
- Check existing issues for solutions
- Contribute improvements via pull requests

## 🎮 Enjoy Building!

May your framerates be high and your temperatures low! 🚀

---

**Note**: This is a simulation game. Component prices and specifications are simplified for gameplay. For real hardware purchases, consult manufacturer specifications and current market prices.
