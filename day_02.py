from lib import run
from typing import Any


# AOC DAY 2


DAY = 2


RED = 12
GREEN = 13
BLUE = 14
MAX = max(RED, GREEN, BLUE)


def solve_one(data: str) -> Any:
    #     data = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    # Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
    # Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
    # Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
    # Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""
    s = 0
    for game in data.splitlines():
        game_with_id, rest = game.split(":")
        game_id = game_with_id.split(" ")[-1]
        print(game_id)
        valid_game = True
        for showing in rest.split(";"):
            for cubes in showing.split(","):
                count, color = cubes.split()
                count = int(count)
                if count > MAX:
                    valid_game = False
                    break

                if color == "red" and count > RED:
                    valid_game = False
                    break

                if color == "green" and count > GREEN:
                    valid_game = False
                    break

                if color == "blue" and count > BLUE:
                    valid_game = False
                    break

        if valid_game:
            s += int(game_id)
    return s


def solve_two(data: str) -> Any:
    # data = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    # Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
    # Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
    # Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
    # Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

    s = 0
    for game in data.splitlines():
        game_with_id, rest = game.split(":")
        game_id = game_with_id.split(" ")[-1]
        print(game_id)
        r, g, b = 0, 0, 0
        for showing in rest.split(";"):
            for cubes in showing.split(","):
                count, color = cubes.split()
                count = int(count)
                if color == "red":
                    r = max(r, count)
                elif color == "green":
                    g = max(g, count)
                elif color == "blue":
                    b = max(b, count)

        power = r * g * b
        s += power

    # assert s == 2286, f"s is {s}"
    return s


def main(quiet: bool = False) -> None:
    run(DAY, 1, solve_one, quiet=quiet)
    run(DAY, 2, solve_two, quiet=quiet)


if __name__ == "__main__":
    main()
