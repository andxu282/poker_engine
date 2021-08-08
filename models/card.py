"""
A card with its rank (2-Ace) and suit (Spades, Hearts, Diamonds, Clubs).
"""
from models.rank import Rank
from models.suit import Suit
class Card:
    def __init__(self, rank_str, suit_str):
        self.rank = Rank(rank_str)
        self.suit = Suit(suit_str)


    def rank(self):
        return self.rank


    def suit(self):
        return self.suit


    def __repr__(self):
        return str(self.rank) + " of " + str(self.suit)
