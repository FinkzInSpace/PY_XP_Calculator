from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QFormLayout,
    QHBoxLayout,
    QGroupBox,
    QLabel,
    QSpinBox,
    QCheckBox,
    QPushButton,
    QTabWidget,
    QMessageBox,
)

from dnd_xp.xp_model import xpConfig, sessionXpInput, calculate_xp

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("D&D Session XP Calculator")

        # Use a single config instance (editable via config tab)
        self.config = xpConfig()

        # --- Central Widget & tab widget --- 
        central = QWidget(self)
        self.setCentralWidget(central)

        main_layout = QVBoxLayout()
        central.setLayout(main_layout)

        self.tabs = QTabWidget()
        main_layout.addWidget(self.tabs)

        # --- Build Tabs ---
        self.session_tab = self._build_session_tab()
        self.config_tab = self._build_config_tab()

        self.tabs.addTab(self.session_tab, "Session XP")
        self.tabs.addTab(self.config_tab, "XP Configuration")

    # ----------------------------------------------------------------------
    # Tab 1: Session XP Calculator
    # ----------------------------------------------------------------------
    def _build_session_tab(self) -> QWidget:
        """Create the tab for per-session XP calulation."""
        tab = QWidget()
        layout = QVBoxLayout()
        tab.setLayout(layout)

       # --- Encounters group ---
        encounters_group = QGroupBox("Encounters")
        encounters_layout =  QFormLayout()
        encounters_group.setLayout(encounters_layout)

        self.easy_spin = QSpinBox()
        self.moderate_spin = QSpinBox()
        self.hard_spin = QSpinBox()
        self.impossible_spin = QSpinBox()

        for spin in (self.easy_spin, self.moderate_spin, self.hard_spin, self.impossible_spin):
            spin.setMinimum(0)
            spin.setMaximum(99)

        encounters_layout.addRow("Easy:", self.easy_spin)
        encounters_layout.addRow("Moderate:", self.moderate_spin)
        encounters_layout.addRow("Hard:", self.hard_spin)
        encounters_layout.addRow("Impossible:", self.impossible_spin)

        # --- Lore Group ---
        lore_group = QGroupBox("Lore")
        lore_layout = QFormLayout()
        lore_group.setLayout(lore_layout)

        self.new_lore_spin = QSpinBox()
        self.enchanced_lore_spin = QSpinBox()

        for spin in (self.new_lore_spin, self.enchanced_lore_spin):
            spin.setMinimum(0)
            spin.setMaximum(99)
        
        lore_layout.addRow("New Lore:", self.new_lore_spin)
        lore_layout.addRow("Enhanced Lore:", self.enchanced_lore_spin)

        # --- Questing group ---
        quest_group = QGroupBox("Questing")
        quest_layout = QFormLayout()
        quest_group.setLayout(quest_layout)

        self.side_quests_spin = QSpinBox()
        self.side_quests_spin.setMinimum(0)
        self.side_quests_spin.setMaximum(99)

        self.followed_plot_check = QCheckBox("Followed the Plot")

        quest_layout.addRow("Completed Side Quests:", self.side_quests_spin)
        quest_layout.addRow(self.followed_plot_check)

        # --- Bottom: calculate button + result label ---

        bottom_layout = QHBoxLayout()
        self.calculate_button = QPushButton("Calculate XP")
        self.result_label = QLabel("Total XP: 0")

        bottom_layout.addWidget(self.calculate_button)
        bottom_layout.addWidget(self.result_label)

        # --- Add groups to tab layout ---
        layout.addWidget(encounters_group)
        layout.addWidget(lore_group)
        layout.addWidget(quest_group)
        layout.addLayout(bottom_layout)

        # --- Wire up signal -> slot ---
        self.calculate_button.clicked.connect(self.on_calculate_clicked)

        return tab

    def on_calculate_clicked(self) -> None:
        """Collect inputs, call calculate_xp, and update the result label."""
        session = sessionXpInput(
            easy_encounters=self.easy_spin.value(),
            moderate_encounters=self.moderate_spin.value(),
            hard_encounters=self.hard_spin.value(),
            impossible_encounters=self.impossible_spin.value(),
            new_lore=self.new_lore_spin.value(),
            enhanced_lore=self.enchanced_lore_spin.value(),
            side_quests_completed=self.side_quests_spin.value(),
            followed_plot=self.followed_plot_check.isChecked(),
        )
        total_xp = calculate_xp(self.config, session)
        self.result_label.setText(f"Total XP: {total_xp}")
    # ----------------------------------------------------------------------
    # Tab 2: XP Configuration
    # ----------------------------------------------------------------------
    def _build_config_tab(self) -> QWidget:
        """Create the tab for editing xpConfig values."""
        tab = QWidget()
        layout = QVBoxLayout()
        tab.setLayout(layout)

        # Group: Encounters XP
        encounters_group = QGroupBox("Encounter XP Values")
        encounters_layout = QFormLayout()
        encounters_group.setLayout(encounters_layout)

        self.cfg_easy_spin = QSpinBox()
        self.cfg_moderate_spin = QSpinBox()
        self.cfg_hard_spin = QSpinBox()
        self.cfg_impossible_spin = QSpinBox()

        for spin in (self.cfg_easy_spin, self.cfg_moderate_spin, self.cfg_hard_spin, self.cfg_impossible_spin):
            spin.setMinimum(0)
            spin.setMaximum(10000)

        encounters_layout.addRow("Easy XP:", self.cfg_easy_spin)
        encounters_layout.addRow("Moderate XP:", self.cfg_moderate_spin)
        encounters_layout.addRow("Hard XP:", self.cfg_hard_spin)
        encounters_layout.addRow("Impossible XP:", self.cfg_impossible_spin)

        # Group: Lore XP
        lore_group = QGroupBox("Lore XP Values")
        lore_layout = QFormLayout()
        lore_group.setLayout(lore_layout)

        self.cfg_new_lore_spin = QSpinBox()
        self.cfg_enhanced_lore_spin = QSpinBox()

        for spin in (self.cfg_new_lore_spin, self.cfg_enhanced_lore_spin):
            spin.setMinimum(0)
            spin.setMaximum(10000)

        lore_layout.addRow("New Lore XP:", self.cfg_new_lore_spin)
        lore_layout.addRow("Enhanced Lore XP:", self.cfg_enhanced_lore_spin)

        # Group: Questing XP
        quest_group = QGroupBox("Quest XP Values")
        quest_layout = QFormLayout()
        quest_group.setLayout(quest_layout)

        self.cfg_followed_plot_spin = QSpinBox()
        self.cfg_per_side_quest_spin = QSpinBox()

        for spin in (self.cfg_followed_plot_spin, self.cfg_per_side_quest_spin):
            spin.setMinimum(0)
            spin.setMaximum(10000)
        
        quest_layout.addRow("Followed Plot XP:", self.cfg_followed_plot_spin)
        quest_layout.addRow("Per Side Quest XP:", self.cfg_per_side_quest_spin)

        # Bottom buttons: Apply & Reset
        buttons_layout = QHBoxLayout()
        self.apply_config_button = QPushButton("Apply Changes")
        self.reset_config_button = QPushButton("Reset to Defaults")

        buttons_layout.addWidget(self.apply_config_button)
        buttons_layout.addWidget(self.reset_config_button)

        # Add groups & buttons to layout tab
        layout.addWidget(encounters_group)
        layout.addWidget(lore_group)
        layout.addWidget(quest_group)
        layout.addLayout(buttons_layout)

        # Initialize widgets from current config
        self._load_config_into_widgets()

        # Wire buttons 
        self.apply_config_button.clicked.connect(self.on_apply_config_clicked)
        self.reset_config_button.clicked.connect(self.on_reset_config_clicked)

        return tab

    def _load_config_into_widgets(self) -> None:
        """Populate config tab spinboxes from self.config."""
        self.cfg_easy_spin.setValue(self.config.xp_easy)
        self.cfg_moderate_spin.setValue(self.config.xp_moderate)
        self.cfg_hard_spin.setValue(self.config.xp_hard)
        self.cfg_impossible_spin.setValue(self.config.xp_impossible)

        self.cfg_new_lore_spin.setValue(self.config.xp_new_lore)
        self.cfg_enhanced_lore_spin.setValue(self.config.xp_enhanced_lore)

        self.cfg_followed_plot_spin.setValue(self.config.xp_followed_plot)
        self.cfg_per_side_quest_spin.setValue(self.config.xp_per_side_quest)

    def on_apply_config_clicked(self) -> None:
        """Update the slef.config from the config tab widget."""
        self.config.xp_easy = self.cfg_easy_spin.value()
        self.config.xp_moderate = self.cfg_moderate_spin.value()
        self.config.xp_hard = self.cfg_hard_spin.value()
        self.config.xp_impossible = self.cfg_impossible_spin.value()

        self.config.xp_new_lore = self.cfg_new_lore_spin.value()
        self.config.xp_enhanced_lore = self.cfg_enhanced_lore_spin.value()

        self.config.xp_followed_plot = self.cfg_followed_plot_spin.value()
        self.config.xp_per_side_quest = self.cfg_per_side_quest_spin.value()

        QMessageBox.information(
            self,
            "XP Config Updated",
            "XP Configuration has been updated. \n"
            "New values will be used for future calculations.",
        )
    def on_reset_config_clicked(self) -> None:
        """ Reset config to defaults and update widgets."""
        self.config = xpConfig()
        self._load_config_into_widgets()

        QMessageBox.information(
            self,
            "XP Config Reset",
            "XP configuration has been reset to default values.",
        )