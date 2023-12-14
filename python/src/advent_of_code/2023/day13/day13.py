from copy import deepcopy
from typing import List, Tuple
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


def ranges_valid(first: Tuple[int, int], second: Tuple[int, int], length: int, debug=False):
    if second[1] > length:
        return False
    # make sure at least one of the ranges reaches the end of the grid
    if not (first[0] == 0 or second[1] == length):
        return False

    # make sure the lengths of the ranges are equal
    if first[1] - first[0] != second[1] - second[0]:
        return False

    # make sure the ranges don't intersect
    if first[1] > second[0]:
        return False

    return True


def vertical_reflection(grid: List[str], first: Tuple[int, int], second: Tuple[int, int], to_border=True):
    # first and second are tuples containing the range for comparison (exclusive at the end).
    if not ranges_valid(first, second, len(grid[0])):
        return False

    for row in range(len(grid)):
        for diff in range(0, first[1] - first[0]):
            if grid[row][first[0] + diff] != grid[row][second[1] - diff - 1]:
                return False
    return True


def horizontal_reflection(grid: List[str], first: Tuple[int, int], second: Tuple[int, int]):
    if not ranges_valid(first, second, len(grid)):
        return False

    for diff in range(0, first[1] - first[0]):
        if grid[first[0] + diff] != grid[second[1] - diff - 1]:
            return False

    return True


def find_reflection(grid: List[str], prev_line=None):
    for vertical_start in range(len(grid[0])):
        for vertical_end in range(vertical_start + 1, len(grid[0])):
            if vertical_reflection(grid, (vertical_start, vertical_end), (vertical_end, len(grid[0]))):
                if ("vert", vertical_end) != prev_line:
                    return "vert", vertical_end
            if vertical_start == 0 and vertical_reflection(grid, (vertical_start, vertical_end), (vertical_end, 2 * vertical_end - vertical_start)):
                if ("vert", vertical_end) != prev_line:
                    return "vert", vertical_end

    for horizontal_start in range(len(grid)):
        for horizontal_end in range(horizontal_start + 1, len(grid)):
            if horizontal_reflection(grid, (horizontal_start, horizontal_end), (horizontal_end, len(grid))):
                if ("hor", horizontal_end) != prev_line:
                    return "hor", horizontal_end
            if horizontal_start == 0 and horizontal_reflection(grid, (horizontal_start, horizontal_end), (horizontal_end, 2 * horizontal_end - horizontal_start)):
                if ("hor", horizontal_end) != prev_line:
                    return "hor", horizontal_end

    return "none", 0


def change_grid(grid: List[str], i: int, j: int):
    new_grid = deepcopy(grid)
    row = list(new_grid[i])
    row[j] = "#" if row[j] == "." else "#"
    new_grid[i] = "".join(row)
    return new_grid


def find_smudge_reflection(grid: List[str]):
    prev_line = find_reflection(grid)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            new_grid = change_grid(grid, i, j)
            new_line = find_reflection(new_grid, prev_line)
            if new_line[1] != 0:
                return new_line
    return "none", 0


def calc_score(grids: List[List[str]], reflection_function):
    hor_sum, vert_sum = 0, 0
    for grid in grids:
        type_, refl = reflection_function(grid)
        if type_ == "hor":
            hor_sum += refl
        else:
            vert_sum += refl

    return vert_sum + 100 * hor_sum

def solve():
    grids = []
    line = read_line()
    while line:
        grid = []
        while line:
            grid.append(line)
            line = read_line()
        line = read_line()
        grids.append(grid)

    ans1 = calc_score(grids, find_reflection)
    print(f"Part 1: {ans1}")

    ans2 = calc_score(grids, find_smudge_reflection)
    print(f"Part 2: {ans2}")


if __name__ == '__main__':
    solve()
