# 2. Testing layout and strategy
Date: 11/24/2025
## Status
Accepted
## Context
We are building a D&D XP calculator in Python, with a Qt UI now and a possible web UI later.
We want confidence that changes to the XP rules do not silently break behavior, and we want to
keep domain logic reusable across UIs.

## Decision

- Store production code and tests separately:
  - Production module: `xp_model.py`
  - Test module(s) under `tests/`, e.g. `tests/test_xp_model.py`.
- Use `pytest` as the test runner.
- Write tests that:
  - Verify XP calculation for typical mixes of encounters, lore, and quests.
  - Verify that changing `XpConfig` values affects results as expected.
- Avoid putting significant test logic inside `if __name__ == "__main__":` blocks.

## Consequences

- **Pros**
  - Clear separation between functional code and tests.
  - Easy to run all tests with a single `pytest` command.
  - Supports refactoring and future UI layers without fear of breaking XP logic.

- **Cons**
  - Slightly more project structure than a single-file script.
  - Requires learning and maintaining a minimal test framework (pytest).
