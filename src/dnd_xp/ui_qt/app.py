import sys
from PySide6.QtWidgets import QApplication

from .main_window import MainWindow

def main() -> None:
    """Entry point for the Qt XP Calculator app."""
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    # Start the Qt event loop
    sys.exit(app.exec())

if __name__ == "__main__":
    main()