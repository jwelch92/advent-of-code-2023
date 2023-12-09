from lib import run
from typing import Any


# AOC DAY 9


DAY = 9


def solve_one(data: str) -> Any:
    #     data = """0 3 6 9 12 15
    # 1 3 6 10 15 21
    # 10 13 16 21 30 45"""
    total = 0
    for line in data.splitlines():
        diffs = []
        d = [int(x) for x in line.split(" ")]
        # d.append(0)
        diffs.append(d)
        while not all(x == 0 for x in diffs[-1]):
            diffs.append([i2 - i1 for i1, i2 in zip(diffs[-1], diffs[-1][1:])])

            # print(diffs)
        prediction = 0
        while diffs:
            d = diffs.pop()
            prediction += d[-1]

        print(prediction)
        total += prediction
    print(total)
    return total


def solve_two(data: str) -> Any:
    #     data = """0 3 6 9 12 15
    # 1 3 6 10 15 21
    # 10 13 16 21 30 45"""
    total = 0
    for line in data.splitlines():
        diffs = []
        d = [int(x) for x in line.split(" ")]
        d.reverse()
        # d.append(0)
        diffs.append(d)
        while any(diffs[-1]):
            diffs.append([i2 - i1 for i1, i2 in zip(diffs[-1], diffs[-1][1:])])

            # print(diffs)
        prediction = 0
        while diffs:
            d = diffs.pop()
            prediction += d[-1]

        print(prediction)
        total += prediction
    print(total)
    return total


def main(quiet: bool = False) -> None:
    # run(DAY, 1, solve_one, quiet=quiet)
    run(DAY, 2, solve_two, quiet=quiet)


if __name__ == "__main__":
    main()
