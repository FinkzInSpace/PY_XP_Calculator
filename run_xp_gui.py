# run_xp_gui.py
import sys
from pathlib import Path

# Compute src/ path relative to this file
project_root = Path(__file__).resolve().parent
src_path = project_root / "src"
sys.path.insert(0, str(src_path))

from dnd_xp.ui_qt.app import main

if __name__ == "__main__":
    main()
