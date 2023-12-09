import re
from itertools import cycle
from math import lcm
from pprint import pprint

from lib import run
from typing import Any


# AOC DAY 8


DAY = 8


def solve_one(data: str) -> Any:
    #     data = """LLR
    #
    # AAA = (BBB, BBB)
    # BBB = (AAA, ZZZ)
    # ZZZ = (ZZZ, ZZZ)"""

    instructions, route = data.split("\n\n")
    routes = dict()
    pat = re.compile(r"([A-Z]{3})")
    for line in route.splitlines():
        print(line)
        loc, left, right = pat.findall(line)
        routes[loc] = (left, right)

    steps = 0
    cur = "AAA"
    for instruction in cycle(list(instructions)):
        steps += 1
        cur = routes[cur][0 if instruction == "L" else 1]
        if cur == "ZZZ":
            break
    print(steps)
    return steps


def solve_two(data: str) -> Any:
    #     data = """LR
    #
    # 11A = (11B, XXX)
    # 11B = (XXX, 11Z)
    # 11Z = (11B, XXX)
    # 22A = (22B, XXX)
    # 22B = (22C, 22C)
    # 22C = (22Z, 22Z)
    # 22Z = (22B, 22B)
    # XXX = (XXX, XXX)"""
    instructions, route = data.split("\n\n")
    routes = dict()
    pat = re.compile(r"([A-Z0-9]{3})")
    for line in route.splitlines():
        print(line)
        loc, left, right = pat.findall(line)
        routes[loc] = (left, right)

    starting_nodes = [x for x in routes.keys() if x[-1] == "A"]
    all_steps = []
    for node in starting_nodes:
        steps = 0
        cur = node
        for instruction in cycle(list(instructions)):
            steps += 1
            cur = routes[cur][0 if instruction == "L" else 1]
            if cur[-1] == "Z":
                break

        all_steps.append(steps)
    # LCM magic
    result = lcm(*all_steps)
    print(result)
    return result


def main(quiet: bool = False) -> None:
    run(DAY, 1, solve_one, quiet=quiet)
    run(DAY, 2, solve_two, quiet=quiet)


if __name__ == "__main__":
    main()
