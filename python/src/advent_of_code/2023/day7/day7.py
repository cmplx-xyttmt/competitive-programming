from collections import defaultdict
from functools import cmp_to_key
from typing import List, Dict
import sys

input_ = sys.stdin.readline
print_ = sys.stdout.write
flush = sys.stdout.flush


def read_line() -> str:
    return input_().strip()


def read_int() -> int:
    return int(read_line())


def read_strings() -> List[str]:
    return list(read_line().split())


def read_ints():
    return list(map(int, read_line().split()))

def get_card_value(card: str, joker=False):
    if card.isdigit():
        return int(card)
    return {
        'T': 10,
        'J': 11 if not joker else 1,
        'Q': 12,
        'K': 13,
        'A': 14
    }[card]


def convert_hand_to_comparable_list(cards, joker=False):
    return list(map(lambda card: get_card_value(card, joker), cards))


def get_card_count(cards: str):
    occ = defaultdict(int)
    for card in cards:
        occ[card] += 1
    return occ


def get_type_with_joker(cards: str):
    occ = get_card_count(cards)
    if 'J' in occ and occ['J'] < 5:
        # Add all the Js to the most common card
        js = occ.pop('J')
        key = max(occ, key=occ.get)
        occ[key] += js
    return get_type(occ)


def get_type(card_count: Dict[str, int]) -> int:
    # returns 1 (weakest) to 7 (weakest)
    if len(card_count) == 1:
        return 7  # five of a kind
    if len(card_count) == 2:
        if any(map(lambda x: x == 4, card_count.values())):
            return 6  # 4 of a kind
        else:
            return 5  # full house
    if len(card_count) == 3:
        if any(map(lambda x: x == 3, card_count.values())):
            return 4  # three of a kind
        else:
            return 3  # two pair

    if len(card_count) == 4:
        return 2  # one pair

    if len(card_count) == 5:
        return 1  # High card


class Hand:

    def __init__(self, cards: str, bid: int):
        self.cards = cards
        self.type = get_type(get_card_count(cards))
        self.joker_type = get_type_with_joker(cards)
        self.bid = bid

    def __lt__(self, other):
        if self.type == other.type:
            self_str = convert_hand_to_comparable_list(self.cards)
            other_str = convert_hand_to_comparable_list(other.cards)
            return self_str < other_str
        return self.type < other.type

    def __repr__(self):
        return f"{self.cards} -> type: {self.type} joker_type: {self.joker_type}\n"


def cmp(first, second):
    if first < second:
        return -1
    elif first == second:
        return 0
    else:
        return 1

def joker_cmp(hand1: Hand, hand2: Hand):
    if hand1.joker_type == hand2.joker_type:
        hand1_str = convert_hand_to_comparable_list(hand1.cards, joker=True)
        hand2_str = convert_hand_to_comparable_list(hand2.cards, joker=True)
        return cmp(hand1_str, hand2_str)

    return cmp(hand1.joker_type, hand2.joker_type)


def solve():
    hands = []
    line = read_line()
    while line:
        cards, bid = line.split()
        bid = int(bid)
        hands.append(Hand(cards, bid))
        line = read_line()


    hands.sort()
    ans1 = 0
    for i, hand in enumerate(hands):
        ans1 += (i + 1) * hand.bid

    print(f"Part 1: {ans1}")

    ans2 = 0
    hands.sort(key=cmp_to_key(joker_cmp))
    for i, hand in enumerate(hands):
        ans2 += (i + 1) * hand.bid
    print(f"Part 2: {ans2}")


if __name__ == '__main__':
    solve()
