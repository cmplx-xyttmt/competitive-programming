from copy import deepcopy
from typing import List
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


def tilt(grid: List[str], direction: str):
    new_grid = [list(row) for row in grid]
    if direction == "north":
        next_free = [0] * len(new_grid[0])
        row_range = range(len(new_grid))
        col_range = range(len(new_grid[0]))
        add = 1
    elif direction == "south":
        next_free = [len(grid) - 1] * len(new_grid[0])
        row_range = range(len(new_grid) - 1, -1, -1)
        col_range = range(len(new_grid[0]))
        add = -1
    elif direction == "east":
        next_free = [len(grid[0]) - 1] * len(new_grid)
        row_range = range(len(new_grid))
        col_range = range(len(new_grid[0]) - 1, -1, -1)
        add = -1
    else:
        next_free = [0] * len(new_grid)
        row_range = range(len(new_grid))
        col_range = range(len(new_grid[0]))
        add = 1

    for r in row_range:
        for c in col_range:
            if new_grid[r][c] == "O":
                new_grid[r][c] = "."
                if direction in ["north", "south"]:
                    new_grid[next_free[c]][c] = "O"
                    next_free[c] = next_free[c] + add
                else:
                    new_grid[r][next_free[r]] = "O"
                    next_free[r] = next_free[r] + add
            elif new_grid[r][c] == "#":
                if direction in ["north", "south"]:
                    next_free[c] = r + add
                else:
                    next_free[r] = c + add

    return ["".join(row) for row in new_grid]


def cycle(grid: List[str]):
    for direction in ["north", "west", "south", "east"]:
        grid = tilt(grid, direction)
    return grid


def grid_to_str(grid: List[str]):
    return "\n".join(grid)

def part2(grid: List[str], num_of_cycles):
    seen_states = dict()
    grid_str = grid_to_str(grid)
    states = []
    while grid_str not in seen_states:
        seen_states[grid_str] = len(states)
        states.append(grid_str)
        grid = cycle(grid)
        grid_str = grid_to_str(grid)

    start = seen_states[grid_str]
    cycle_length = len(states) - start
    remaining = num_of_cycles - start
    final_state_idx = start + (remaining % cycle_length)
    # print(start, cycle_length, remaining)
    grid_str = states[final_state_idx]
    return grid_str.split("\n")


def calculate_load(grid: List[str]):
    rows = len(grid)
    load = 0
    for r in range(rows):
        for c in range(len(grid[0])):
            if grid[r][c] == "O":
                load += rows - r

    return load


def solve():
    grid = []
    line = read_line()
    while line:
        grid.append(line)
        line = read_line()

    titled_grid = tilt(grid, "north")
    # print("\n".join(titled_grid))

    print(f"Part 1: {calculate_load(titled_grid)}")

    cycled_grid = part2(titled_grid, 1000000000)
    # print("\n".join(cycled_grid))
    ans2 = calculate_load(cycled_grid)
    print(f"Part 2: {ans2}")


if __name__ == '__main__':
    solve()
