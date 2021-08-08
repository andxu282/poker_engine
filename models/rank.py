"""
The rank of the card (2 through Ace). The rank is represented by a single character string (the number itself for 2-9
and T, J, Q, K, A for 10, Jack, Queen, King, and Ace respectively.
"""
from helpers.constants import rank_dict
class Rank():
    def __init__(self, rank_str):
        self.rank_str = rank_str


    def __str__(self):
        return rank_dict[self.rank_str]


    def __eq__(self, other):
        return self.rank_str == other.rank_str

    def get_rank(self):
        return self.rank_str