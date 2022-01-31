from dataclasses import dataclass

@dataclass
class Stats:
    """An object representing the current statistics of a user."""

    _user_id: int

    stars: int
    diamonds: int
    coins: int
    user_coins: int
    demons: int
    creator_points: int
    rank: int

    # Icons
    primary_colour: int
    secondary_colour: int
    cube: int # Perhaps maybe make these objects with a nicer api rather than simple numbers.
    ship: int
    ufo: int
    wave: int
    ball: int
    robot: int
    spider: int
    explosion: int
    glow: bool
    display_mode: int # Which of the "forms" should be displayed as the user's main one.
