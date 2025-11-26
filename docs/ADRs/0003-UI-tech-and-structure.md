# 3. UI technology and structure for desktop app
date: 11/24/2025
## Status
Accepted
## Context
We want a local, desktop XP calculator UI that:
 - Runs on the user's machine without a server.
 - Is implemented in Python.
 - Can be evolved later into a web-based experience without rewriting core logic.
 - Is simple enough for a learning-oriented project, but structured enough to grow.

We already have:

 - Isolated XP rules in our xp_model.py (See ADR-0001).
 - Set up tests under 'tests/' using pytest (see - ADR-0002)

We now need to choose a specific UI framework anddecide how it will talk to the XP model.

## Decision(s)

1. **Use Qt PySide6 for the desktop UI**
  - We will implement the desktop application using **PySide6** (Qt for Python).
  - Rationale:
    - Official Qt for Python binding, actively maintained.
    - widely used, good docs and examples.
    - Cross-platform (Windows, MacOS, Linux).
    - Works well with the "src/ package + tests" layout we already have.
 - The project will add a runtime dependecy on 'PySide6'.

 2. **Use Qt Widgets (not QML) for the initial version**
 - We will build the UI using traditional Qt Widgets:
    - A main Window
    - Standard input widgets ('QSpinBox', 'QCheckBox', 'QPushButton', 'QLabel')
 - Reasons:
    - Simpler to learn and reason about for a small tool
    - Plenty of examples, easier to wire up to Python logic.
    - QML/QtQuick is powerful but adds complexity we don't need yet.

3. **Keep the Ui Layer thin and call into the domain model**
 - New UI code will live under, 'src/dnd_xp/ui_qt'
 - The UI will:
    - Read user inputs (encounter counts, lore counts, side quests, plot toggle).
    - Construct a 'sessionXpInput' instance.
    - Use an 'xpConfig' instance (with defaults or configurable values).
    - Call 'calculate_xp(config, session)' from 'xp_model.py'.
    - Display the resulting XP in the UI.
 - The UI **will not** implement XP math itself; that lives only in 'xp_model.py'.

4. **Entry point**
 - A small 'app.py' (or '__main__.py') module will serve as the UI entry point:
         ```bash
     python -m dnd_xp.ui_qt.app
     ```

   - This module will:
     - Create a `QApplication`.
     - Create and show the main window.
     - Start the Qt event loop.

## Consequences
- **Pros**
  - Clear separation between UI and XP logic:
    - XP logic is reusable by tests, CLI tools, or a future web backend.
    - UI can evolve (new layout, themes, even QML later) with minimal changes to the domain layer.
  - PySide6 + Qt Widgets is a stable, well-documented tech stack.
  - The project structure scales: we can add `ui_web/` later while reusing `xp_model.py`.

- **Cons**
  - Adds a GUI toolkit dependency (`PySide6`), increasing install size and complexity compared to a pure CLI script.
  - Qt Widgets require some boilerplate and understanding of signals/slots.
  - We are not using QML/QtQuick, which might be preferable for highly dynamic or animated UIs; switching later would require some rewrite of the UI layer.

## Next Steps

- Implement `src/dnd_xp/ui_qt/app.py` with a minimal Qt bootstrap.
- Implement `src/dnd_xp/ui_qt/main_window.py`:
  - Input widgets for:
    - Easy/Moderate/Hard/Impossible encounters
    - New / Enhanced lore
    - Side quests completed
    - Followed Plot (checkbox)
  - A “Calculate XP” button
  - A label that displays the total XP using `calculate_xp`.
- Add a small ADR for configuration persistence if/when we allow editing `xpConfig` via the UI.