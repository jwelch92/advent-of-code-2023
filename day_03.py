from pprint import pprint

from lib import run, build_grid, neighbors_fn
from typing import Any


# AOC DAY 3


DAY = 3


def solve_one(data: str) -> Any:
    #     data = """467..114..
    # ...*......
    # ..35..633.
    # ......#...
    # 617*.......
    # .....+.58.
    # ..592.....
    # ......755.
    # ...$.*....
    # .664.598.."""

    g, h, w, points, values = build_grid(data, split_fn=lambda x: list(x))
    print(g[0])
    print(f"{h=} {w=}")
    # pprint(points)
    part_nos = []
    nfn = neighbors_fn(h, w, True)
    nums = set("1234567890")

    total = 0

    for line_idx, line in enumerate(g):
        for col_idx, col in enumerate(line):
            if (
                points[col_idx, line_idx] in nums
                and not points.get((col_idx - 1, line_idx), ".") in nums
            ):
                x2 = col_idx
                t = ""
                part_no = False
                while points.get((x2, line_idx), ".") in nums:
                    t += points[x2, line_idx]
                    for nx, ny in nfn((x2, line_idx)):
                        if not points[nx, ny] in {".", "0"} | nums:
                            part_no = True
                    x2 += 1
                if part_no:
                    total += int(t)

            # print(cur_num)
            # if col.isdigit():
            #     cur_num += col
            #     # find neighbors
            #
            #     if is_part_no:
            #         continue
            #
            #     print(f"{col} is a number")
            #     neighbors = nfn((col_idx, line_idx))
            #     for (nx, ny) in neighbors:
            #         print(f"neighbor {nx=} {ny=} is {g[ny][nx]}")
            #         p = g[ny][nx]
            #         if not p.isdigit() and p != ".":
            #             is_part_no = True
            #             break
            #
            # else:
            #     if is_part_no:
            #         part_nos.append(cur_num)
            #         is_part_no = False
            #
            #     cur_num = ""

    assert total == 4361, f"Total is {total}"
    return total


def solve_two(data: str) -> Any:
    pass


def main(quiet: bool = False) -> None:
    run(DAY, 1, solve_one, quiet=quiet)
    run(DAY, 2, solve_two, quiet=quiet)


if __name__ == "__main__":
    main()
