from lib import run
from typing import Any


# AOC DAY 4


DAY = 4


def solve_one(data: str) -> Any:
    #     data = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
    # Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
    # Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
    # Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
    # Card 5: 87 83 26 28  2 | 88 30 70 12 93 22 82  6
    # Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

    s = 0
    for card in data.splitlines():
        card = card.split(":")[-1]
        card, have = card.split("|")
        card = card.strip().split(" ")
        have = have.strip().split(" ")
        card = [c for c in card if c != ""]
        have = [h for h in have if h != ""]
        c = set(card)
        h = set(have)

        u = c & h
        score = 2 ** (len(u) - 1) if len(u) > 0 else 0
        s += score

    return s


def solve_two(data: str) -> Any:
    # data = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
    # Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
    # Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
    # Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
    # Card 5: 87 83 26 28  2 | 88 30 70 12 93 22 82  6
    # Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

    scores = {}
    cards = {}

    data = data.splitlines()
    card_count = len(data)
    for card in data:
        card_no, card = card.split(":")
        card_no = int(card_no.replace("Card ", ""))
        card, have = card.split("|")
        card = card.strip().split(" ")
        have = have.strip().split(" ")
        card = [c for c in card if c != ""]
        have = [h for h in have if h != ""]
        # print(card_no, card, have)
        u = set(card) & set(have)
        score = len(u)
        scores[card_no] = score
        cards[card_no] = 1

    for i in range(1, card_count + 1):
        for n in range(i + 1, i + scores[i] + 1):
            cards[n] += cards[i]

    s = sum(cards.values())
    assert s == 5539496
    return s


def main(quiet: bool = False) -> None:
    run(DAY, 1, solve_one, quiet=quiet)
    run(DAY, 2, solve_two, quiet=quiet)


if __name__ == "__main__":
    main()
