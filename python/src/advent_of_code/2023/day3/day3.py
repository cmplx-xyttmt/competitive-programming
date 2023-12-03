from collections import defaultdict
from typing import List, Optional, Set, Dict, Tuple
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


def grid_safe(grid: List[str], r: int, c: int) -> Optional[str]:
    rows = len(grid)
    cols = len(grid[0])
    if 0 <= r < rows and 0 <= c < cols:
        return grid[r][c]
    return "."



def has_adjacent_symbol(grid: List[str], r: int, c: int):
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            neighbor = grid_safe(grid, r + dr, c + dc)
            if not (neighbor == "." or neighbor.isdigit()):
                return True
    return False


def adjacent_star(grid: List[str], r: int, c: int) -> Set:
    adj_stars = set()
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            neighbor = grid_safe(grid, r + dr, c + dc)
            if neighbor == "*":
                adj_stars.add((r + dr, c + dc))
    return adj_stars


def solve():
    line = read_line()
    grid: List[str] = []
    while line:
        grid.append(line)
        line = read_line()
    ans1 = 0
    stars: Dict[Tuple, List] = defaultdict(list)
    for r, row in enumerate(grid):
        current_number, is_part = 0, False
        num_stars = set()
        for c, char in enumerate(row):
            if char.isdigit():
                current_number, is_part = current_number * 10 + int(char), is_part or has_adjacent_symbol(grid, r, c)
                num_stars = num_stars.union(adjacent_star(grid, r, c))
            else:
                ans1 += (current_number if is_part else 0)
                if is_part:
                    for (sr, sc) in num_stars:
                        stars[(sr, sc)].append(current_number)

                current_number, is_part = 0, False
                num_stars = set()
        ans1 += (current_number if is_part else 0)
        if is_part:
            for (sr, sc) in num_stars:
                stars[(sr, sc)].append(current_number)


    print(f"Part 1: {ans1}")

    ans2 = 0
    for part_nums in stars.values():
        if len(part_nums) == 2:
            ans2 += (part_nums[0] * part_nums[1])

    print(f"Part 2: {ans2}")


if __name__ == '__main__':
    solve()
