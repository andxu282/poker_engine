import unittest
from models.card import Card
from helpers.hand_checker import is_one_pair, is_two_pair, is_three_of_a_kind, is_straight, is_flush, is_full_house, \
    is_four_of_a_kind, is_straight_flush

class TestHandChecker(unittest.TestCase):

    def test_is_one_pair(self):
        one_pair = [Card("A", "S"), Card("A", "C"), Card("T", "S"), Card("9", "S"), Card("8", "S")]
        self.assertTrue(is_one_pair(one_pair))

    def test_is_two_pair(self):
        two_pair = [Card("A", "S"), Card("A", "C"), Card("T", "S"), Card("T", "C"), Card("8", "S")]
        self.assertTrue(is_two_pair(two_pair))

    def test_is_three_of_a_kind(self):
        three_of_a_kind = [Card("A", "S"), Card("A", "C"), Card("A", "D"), Card("T", "C"), Card("8", "S")]
        self.assertTrue(is_three_of_a_kind(three_of_a_kind))

    def test_is_straight(self):
        straight = [Card("A", "S"), Card("2", "C"), Card("3", "D"), Card("4", "C"), Card("5", "S")]
        self.assertTrue(is_straight(straight))

    def test_is_flush(self):
        flush = [Card("A", "S"), Card("8", "S"), Card("3", "S"), Card("4", "S"), Card("5", "S")]
        self.assertTrue(is_flush(flush))

    def test_is_full_house(self):
        full_house = [Card("A", "S"), Card("A", "C"), Card("A", "D"), Card("T", "C"), Card("T", "S")]
        self.assertTrue(is_full_house(full_house))

    def test_is_four_of_a_kind(self):
        four_of_a_kind = [Card("A", "S"), Card("A", "C"), Card("A", "D"), Card("A", "H"), Card("8", "S")]
        self.assertTrue(is_four_of_a_kind(four_of_a_kind))

    def test_is_straight_flush(self):
        straight_flush = [Card("A", "S"), Card("2", "S"), Card("3", "S"), Card("4", "S"), Card("5", "S")]
        self.assertTrue(is_straight_flush(straight_flush))

    if __name__ == '__main__':
        unittest.main()
