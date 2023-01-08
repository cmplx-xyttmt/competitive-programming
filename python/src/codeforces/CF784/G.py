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


def next_free_cell(col, grid, start):
    free_cell = start
    while free_cell >= 0 and grid[free_cell][col] != '.':
        free_cell -= 1
    return free_cell


def handle_column(col, grid):
    free_cell = next_free_cell(col, grid, len(grid) - 1)
    for i in range(free_cell, -1, -1):
        if i > free_cell:
            continue
        if grid[i][col] == '*':
            grid[free_cell][col] = '*'
            grid[i][col] = '.'
            free_cell = next_free_cell(col, grid, free_cell - 1)
        elif grid[i][col] == 'o':
            free_cell = next_free_cell(col, grid, min(free_cell, i - 1))


def solve():
    t = read_int()
    for _ in range(t):
        n, m = read_ints()
        grid = []
        for _ in range(n):
            grid.append(list(read_line()))

        for col in range(m):
            handle_column(col, grid)
        ans = '\n'.join(map(lambda x: "".join(x), grid))
        print_(f"{ans}\n")


if __name__ == '__main__':
    solve()
