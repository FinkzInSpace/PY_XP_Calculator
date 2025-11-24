import pytest
from xp_model import XpConfig, SessionXpInput, calculate_xp


def test_easy_encounter_uses_easy_xp_value():
    config = XpConfig(xp_easy=50)
    session = SessionXpInput(easy_encounters=1)

    total = calculate_xp(config, session)

    assert total == 50


def test_mix_of_encounters_lore_and_quests():
    config = XpConfig()
    session = SessionXpInput(
        easy_encounters=1,        # 1 * 50 = 50
        moderate_encounters=2,    # 2 * 100 = 200
        hard_encounters=1,        # 1 * 150 = 150
        new_lore=2,               # 2 * 30 = 60
        enhanced_lore=1,          # 1 * 20 = 20
        side_quests_completed=1,  # 1 * 50 = 50
        followed_plot=True        # 25
    )

    total = calculate_xp(config, session)

    # 50 + 200 + 150 + 60 + 20 + 50 + 25 = 555
    assert total == 555


def test_followed_plot_false_gives_no_plot_xp():
    config = XpConfig()
    session = SessionXpInput(followed_plot=False)

    total = calculate_xp(config, session)

    assert total == 0


def test_custom_config_changes_result():
    config = XpConfig(
        xp_easy=10,
        xp_moderate=20,
        xp_hard=30,
        xp_impossible=40,
        xp_new_lore=5,
        xp_enhanced_lore=3,
        xp_followed_plot=7,
        xp_per_side_quest=11,
    )

    session = SessionXpInput(
        easy_encounters=1,
        moderate_encounters=1,
        hard_encounters=0,
        impossible_encounters=0,
        new_lore=1,
        enhanced_lore=1,
        side_quests_completed=1,
        followed_plot=True,
    )

    total = calculate_xp(config, session)

    # 10 + 20 + 5 + 3 + 11 + 7 = 56
    assert total == 56
