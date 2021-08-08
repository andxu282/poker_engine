from helpers.constants import card_dict, straight_list


def compare_cards(card):
    return card_dict[card.rank.get_rank()]


def _same_count(cards):
    same_count = 0
    for i in range(len(cards) - 1):
        for j in range(i + 1, len(cards)):
            card1 = cards[i]
            card2 = cards[j]
            if (card1.rank == card2.rank):
                same_count += 1
    return same_count

def is_one_pair(cards):
    same_count = _same_count(cards)
    return same_count == 1

def is_two_pair(cards):
    same_count = _same_count(cards)
    return same_count == 2

def is_three_of_a_kind(cards):
    same_count = _same_count(cards)
    return same_count == 3

def is_straight(cards):
    cards.sort(key=compare_cards)
    return [card_dict[card.rank.get_rank()] for card in cards] in straight_list

def is_flush(cards):
    suits = []
    for card in cards:
        suits.append(card.suit)
    return suits[0] == suits[1] and suits[1] == suits[2] and suits[2] == suits[3] and suits[3] == suits[4]

def is_full_house(cards):
    same_count = _same_count(cards)
    return same_count == 4

def is_four_of_a_kind(cards):
    same_count = _same_count(cards)
    return same_count == 6

def is_straight_flush(cards):
    return is_straight(cards) and is_flush(cards)
