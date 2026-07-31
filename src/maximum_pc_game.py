#!/usr/bin/env python3
"""
Maximum Performance PC Builder - RPG Strategy Game
Build your ultimate Linux workstation through strategic planning and resource management
"""

import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
from datetime import datetime

class Component:
    """Represents a PC component that can be researched and purchased"""
    def __init__(self, name, category, base_cost, research_time, power_draw, 
                 performance_boost, prerequisites=None, description=""):
        self.name = name
        self.category = category
        self.base_cost = base_cost
        self.research_time = research_time  # seconds for game progression
        self.power_draw = power_draw
        self.performance_boost = performance_boost
        self.prerequisites = prerequisites or []
        self.description = description
        self.researched = False
        self.owned = False
        self.research_progress = 0

def _owns_component(game, name):
    """Helper to check if a component is owned"""
    return any(c.name == name and c.owned for c in game.components)

ACHIEVEMENTS = [
    {"id": "first_build", "name": "First Build",
     "description": "Own at least 1 component",
     "condition": lambda g: sum(1 for c in g.components if c.owned) >= 1},
    {"id": "scholar", "name": "Scholar",
     "description": "Complete 5 research projects",
     "condition": lambda g: g.stats["researches_completed"] >= 5},
    {"id": "research_master", "name": "Research Master",
     "description": "Complete 15 research projects",
     "condition": lambda g: g.stats["researches_completed"] >= 15},
    {"id": "money_maker", "name": "Money Maker",
     "description": "Earn $100,000 in passive income",
     "condition": lambda g: g.stats["money_earned"] >= 100000},
    {"id": "tycoon", "name": "Tech Tycoon",
     "description": "Earn $500,000 in passive income",
     "condition": lambda g: g.stats["money_earned"] >= 500000},
    {"id": "power_player", "name": "Power Player",
     "description": "Reach a 24,000W power budget",
     "condition": lambda g: g.power_budget >= 24000},
    {"id": "memory_mogul", "name": "Memory Mogul",
     "description": "Own the 24TB DDR5-6400 Ultimate",
     "condition": lambda g: _owns_component(g, "24TB DDR5-6400 Ultimate")},
    {"id": "storage_giant", "name": "Storage Giant",
     "description": "Own the 1PB RAID Array",
     "condition": lambda g: _owns_component(g, "1PB RAID Array")},
    {"id": "compute_champion", "name": "Compute Champion",
     "description": "Own the NVIDIA H200 Octo",
     "condition": lambda g: _owns_component(g, "NVIDIA H200 Octo")},
    {"id": "server_king", "name": "Server King",
     "description": "Own the Server Platform",
     "condition": lambda g: _owns_component(g, "Server Platform")},
    {"id": "network_ninja", "name": "Network Ninja",
     "description": "Own the 100Gb QSFP28 Dual",
     "condition": lambda g: _owns_component(g, "100Gb QSFP28 Dual")},
    {"id": "core_lord", "name": "Core Lord",
     "description": "Own the AMD EPYC 9754 or Intel Xeon Platinum 8592+",
     "condition": lambda g: any(
         c.name in ("AMD EPYC 9754", "Intel Xeon Platinum 8592+") and c.owned
         for c in g.components)},
    {"id": "techno_supremacy", "name": "Technological Supremacy",
     "description": "Complete the Ultimate Build",
     "condition": lambda g: g.victory_achieved is True},
    {"id": "completionist", "name": "Completionist",
     "description": "Own every component in the game",
     "condition": lambda g: all(c.owned for c in g.components)},
    {"id": "veteran", "name": "Veteran Builder",
     "description": "Play for 30 minutes",
     "condition": lambda g: g.stats["play_seconds"] >= 1800},
]

class MaximumPCGame:
    """Main game class for Maximum PC Builder"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Maximum Performance PC Builder - Ultimate Edition")
        self.root.geometry("1200x800")
        self.root.configure(bg='#1a1a2e')
        
        # Game state
        self.money = 50000  # Starting capital
        self.research_points = 100
        self.power_budget = 2000  # watts
        self.performance_score = 0
        self.tick_rate = 100  # ms per game tick
        self.money_per_tick = 100  # passive income
        self.research_per_tick = 1
        self.game_running = True
        
        # Initialize components
        self.components = self._create_components()
        self.selected_component = None
        self.active_research = None
        self.victory_achieved = False
        self.auto_save_counter = 0
        
        # Stats and achievements
        self.stats = {
            "money_earned": 0.0,
            "researches_completed": 0,
            "purchases": 0,
            "play_seconds": 0.0
        }
        self.achievements_unlocked = {}
        
        # Setup UI
        self._setup_ui()
        
        # Save on window close
        self.root.protocol("WM_DELETE_WINDOW", self._on_close)
        
        # Start game loop
        self._game_loop()
        
        # Load saved game if exists (silent at startup)
        self._load_game(silent=True)
    
    def _create_components(self):
        """Create all available components"""
        components = []
        
        # CPU Components
        components.extend([
            Component(
                "Budget CPU", "CPU", 500, 10, 65,
                {"performance": 100, "cores": 8},
                [], "Entry-level processor for basic computing"
            ),
            Component(
                "Mid-Range CPU", "CPU", 2000, 30, 125,
                {"performance": 500, "cores": 16},
                ["Budget CPU"], "Solid mid-range processor"
            ),
            Component(
                "High-End CPU", "CPU", 8000, 60, 250,
                {"performance": 2000, "cores": 64},
                ["Mid-Range CPU"], "Server-class processor"
            ),
            Component(
                "Intel Xeon Platinum 8592+", "CPU", 12000, 120, 350,
                {"performance": 5000, "cores": 128},
                ["High-End CPU"], "64-core beast with 5.7GHz turbo"
            ),
            Component(
                "AMD EPYC 9754", "CPU", 11000, 120, 350,
                {"performance": 5200, "cores": 128},
                ["High-End CPU"], "128-core monster with 384MB L3 cache"
            ),
        ])
        
        # RAM Components
        components.extend([
            Component(
                "16GB DDR4", "RAM", 100, 5, 10,
                {"memory": 16, "bandwidth": 25},
                [], "Basic memory configuration"
            ),
            Component(
                "64GB DDR4", "RAM", 300, 15, 20,
                {"memory": 64, "bandwidth": 50},
                ["16GB DDR4"], "Decent memory for multitasking"
            ),
            Component(
                "256GB DDR5", "RAM", 2000, 30, 40,
                {"memory": 256, "bandwidth": 100},
                ["64GB DDR4"], "High-speed DDR5 memory"
            ),
            Component(
                "1TB DDR5-6400 RDIMM", "RAM", 8000, 60, 80,
                {"memory": 1024, "bandwidth": 400},
                ["256GB DDR5"], "Registered ECC DDR5 modules"
            ),
            Component(
                "24TB DDR5-6400 Ultimate", "RAM", 200000, 180, 500,
                {"memory": 24576, "bandwidth": 600},
                ["1TB DDR5-6400 RDIMM"], "24x 1TB modules - Ultimate memory"
            ),
        ])
        
        # Storage Components
        components.extend([
            Component(
                "500GB SATA SSD", "Storage", 50, 5, 5,
                {"capacity": 500, "speed": 550},
                [], "Basic solid state storage"
            ),
            Component(
                "2TB NVMe Gen3", "Storage", 200, 15, 8,
                {"capacity": 2000, "speed": 3500},
                ["500GB SATA SSD"], "Fast NVMe storage"
            ),
            Component(
                "8TB NVMe Gen4", "Storage", 800, 30, 12,
                {"capacity": 8000, "speed": 7000},
                ["2TB NVMe Gen3"], "Blazing Gen4 speeds"
            ),
            Component(
                "8TB NVMe Gen5", "Storage", 1200, 45, 15,
                {"capacity": 8000, "speed": 14000},
                ["8TB NVMe Gen4"], "Next-gen PCIe 5.0 speeds"
            ),
            Component(
                "1PB RAID Array", "Storage", 500000, 240, 2000,
                {"capacity": 1024000, "speed": 1400000},
                ["8TB NVMe Gen5"], "128x 8TB NVMe in RAID 6"
            ),
            Component(
                "2PB Secondary Storage", "Storage", 60000, 120, 500,
                {"capacity": 2048000, "speed": 5000},
                ["1PB RAID Array"], "Archive/backup storage array"
            ),
        ])
        
        # GPU Components
        components.extend([
            Component(
                "Budget GPU", "GPU", 300, 10, 150,
                {"compute": 500, "vram": 8},
                [], "Entry-level graphics"
            ),
            Component(
                "Mid-Range GPU", "GPU", 800, 20, 220,
                {"compute": 2000, "vram": 16},
                ["Budget GPU"], "Solid 1440p performance"
            ),
            Component(
                "High-End Gaming GPU", "GPU", 2000, 40, 350,
                {"compute": 8000, "vram": 24},
                ["Mid-Range GPU"], "Top-tier gaming GPU"
            ),
            Component(
                "Workstation GPU", "GPU", 5000, 60, 400,
                {"compute": 15000, "vram": 48},
                ["High-End Gaming GPU"], "Professional workstation GPU"
            ),
            Component(
                "NVIDIA H200 Single", "GPU", 40000, 90, 700,
                {"compute": 150000, "vram": 141},
                ["Workstation GPU"], "141GB HBM3E, 1.5 PFLOPS"
            ),
            Component(
                "NVIDIA H200 Octo", "GPU", 320000, 300, 5600,
                {"compute": 1200000, "vram": 1128},
                ["NVIDIA H200 Single"], "8x H200 with NVLink - 12 PFLOPS"
            ),
            Component(
                "NVIDIA B200 Quad", "GPU", 480000, 360, 4000,
                {"compute": 2000000, "vram": 768},
                ["NVIDIA H200 Octo"], "4x B200 - 80+ PFLOPS"
            ),
        ])
        
        # Motherboard & Infrastructure
        components.extend([
            Component(
                "Basic Motherboard", "Infrastructure", 150, 5, 30,
                {"slots": 4, "pcie_lanes": 16},
                [], "Basic consumer board"
            ),
            Component(
                "Enthusiast Board", "Infrastructure", 500, 15, 50,
                {"slots": 8, "pcie_lanes": 44},
                ["Basic Motherboard"], "High-end consumer board"
            ),
            Component(
                "Workstation Board", "Infrastructure", 1500, 30, 80,
                {"slots": 12, "pcie_lanes": 64},
                ["Enthusiast Board"], "Professional workstation board"
            ),
            Component(
                "Server Platform", "Infrastructure", 8000, 90, 150,
                {"slots": 24, "pcie_lanes": 128},
                ["Workstation Board"], "Dual-socket server platform"
            ),
        ])
        
        # Networking
        components.extend([
            Component(
                "1Gb Ethernet", "Network", 50, 5, 5,
                {"bandwidth": 1000},
                [], "Standard gigabit networking"
            ),
            Component(
                "10Gb Ethernet", "Network", 300, 15, 15,
                {"bandwidth": 10000},
                ["1Gb Ethernet"], "10 gigabit networking"
            ),
            Component(
                "40Gb QSFP+", "Network", 1000, 30, 25,
                {"bandwidth": 40000},
                ["10Gb Ethernet"], "40Gb datacenter networking"
            ),
            Component(
                "100Gb QSFP28 Dual", "Network", 5000, 60, 50,
                {"bandwidth": 200000},
                ["40Gb QSFP+"], "200Gb aggregate bandwidth"
            ),
        ])
        
        # Power & Cooling
        components.extend([
            Component(
                "750W PSU", "Power", 100, 5, 0,
                {"power_capacity": 750},
                [], "Basic power supply"
            ),
            Component(
                "1200W PSU", "Power", 250, 10, 0,
                {"power_capacity": 1200},
                ["750W PSU"], "High-end power supply"
            ),
            Component(
                "2000W PSU", "Power", 500, 20, 0,
                {"power_capacity": 2000},
                ["1200W PSU"], "Extreme power supply"
            ),
            Component(
                "Quad 6kW Titanium", "Power", 12000, 90, 0,
                {"power_capacity": 24000},
                ["2000W PSU"], "24kW redundant server PSUs"
            ),
            Component(
                "Liquid Cooling", "Cooling", 300, 15, 50,
                {"cooling": 500},
                [], "Closed-loop liquid cooling"
            ),
            Component(
                "Custom Loop", "Cooling", 1500, 30, 100,
                {"cooling": 2000},
                ["Liquid Cooling"], "Custom water cooling loop"
            ),
            Component(
                "Server Cooling System", "Cooling", 15000, 60, 200,
                {"cooling": 10000},
                ["Custom Loop"], "Industrial cooling with redundant pumps"
            ),
        ])
        
        return components
    
    def _setup_ui(self):
        """Setup the game UI"""
        # Top status bar
        status_frame = tk.Frame(self.root, bg='#16213e', height=80)
        status_frame.pack(fill=tk.X, padx=5, pady=5)
        status_frame.pack_propagate(False)
        
        # Money display
        money_frame = tk.Frame(status_frame, bg='#16213e')
        money_frame.pack(side=tk.LEFT, padx=20)
        tk.Label(money_frame, text="💰 Money:", font=('Arial', 12, 'bold'),
                bg='#16213e', fg='#00ff00').pack()
        self.money_label = tk.Label(money_frame, text=f"${self.money:,.0f}",
                                    font=('Arial', 14, 'bold'), bg='#16213e', fg='#00ff00')
        self.money_label.pack()
        
        # Research Points
        research_frame = tk.Frame(status_frame, bg='#16213e')
        research_frame.pack(side=tk.LEFT, padx=20)
        tk.Label(research_frame, text="🔬 Research:", font=('Arial', 12, 'bold'),
                bg='#16213e', fg='#00ffff').pack()
        self.research_label = tk.Label(research_frame, text=f"{self.research_points}",
                                       font=('Arial', 14, 'bold'), bg='#16213e', fg='#00ffff')
        self.research_label.pack()
        
        # Performance Score
        perf_frame = tk.Frame(status_frame, bg='#16213e')
        perf_frame.pack(side=tk.LEFT, padx=20)
        tk.Label(perf_frame, text="⚡ Performance:", font=('Arial', 12, 'bold'),
                bg='#16213e', fg='#ffff00').pack()
        self.perf_label = tk.Label(perf_frame, text=f"{self.performance_score:,.0f}",
                                   font=('Arial', 14, 'bold'), bg='#16213e', fg='#ffff00')
        self.perf_label.pack()
        
        # Power Usage
        power_frame = tk.Frame(status_frame, bg='#16213e')
        power_frame.pack(side=tk.LEFT, padx=20)
        tk.Label(power_frame, text="⚡ Power:", font=('Arial', 12, 'bold'),
                bg='#16213e', fg='#ff6b6b').pack()
        self.power_label = tk.Label(power_frame, text=f"0W / {self.power_budget}W",
                                    font=('Arial', 14, 'bold'), bg='#16213e', fg='#ff6b6b')
        self.power_label.pack()
        
        # Main content area
        content_frame = tk.Frame(self.root, bg='#1a1a2e')
        content_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Left panel - Component list
        left_panel = tk.Frame(content_frame, bg='#16213e', width=400)
        left_panel.pack(side=tk.LEFT, fill=tk.BOTH, padx=5)
        left_panel.pack_propagate(False)
        
        tk.Label(left_panel, text="Components", font=('Arial', 16, 'bold'),
                bg='#16213e', fg='#ffffff').pack(pady=10)
        
        # Category filter
        filter_frame = tk.Frame(left_panel, bg='#16213e')
        filter_frame.pack(fill=tk.X, padx=5)
        
        self.category_var = tk.StringVar(value="All")
        categories = ["All", "CPU", "RAM", "Storage", "GPU", "Infrastructure", "Network", "Power", "Cooling"]
        category_menu = ttk.Combobox(filter_frame, textvariable=self.category_var,
                                     values=categories, state='readonly', width=15)
        category_menu.pack(side=tk.LEFT, padx=5, pady=5)
        category_menu.bind('<<ComboboxSelected>>', lambda e: self._update_component_list())
        
        # Component listbox
        list_frame = tk.Frame(left_panel, bg='#16213e')
        list_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.component_listbox = tk.Listbox(list_frame, yscrollcommand=scrollbar.set,
                                           bg='#0f3460', fg='#ffffff',
                                           font=('Arial', 10), selectmode=tk.SINGLE,
                                           height=20)
        self.component_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.component_listbox.yview)
        self.component_listbox.bind('<<ListboxSelect>>', self._on_component_select)
        
        # Right panel - Component details
        right_panel = tk.Frame(content_frame, bg='#16213e')
        right_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)
        
        tk.Label(right_panel, text="Component Details", font=('Arial', 16, 'bold'),
                bg='#16213e', fg='#ffffff').pack(pady=10)
        
        # Details text area
        details_frame = tk.Frame(right_panel, bg='#16213e')
        details_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        self.details_text = tk.Text(details_frame, bg='#0f3460', fg='#ffffff',
                                   font=('Arial', 11), wrap=tk.WORD, height=15)
        self.details_text.pack(fill=tk.BOTH, expand=True)
        
        # Research/Purchase progress bar
        progress_frame = tk.Frame(right_panel, bg='#16213e')
        progress_frame.pack(fill=tk.X, padx=10, pady=10)
        
        self.progress_label = tk.Label(progress_frame, text="Progress:",
                                       bg='#16213e', fg='#ffffff', font=('Arial', 10))
        self.progress_label.pack()
        
        self.progress_bar = ttk.Progressbar(progress_frame, mode='determinate', length=400)
        self.progress_bar.pack(pady=5)
        
        # Action buttons
        button_frame = tk.Frame(right_panel, bg='#16213e')
        button_frame.pack(fill=tk.X, padx=10, pady=10)
        
        self.research_button = tk.Button(button_frame, text="🔬 Start Research",
                                         command=self._start_research,
                                         bg='#00ffff', fg='#000000',
                                         font=('Arial', 12, 'bold'),
                                         state=tk.DISABLED)
        self.research_button.pack(side=tk.LEFT, padx=5, expand=True, fill=tk.X)
        
        self.purchase_button = tk.Button(button_frame, text="💰 Purchase",
                                        command=self._purchase_component,
                                        bg='#00ff00', fg='#000000',
                                        font=('Arial', 12, 'bold'),
                                        state=tk.DISABLED)
        self.purchase_button.pack(side=tk.LEFT, padx=5, expand=True, fill=tk.X)
        
        # Bottom panel - Game controls
        bottom_frame = tk.Frame(self.root, bg='#16213e', height=60)
        bottom_frame.pack(fill=tk.X, padx=5, pady=5)
        bottom_frame.pack_propagate(False)
        
        tk.Button(bottom_frame, text="💾 Save Game", command=self._save_game,
                 bg='#4ecdc4', fg='#000000', font=('Arial', 11, 'bold')).pack(side=tk.LEFT, padx=10, pady=10)
        tk.Button(bottom_frame, text="🔄 Load Game", command=self._load_game,
                 bg='#95e1d3', fg='#000000', font=('Arial', 11, 'bold')).pack(side=tk.LEFT, padx=10, pady=10)
        tk.Button(bottom_frame, text="🔄 Reset Game", command=self._reset_game,
                 bg='#ff6b6b', fg='#000000', font=('Arial', 11, 'bold')).pack(side=tk.LEFT, padx=10, pady=10)
        tk.Button(bottom_frame, text="🏆 Achievements", command=self._show_achievements,
                 bg='#f9d423', fg='#000000', font=('Arial', 11, 'bold')).pack(side=tk.LEFT, padx=10, pady=10)
        
        # Initialize component list
        self._update_component_list()
    
    def _update_component_list(self):
        """Update the component listbox"""
        self.component_listbox.delete(0, tk.END)
        
        category = self.category_var.get()
        
        for comp in self.components:
            if category != "All" and comp.category != category:
                continue
            
            status = ""
            if comp.owned:
                status = "✓ "
            elif comp.researched:
                status = "📖 "
            elif self.active_research == comp:
                status = "🔬 "
            
            name = f"{status}{comp.name} (${comp.base_cost:,.0f})"
            self.component_listbox.insert(tk.END, name)
    
    def _on_component_select(self, event):
        """Handle component selection"""
        selection = self.component_listbox.curselection()
        if not selection:
            return
        
        idx = selection[0]
        category = self.category_var.get()
        
        # Find the actual component
        visible_comps = [c for c in self.components if category == "All" or c.category == category]
        if idx >= len(visible_comps):
            return
        
        self.selected_component = visible_comps[idx]
        self._update_details()
    
    def _update_details(self):
        """Update component details panel"""
        if not self.selected_component:
            return
        
        comp = self.selected_component
        
        self.details_text.delete('1.0', tk.END)
        
        details = f"Component: {comp.name}\n"
        details += f"Category: {comp.category}\n"
        details += f"Cost: ${comp.base_cost:,.0f}\n"
        details += f"Power Draw: {comp.power_draw}W\n"
        details += f"Research Time: {comp.research_time}s\n"
        details += f"Research Cost: {comp.research_time} points\n\n"
        details += f"Description:\n{comp.description}\n\n"
        
        if comp.performance_boost:
            details += "Performance Boosts:\n"
            for key, value in comp.performance_boost.items():
                details += f"  • {key.replace('_', ' ').title()}: {value:,.0f}\n"
        
        details += "\nPrerequisites:\n"
        if comp.prerequisites:
            for prereq in comp.prerequisites:
                prereq_comp = next((c for c in self.components if c.name == prereq), None)
                if prereq_comp:
                    status = "✓" if prereq_comp.owned else "✗"
                    details += f"  {status} {prereq}\n"
        else:
            details += "  None\n"
        
        details += "\nStatus:\n"
        if comp.owned:
            details += "  ✓ Owned\n"
        elif comp.researched:
            details += "  📖 Researched (ready to purchase)\n"
        else:
            details += "  🔒 Locked (requires research)\n"
        
        self.details_text.insert('1.0', details)
        
        # Update buttons
        prereqs_met = all(
            next((c for c in self.components if c.name == p), None).owned
            for p in comp.prerequisites
        )
        
        if not comp.researched and not comp.owned and prereqs_met:
            self.research_button.config(state=tk.NORMAL if self.active_research is None else tk.DISABLED)
        else:
            self.research_button.config(state=tk.DISABLED)
        
        if comp.researched and not comp.owned and prereqs_met:
            self.purchase_button.config(state=tk.NORMAL if self.money >= comp.base_cost else tk.DISABLED)
        else:
            self.purchase_button.config(state=tk.DISABLED)
        
        # Update progress bar
        if self.active_research == comp:
            progress = (comp.research_progress / comp.research_time) * 100
            self.progress_bar['value'] = progress
            self.progress_label.config(text=f"Researching... {comp.research_progress:.0f}s / {comp.research_time}s")
        else:
            self.progress_bar['value'] = 0
            self.progress_label.config(text="Progress:")
    
    def _start_research(self):
        """Start researching selected component"""
        if not self.selected_component or self.active_research:
            return
        
        comp = self.selected_component
        
        if comp.researched or comp.owned:
            return
        
        # Check research points
        if self.research_points < comp.research_time:
            messagebox.showwarning(
                "Insufficient Research Points",
                f"Researching this component costs {comp.research_time:.0f} points "
                f"but you only have {self.research_points:.0f}!"
            )
            return
        
        # Check prerequisites
        prereqs_met = all(
            next((c for c in self.components if c.name == p), None).owned
            for p in comp.prerequisites
        )
        
        if not prereqs_met:
            messagebox.showwarning("Prerequisites Not Met",
                                  "You must own all prerequisite components first!")
            return
        
        self.research_points -= comp.research_time
        self.active_research = comp
        comp.research_progress = 0
        self._update_component_list()
        self._update_details()
        messagebox.showinfo("Research Started", f"Now researching: {comp.name}")
    
    def _purchase_component(self):
        """Purchase the selected component"""
        if not self.selected_component:
            return
        
        comp = self.selected_component
        
        if not comp.researched or comp.owned:
            return
        
        if self.money < comp.base_cost:
            messagebox.showwarning("Insufficient Funds",
                                  f"You need ${comp.base_cost:,.0f} but only have ${self.money:,.0f}")
            return
        
        # Check power budget
        current_power = sum(c.power_draw for c in self.components if c.owned)
        if current_power + comp.power_draw > self.power_budget:
            messagebox.showwarning("Insufficient Power",
                                  f"This component needs {comp.power_draw}W but you only have "
                                  f"{self.power_budget - current_power}W available!")
            return
        
        # Purchase
        self.money -= comp.base_cost
        comp.owned = True
        self.stats["purchases"] += 1
        
        # Update performance
        if comp.performance_boost:
            for key, value in comp.performance_boost.items():
                self.performance_score += value
        
        # Update power budget if it's a PSU
        if comp.category == "Power" and "power_capacity" in comp.performance_boost:
            self._recalculate_power_budget()
        
        self._update_component_list()
        self._update_details()
        self._update_status()
        
        messagebox.showinfo("Purchase Complete", f"Successfully purchased: {comp.name}!")
        
        # Check for ultimate build completion
        self._check_ultimate_build()
        self._check_achievements()
    
    def _game_loop(self):
        """Main game loop"""
        if not self.game_running:
            return
        
        # Add passive income
        self.money += self.money_per_tick
        self.research_points += self.research_per_tick
        
        # Track stats
        self.stats["money_earned"] += self.money_per_tick
        self.stats["play_seconds"] += self.tick_rate / 1000.0
        
        # Update research progress
        if self.active_research:
            self.active_research.research_progress += self.tick_rate / 1000.0
            
            if self.active_research.research_progress >= self.active_research.research_time:
                completed = self.active_research
                completed.researched = True
                self.stats["researches_completed"] += 1
                self.active_research = None
                self._update_component_list()
                self._check_achievements()
                messagebox.showinfo("Research Complete", f"Research completed: {completed.name}!")
                if self.selected_component == completed:
                    self._update_details()
            
            if self.selected_component == self.active_research:
                self._update_details()
        
        # Auto-save every 300 ticks
        self.auto_save_counter += 1
        if self.auto_save_counter >= 300:
            self.auto_save_counter = 0
            self._save_game(silent=True)
        
        # Update UI
        self._update_status()
        
        # Schedule next tick
        self.root.after(self.tick_rate, self._game_loop)
    
    def _update_status(self):
        """Update status bar"""
        self.money_label.config(text=f"${self.money:,.0f}")
        self.research_label.config(text=f"{self.research_points}")
        self.perf_label.config(text=f"{self.performance_score:,.0f}")
        
        current_power = sum(c.power_draw for c in self.components if c.owned)
        self.power_label.config(text=f"{current_power}W / {self.power_budget}W")
        
        # Update purchase button state
        if self.selected_component and self.selected_component.researched and not self.selected_component.owned:
            self.purchase_button.config(state=tk.NORMAL if self.money >= self.selected_component.base_cost else tk.DISABLED)
    
    def _check_ultimate_build(self):
        """Check if ultimate build is complete"""
        ultimate_components = [
            "24TB DDR5-6400 Ultimate",
            "1PB RAID Array",
            "Server Platform",
            "100Gb QSFP28 Dual",
            "Quad 6kW Titanium"
        ]
        
        cpu_owned = any(c.name in ("AMD EPYC 9754", "Intel Xeon Platinum 8592+") and c.owned
                        for c in self.components)
        gpu_owned = any(c.name in ("NVIDIA H200 Octo", "NVIDIA B200 Quad") and c.owned
                        for c in self.components)
        owned_ultimate = sum(1 for c in self.components if c.name in ultimate_components and c.owned)
        
        if owned_ultimate == len(ultimate_components) and cpu_owned and gpu_owned:
            if not self.victory_achieved:
                self.victory_achieved = True
                messagebox.showinfo(
                    "🏆 ULTIMATE BUILD COMPLETE! 🏆",
                    "Congratulations! You've built the Maximum Performance Linux Machine!\n\n"
                    f"Final Performance Score: {self.performance_score:,.0f}\n"
                    f"Total Investment: ${sum(c.base_cost for c in self.components if c.owned):,.0f}\n\n"
                    "You've achieved technological supremacy!"
                )
    
    def _save_game(self, silent=False):
        """Save game state"""
        save_data = {
            "money": self.money,
            "research_points": self.research_points,
            "power_budget": self.power_budget,
            "performance_score": self.performance_score,
            "stats": self.stats,
            "achievements_unlocked": self.achievements_unlocked,
            "victory_achieved": self.victory_achieved,
            "components": [
                {
                    "name": c.name,
                    "researched": c.researched,
                    "owned": c.owned,
                    "research_progress": c.research_progress
                }
                for c in self.components
            ],
            "active_research": self.active_research.name if self.active_research else None,
            "timestamp": datetime.now().isoformat()
        }
        
        save_path = os.path.expanduser("~/.maximum_pc_game_save.json")
        with open(save_path, 'w') as f:
            json.dump(save_data, f, indent=2)
        
        if not silent:
            messagebox.showinfo("Game Saved", f"Game saved successfully!\n{save_path}")
    
    def _load_game(self, silent=False):
        """Load game state"""
        save_path = os.path.expanduser("~/.maximum_pc_game_save.json")
        
        if not os.path.exists(save_path):
            return
        
        try:
            with open(save_path, 'r') as f:
                save_data = json.load(f)
            
            self.money = save_data["money"]
            self.research_points = save_data["research_points"]
            self.power_budget = save_data["power_budget"]
            self.performance_score = save_data["performance_score"]
            
            default_stats = {
                "money_earned": 0.0,
                "researches_completed": 0,
                "purchases": 0,
                "play_seconds": 0.0
            }
            self.stats = {**default_stats, **save_data.get("stats", {})}
            self.achievements_unlocked = save_data.get("achievements_unlocked") or {}
            self.victory_achieved = bool(save_data.get("victory_achieved", False))
            
            for comp_data in save_data["components"]:
                comp = next((c for c in self.components if c.name == comp_data["name"]), None)
                if comp:
                    comp.researched = comp_data["researched"]
                    comp.owned = comp_data["owned"]
                    comp.research_progress = comp_data["research_progress"]
            
            self._recalculate_power_budget()
            
            active_research_name = save_data.get("active_research")
            self.active_research = next(
                (c for c in self.components if c.name == active_research_name),
                None
            ) if active_research_name else None
            
            self._update_component_list()
            self._update_status()
            self._check_ultimate_build()
            self._check_achievements()
            
            if not silent:
                messagebox.showinfo("Game Loaded", "Game loaded successfully!")
        except Exception as e:
            messagebox.showerror("Load Error", f"Failed to load game: {e}")
    
    def _reset_game(self):
        """Reset game to initial state"""
        if messagebox.askyesno("Reset Game", "Are you sure you want to reset? All progress will be lost!"):
            self.money = 50000
            self.research_points = 100
            self.power_budget = 2000
            self.performance_score = 0
            self.active_research = None
            self.victory_achieved = False
            self.auto_save_counter = 0
            self.stats = {
                "money_earned": 0.0,
                "researches_completed": 0,
                "purchases": 0,
                "play_seconds": 0.0
            }
            self.achievements_unlocked = {}
            
            for comp in self.components:
                comp.researched = False
                comp.owned = False
                comp.research_progress = 0
            
            self._recalculate_power_budget()
            self._update_component_list()
            self._update_status()
            
            messagebox.showinfo("Game Reset", "Game has been reset to initial state.")
    
    def _recalculate_power_budget(self):
        """Recalculate power budget from all owned power supplies"""
        total_capacity = sum(
            c.performance_boost.get("power_capacity", 0)
            for c in self.components
            if c.category == "Power" and c.owned
        )
        self.power_budget = 2000 + total_capacity
    
    def _check_achievements(self):
        """Check for newly unlocked achievements"""
        for achievement in ACHIEVEMENTS:
            if achievement["id"] in self.achievements_unlocked:
                continue
            if achievement["condition"](self):
                self.achievements_unlocked[achievement["id"]] = datetime.now().isoformat()
                messagebox.showinfo(
                    "🏆 Achievement Unlocked!",
                    f"{achievement['name']}\n\n{achievement['description']}"
                )
    
    def _show_achievements(self):
        """Show the achievements window"""
        window = tk.Toplevel(self.root)
        window.title("🏆 Achievements")
        window.geometry("500x600")
        window.configure(bg='#1a1a2e')
        
        text = tk.Text(window, bg='#0f3460', fg='#ffffff',
                       font=('Arial', 11), wrap=tk.WORD)
        text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        unlocked = [a for a in ACHIEVEMENTS if a["id"] in self.achievements_unlocked]
        locked = [a for a in ACHIEVEMENTS if a["id"] not in self.achievements_unlocked]
        
        for a in unlocked + locked:
            if a["id"] in self.achievements_unlocked:
                text.insert(tk.END, f"✓ {a['name']} - Unlocked\n")
            else:
                text.insert(tk.END, f"🔒 {a['name']} - Locked\n")
            text.insert(tk.END, f"   {a['description']}\n\n")
        
        text.config(state=tk.DISABLED)
    
    def _on_close(self):
        """Save game and close window"""
        self._save_game(silent=True)
        self.root.destroy()

def main():
    root = tk.Tk()
    MaximumPCGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
