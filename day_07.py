import functools
from pprint import pprint

from lib import run
from typing import Any


# AOC DAY 7


DAY = 7


CARDS = dict(zip("23456789TJQKA", range(2, 15)))
print(CARDS)


def hand_type(hand):
    return sorted(map(hand.count, hand), reverse=True)

def score_hand(line, replace_faces = "ABCDE"):
    hand, bid = line.split(" ")
    # replace with lexicographically sortable chars
    hand = hand.translate(str.maketrans('TJQKA', replace_faces))
    ht = max(hand_type(hand.replace('0', c)) for c in hand)
    return ht, hand, int(bid)

def solve_one(data: str) -> Any:
#     data = """32T3K 765
# T55J5 684
# KK677 28
# KTJJT 220
# QQQJA 483
# """

    d = [
        x for x in enumerate(sorted(map(score_hand, data.splitlines())), start=1)
    ]

    total = sum(i*s[-1] for i, s in d)
    print(total)
    return total


def solve_two(data: str) -> Any:
#     data = """32T3K 765
# T55J5 684
# KK677 28
# KTJJT 220
# QQQJA 483
# """

    d = [
        x for x in enumerate(sorted(map(functools.partial(score_hand, replace_faces="A0CDE"), data.splitlines())), start=1)
    ]

    total = sum(i*s[-1] for i, s in d)
    print(total)
    return total


def main(quiet: bool = False) -> None:
    run(DAY, 1, solve_one, quiet=quiet)
    run(DAY, 2, solve_two, quiet=quiet)


if __name__ == "__main__":
    main()
