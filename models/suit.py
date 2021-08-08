"""
Suit of a card (Spades, Hearts, Diamonds, Clubs). Represented by a single character string of the first letter of the
suit.
"""
from helpers.constants import suit_dict
class Suit():
    def __init__(self, suit_str):
        self.suit_str = suit_str


    def __str__(self):
        return suit_dict[self.suit_str]


    def __eq__(self, other):
        return self.suit_str == other.suit_str