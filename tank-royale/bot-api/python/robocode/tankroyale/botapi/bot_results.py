""" robocode.tankroyal.botapi.bot_results """

from dataclasses import dataclass


@dataclass(frozen=True)
class BotResults:
    """
    BotResults class

    Args:
        rank: The rank/placement of the bot.
        survival: The survival score.
        last_survivor_bonus: The last survivor score.
        bullet_damage: The bullet damage score.
        bullet_kill_bonus: The bullet kill bonus.
        ram_damage: The ram damage score.
        ram_kill_bonus: The ram kill bonus.
        total_score: The total score.
        first_places: The number of 1st places.
        second_places: The number of 2nd places.
        third_place: The number of 3rd places.
    """

    rank: int
    survival: float
    last_survivor_bonus: float
    bullet_damage: float
    bullet_kill_bonus: float
    ram_damage: float
    ram_kill_bonus: float
    total_score: float
    first_places: float
    second_places: float
    third_places: float