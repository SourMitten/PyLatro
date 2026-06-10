"""Game enumerations"""

from enum import Enum, auto


class Suit(Enum):
    """Card suits"""
    SPADES = auto()
    HEARTS = auto()
    DIAMONDS = auto()
    CLUBS = auto()


class Rank(Enum):
    """Card ranks"""
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14


class ItemRarity(Enum):
    """Rarity levels for items"""
    COMMON = auto()
    UNCOMMON = auto()
    RARE = auto()
    LEGENDARY = auto()


class GameState(Enum):
    """Game states"""
    MAIN_MENU = auto()
    GAMEPLAY = auto()
    SHOP = auto()
    BLIND_SELECT = auto()
    GAME_OVER = auto()
    COLLECTION = auto()
