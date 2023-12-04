from lib import run
from typing import Any, Iterator

# AOC DAY 1


DAY = 1


def solve_one(data: str) -> Any:
    s = 0
    lines = data.splitlines()
    for l in lines:
        l = list(filter(str.isdigit, l))
        s += int(f"{l[0]}{l[-1]}")
    return s


def find_all(s: str, sub: str) -> Iterator[int]:
    start = 0
    while True:
        start = s.find(sub, start)
        if start == -1:
            return
        yield start
        start += 1


def solve_two(data: str) -> Any:
    # replace with word to account for overlapping word digits
    mapping = {
        "zero": "zero0zero",
        "one": "one1one",
        "two": "two2two",
        "three": "three3three",
        "four": "four4four",
        "five": "five5five",
        "six": "six6six",
        "seven": "seven7seven",
        "eight": "eight8eight",
        "nine": "nine9nine",
    }

    s = 0
    lines = data.splitlines()
    for l in lines:
        for k, v in mapping.items():
            l = l.replace(k, v)
        l = list(filter(str.isdigit, l))
        s += int(l[0] + l[-1])
    return s


def main(quiet: bool = False) -> None:
    # run(DAY, 1, solve_one, quiet=quiet)
    run(DAY, 2, solve_two, quiet=quiet)


if __name__ == "__main__":
    main()
