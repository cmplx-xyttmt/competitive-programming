from typing import List
import sys

sys.stdin = open("day8.in", "r")
sys.stdout = open("day8.out", "w")

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


def mark_cell(row, col, grid, visible, max_height):
    if grid[row][col] > max_height:
        visible[row][col] = True
        max_height = grid[row][col]
    return max_height


def lr(grid, visible, rows, cols):
    for row in range(rows):
        max_height = -1
        for col in range(cols):
            max_height = mark_cell(row, col, grid, visible, max_height)
        max_height = -1
        for col in range(cols - 1, -1, -1):
            max_height = mark_cell(row, col, grid, visible, max_height)


def ud(grid, visible, rows, cols):
    for col in range(cols):
        max_height = -1
        for row in range(rows):
            max_height = mark_cell(row, col, grid, visible, max_height)
        max_height = -1
        for row in range(rows - 1, -1, -1):
            max_height = mark_cell(row, col, grid, visible, max_height)


def move(row, col, grid, dx, dy):
    rows, cols = len(grid), len(grid[0])
    visible = 0
    diff_x, diff_y = dx, dy
    while 0 <= row + diff_x < rows and 0 <= col + diff_y < cols:
        visible += 1
        if grid[row + diff_x][col + diff_y] >= grid[row][col]:
            break
        diff_x += dx
        diff_y += dy

    return visible


def scenic_score(row, col, grid):
    up = move(row, col, grid, -1, 0)
    down = move(row, col, grid, 1, 0)
    left = move(row, col, grid, 0, -1)
    right = move(row, col, grid, 0, 1)
    return up * down * left * right


def solve():
    grid = []
    line = read_line()
    while line:
        heights = list(map(int, list(line)))
        grid.append(heights)
        line = read_line()

    rows, cols = len(grid), len(grid[0])
    visible = [[False for _ in range(cols)] for _ in range(rows)]

    lr(grid, visible, rows, cols)
    ud(grid, visible, rows, cols)

    print(f"Part 1: {sum([sum(row) for row in visible])}")
    scenic_scores = [[scenic_score(row, col, grid) for col in range(cols)] for row in range(rows)]
    print(f"Part 2: {max([max(row) for row in scenic_scores])}")


if __name__ == '__main__':
    solve()
