# tests/conftest.py
import sys
from pathlib import Path

# project_root = .../project_root
project_root = Path(__file__).resolve().parents[1]
src_path = project_root / "src"

# Put src/ at the front of sys.path so `import dnd_xp` works
sys.path.insert(0, str(src_path))