import re

from lib import run
from typing import Any


# AOC DAY 6


DAY = 6


def solve_one(data: str) -> Any:
    data = """Time:      7  15   30
Distance:  9  40  200"""
    time_line, distance_line = data.splitlines()
    times = [int(x) for x in re.findall(r"\d+", time_line)]
    distances = [int(x) for x in re.findall(r"\d+", distance_line)]

    print(times, distances)
    total = 1
    for (time, distance) in zip(times, distances):
        ways = 0
        print(time, distance)
        # each ms held increases speed by 1 mm
        # find how many different ways there are
        for held in range(time + 1):
            remaining_time = time - held
            traveled = remaining_time * held
            if traveled > distance:
                ways += 1
        total *= ways
    print(total)
    return total








def solve_two(data: str) -> Any:
#     data = """Time:      7  15   30
# Distance:  9  40  200"""
    time_line, distance_line = data.splitlines()
    time = int("".join(re.findall(r"\d+", time_line)))
    distance = int("".join(re.findall(r"\d+", distance_line)))
    print(time, distance)
    total = 0
    for held in range(time + 1):
        remaining_time = time - held
        traveled = remaining_time * held
        if traveled > distance:
            total += 1
    print(total)
    assert total == 71503



def main(quiet: bool = False) -> None:
    # run(DAY, 1, solve_one, quiet=quiet)
    run(DAY, 2, solve_two, quiet=quiet)


if __name__ == "__main__":
    main()
