# 1. XP Model and Architecure
Date: 11/24/2025
## Status
Accepted

## Context
As a TTRPG dungeon master (DM), I want to run a game using experience points (XP) that is not ONLY considering combat as a mechanic to provide players with XP, but considers social encounters, and generic situations, such as skill challenges, all under the category of an Encounter.  
Encounters shall be weighted as Easy, Moderate, Hard, or Impossible, with the DM able to adjust the XP that is offered for each of these encounter categories.  
Additionally we want to reward players for discoveries and growing discoveries aka LORE. 
Finally whether players finish side quests, or follow the plot, this should provide them some additional XP for their progress. </br>

Summary of user desirements:
- Rewards encounters (combat or social) by difficulty tier.
- Rewards discovering and expanding lore.
- Provides small incentives for following the main plot.
- Rewards completing side quests.
- Can be tuned per campaign.
- Starts as a local Python + Qt app but should be easy to reuse in a future web-based UI.
To keep the project maintainable and adaptable, the XP rules should not be tightly coupled to any particular UI technology.

## Decision(s)
1. **Seperate domain logic from UI**
  - Implement all XP rules in a small, pure Python module (`xp_model.py`).
     - The module exposes:
       - `XpConfig` – configurable XP values.
       - `SessionXpInput` – inputs describing a single session.
       - `calculate_xp(config, session)` – pure function returning an integer XP value.
  
     - The Qt application will import and call these objects instead of embedding XP math directly in UI code.
     - Future web frontends (e.g., FastAPI, Flask, or a JS frontend calling a Python backend) can reuse the same `xp_model.py` without modification.
   
2. **Adopt a baseline XP spread**
   - Encounters:
       - Easy: 50 XP
       - Moderate: 100 XP
       - Hard: 150 XP
       - Impossible: 225 XP
  
     - Lore:
       - New Lore: 30 XP
       - Enhanced Lore: 20 XP
  
     - Questing:
       - Followed Plot: 25 XP (flat per session)
       - Completed Side Quest: 50 XP per quest
  
     - These defaults are intended to:
       - Keep encounters as the main XP source (D&D-like).
       - Make lore meaningfully rewarding without overshadowing challenges.
       - Provide small nudges for plot adherence and steady rewards for side quests.
      
3. **Configuration Strategy**
   - The XP values live in 'XPconfig' with sensible defaults.
   - The UI will allow editing of these values (later ADRs will define how).
   - XP calculation remains a pure function for testability.

## Consequences

- **Pros**
  - XP logic is easy to test and reason about in isolation.
  - The Qt UI layer can stay lightweight and focused on user interaction.
  - Reuse is straightforward for future web or CLI tools.
  - XP tuning can be done by adjusting `XpConfig` without changing logic code.

- **Cons**
  - Requires an initial discipline to keep UI code from “re-implementing” XP logic.
  - Some extra boilerplate (dataclasses and DTO-like structures) compared to an all-in-one script.

- **Follow-up ADRs (planned)**
  - ADR-0002: Choose specific Qt binding (e.g., PySide6).
  - ADR-0003: Decide on config persistence (JSON/YAML file vs. hard-coded defaults).
  - ADR-0004: UI layout and interactions for the desktop app.
