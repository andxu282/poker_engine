"""
The hole cards that a player holds during play hidden from all other players. Two card objects are kept as instance
variables to represent the hole cards.
"""
class Hole:
    def __init__(self, hole1, hole2):
        self.hole1 = hole1
        self.hole2 = hole2
        self.preflop_value = self.preflop_value()
        self.current_value = self.preflop_value


    def cards(self):
        return [self.hole1, self.hole2]


    def is_suited(self):
        return self.hole1.suit == self.hole2.suit


    def is_pair(self):
        return self.hole1.rank == self.hole2.rank


    def connected(self):
        return self.hole1.rank - self.hole2.rank


    def preflop_value(self):
        return 1


    def current_value(self):
        return self.current_value


    def get_cards(self):
        if self.is_pair():
            print("Pocket " + str(self.hole1.rank) + "s")
        elif self.is_suited():
            print(str(self.hole1.rank) + "-" + str(self.hole2.rank) + " Suited")
        else:
            print(str(str(self.hole1.rank) + "-" + str(self.hole2.rank)) + " Offsuit")


    def print_cards(self):
        print("Your Hole Cards: ")
        print(self.cards())
