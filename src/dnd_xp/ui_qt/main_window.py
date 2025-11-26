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
)

from dnd_xp.xp_model import xpConfig, sessionXpInput, calculate_xp

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("D&D Session XP Calculator")

        # Use a single config instance (you can later make this editable)
        self.config = xpConfig()

        # --- Central Widget & Main Layout --- 
        central = QWidget(self)
        self.setCentralWidget(central)

        main_layout = QVBoxLayout()
        central.setLayout(main_layout)

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

        # --- Add groups to main layout ---
        main_layout.addWidget(encounters_group)
        main_layout.addWidget(lore_group)
        main_layout.addWidget(quest_group)
        main_layout.addLayout(bottom_layout)

        # --- Wire up signal -> slot ---
        self.calculate_button.clicked.connect(self.on_calculate_clicked)

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
