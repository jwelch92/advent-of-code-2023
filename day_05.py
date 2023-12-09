import re
from pprint import pprint

from lib import run, chunks
from typing import Any


# AOC DAY 5


DAY = 5


def lookup(v, maps):
    val = v
    for m in maps:
        val = next(
            (dr.start + (val - sr.start) for sr, dr in m.items() if val in sr), val
        )
    return val


def reverse_lookup(v, maps):
    val = v
    for m in reversed(maps):
        val = next(
            (sr.start + (val - dr.start) for sr, dr in m.items() if val in dr), val
        )
    return val


def solve_one(data: str) -> Any:
    data = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""

    seeds, *maps = data.split("\n\n")
    print(seeds)
    pprint(maps)

    seeds = set(map(int, re.findall(r"\d+", seeds)))
    print(seeds)
    t = []
    for m in maps:
        y = dict()
        _, *mappings = m.splitlines()
        print(mappings)
        for s in mappings:
            dest, src, length = map(int, s.split(" "))
            y[range(src, src + length)] = range(dest, dest + length)
        t.append(y)
    pprint(t)

    locs = [lookup(x, t) for x in seeds]
    print(locs)
    ans = min(locs)
    print(ans)
    return ans


def solve_two(data: str) -> Any:
    #     data = """seeds: 79 14 55 13
    #
    # seed-to-soil map:
    # 50 98 2
    # 52 50 48
    #
    # soil-to-fertilizer map:
    # 0 15 37
    # 37 52 2
    # 39 0 15
    #
    # fertilizer-to-water map:
    # 49 53 8
    # 0 11 42
    # 42 0 7
    # 57 7 4
    #
    # water-to-light map:
    # 88 18 7
    # 18 25 70
    #
    # light-to-temperature map:
    # 45 77 23
    # 81 45 19
    # 68 64 13
    #
    # temperature-to-humidity map:
    # 0 69 1
    # 1 0 69
    #
    # humidity-to-location map:
    # 60 56 37
    # 56 93 4"""

    seeds, *maps = data.split("\n\n")
    print(seeds)
    pprint(maps)

    seeds = [int(c) for c in re.findall(r"\d+", seeds)]
    print(seeds)
    t = []
    for m in maps:
        y = dict()
        _, *mappings = m.splitlines()
        print(mappings)
        for s in mappings:
            dest, src, length = map(int, s.split(" "))
            y[range(src, src + length)] = range(dest, dest + length)
        t.append(y)
    pprint(t)

    seed_ranges = []
    for se in chunks(seeds, 2):
        start, ln = se
        seed_ranges.append(range(start, start + ln))

    # this is way too slow and takes too long to bruteforce. Interesting approximation technique used here: https://github.com/mmdoogie/adventofcode2023/blob/main/aoc_2023_05.py
    loc = 0
    while True:
        potential_seed = reverse_lookup(loc, t)
        if any(potential_seed in sr for sr in seed_ranges):
            print(loc)
            break
        loc += 1


def main(quiet: bool = False) -> None:
    run(DAY, 1, solve_one, quiet=quiet)
    run(DAY, 2, solve_two, quiet=quiet)


if __name__ == "__main__":
    main()
