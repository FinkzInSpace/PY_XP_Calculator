from dataclasses import dataclass

@dataclass
class xpConfig:
  """Configureable XP values for the calculator."""
  # Encounters
  xp_easy: int = 50
  xp_moderate: int = 100
  xp_hard: int = 150
  xp_impossible: int = 225
  
  # Lore
  xp_new_lore: int = 50
  xp_enhanced_lore: int = 30

  # Questing
  xp_followed_plot: int = 25
  xp_per_side_quest: int = 100

@dataclass
class sessionXpInput:
  """Inputs representing what happend in a single session."""
  easy_encounters: int = 0
  moderate_encounters: int = 0
  hard_encounters: int = 0
  impossible_encounters: int = 0
  new_lore: int = 0
  enhanced_lore: int = 0
  side_quests_completed: int = 0
  followed_plot: bool = False

def calculate_xp(config: xpConfig, session: sessionXpInput) -> int:
    """ 
    Calculate total XP to award per player for a session.
    You can divide by party size or apply multipliers outside this function
    if you want party-based XP instead.
    """
  encounter_xp = (
    session.easy_encounters * config.xp_easy + session.moderate_encounters * config.xp_moderate + session.hard_encounters * config.xp_hard + session.impossible_encounters * config.xp_impossible
  )
lore_xp = (
  session.new_lore * config.xp_new_lore + session.enhanced_lore + config.xp_enhanced_lore
)
quest_xp = (
  session.side_quests_completed * config.xp_per_side_quest + (config.xp_followed_plot if session.followed_plot else 0)
)

return encounter_xp + lore_xp + quest_xp

if __name__ == "__main__":
  # small manual test / example
  config = xpConfig()
  session = sessionXpInput(
    easy_encounters=1,
        moderate_encounters=2,
        hard_encounters=1,
        new_lore=2,
        enhanced_lore=1,
        side_quests_completed=1,
        followed_plot=True,
  )

total_xp = calculate_xp(config, session)
print(f"Total XP per player for this session: {total_xp}")
