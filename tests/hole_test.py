from models.hole import Hole
from models.card import Card
player1 = Hole(Card("A", "S"), Card("A", "C"))
player1.print_cards()
player1.get_cards()