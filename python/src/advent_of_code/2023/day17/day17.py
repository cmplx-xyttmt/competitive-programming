import functools
from typing import List
import sys

input_ = sys.stdin.readline
print_ = sys.stdout.write
flush = sys.stdout.flush

sys.setrecursionlimit(int(1e6))


def read_line() -> str:
    return input_().strip()


def read_int() -> int:
    return int(read_line())


def read_strings() -> List[str]:
    return list(read_line().split())


def read_ints():
    return list(map(int, read_line().split()))


def least_heat_loss(grid: List[List[int]]):

    next_directions = {
        "right": ["right", "up", "down"],
        "left": ["left", "up", "down"],
        "down": ["down", "left", "right"],
        "up": ["up", "left", "right"]
    }
    num_rows, num_cols = len(grid), len(grid[0])
    states = set()
    @functools.lru_cache(maxsize=None)
    def least(i: int, j: int, direction: str, consec: int):
        states.add((i, j, direction, consec))
        print(i, j, direction, consec, f"states seen: {len(states)}")
        if i == num_rows - 1 and j == num_cols - 1:
            return grid[i][j]
        new_coordinates = {
            "right": (i, j + 1),
            "left": (i, j - 1),
            "up": (i - 1, j),
            "down": (i + 1, j)
        }
        best = float('inf')
        for new_direction in next_directions[direction]:
            ni, nj = new_coordinates[new_direction]
            if (0 <= ni < num_rows and 0 <= nj < num_cols) and ((direction == new_direction and consec < 3) or (direction != new_direction)):
                state = (ni, nj, new_direction, consec + 1 if direction == new_direction else 1)
                if state not in states:
                    best = min(best, grid[i][j] + least(ni, nj, new_direction, consec + 1 if direction == new_direction else 1))

        return best
    return min(least(0, 1, "right", 1), least(1, 0, "down", 1))


def solve():
    grid = []
    row = read_line()
    while row:
        nums = list(map(int, list(row)))
        grid.append(nums)
        row = read_line()

    print(f"Part 1: {least_heat_loss(grid)}")


if __name__ == '__main__':
    solve()
