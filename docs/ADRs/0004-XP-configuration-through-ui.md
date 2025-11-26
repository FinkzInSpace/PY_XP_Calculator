# 4. XP Configuration Through User Interface
date: 11/26/2025
## Status
Accepted
## Context
We have made the calculation code, and the initial User Interface (UI), now we want to add the extensibility for our users to be able to adjust the XP values per item as detailed in the xpConfig without needing to touch the code. However, we do not want to clutter or complicate our easy to use calcluator UI. 

## Decisions

1. **User Interface Tabs**
We will add tabbing to our UI allowing our users to switch between the Calculator, and the Configuration sides of our application. This will remove the over cluttering, and allow for a cleaner, easy to use, and easy to interpret operations. This will be achieved by updating our main_window.py code to include this tabualarized Calculator, and Configuration tabs,  defined as "Session XP Calculator" and the other defined as "XP Configuration". 

2. **Add the UI framework for setting the XP Confguration**
We will use the same Qt principles as defined in ARD-0003 for constructing our UI for the setting of the XP Configuration, however, unlike the calculator that creates an instance of the sessionXpInput, the XP configuration shall be capable of loading the XP configuration from the current setting, then save a new set of XP configuration. Finally, we will also provide the user with a way to reset the XP configuration to the defaulted values from our own code. 

## Consequences
- **Pros**
  - Clear separation between Session Calculator and XP Configuration:
    - Tabs keep things clearly seperate and easy to manage.
    - Can evolve with additional tabs or features as desired on either tab.

- **Cons**
  - Adds a GUI toolkit dependency (`PySide6`), increasing install size and complexity compared to a pure CLI script.
  - Qt Widgets require some boilerplate and understanding of signals/slots.
  - Adds additional complexity to main_window.py, may want to examine breaking out tabs if the code grows larger.