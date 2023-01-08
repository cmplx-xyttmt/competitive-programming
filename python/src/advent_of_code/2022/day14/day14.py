from typing import List
import sys

sys.stdin = open("day14.in", "r")
sys.stdout = open("day14.out", "w")
sys.setrecursionlimit(int(1e6))

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


grid_size = 1000


def create_grid(paths):
    highest_point = 0
    grid = [list('.' * grid_size) for _ in range(grid_size)]
    grid[0][grid_size // 2] = '+'
    for path in paths:
        highest_point = max(highest_point, add_path(path, grid))
    return grid, highest_point


def add_path(path, grid):
    highest_point = 0
    y, x = path[0]
    grid[x][y] = '#'
    for i in range(1, len(path)):
        y, x = path[i - 1]
        ny, nx = path[i]
        highest_point = max(highest_point, max(x, nx))
        dx, dy = nx - x, ny - y
        dx, dy = 0 if dx == 0 else dx // abs(dx), 0 if dy == 0 else dy // abs(dy)
        # sys.stderr.write(f"{dx, dy}\n")
        while not (x == nx and y == ny):
            # sys.stderr.write(f"{x, y}\n")
            grid[x][y] = '#'
            x += dx
            y += dy
        grid[x][y] = '#'
    return highest_point


def dfs(x, y, grid):
    if x + 1 >= grid_size:
        return True
    elif grid[x + 1][y] == '.':
        return dfs(x + 1, y, grid)
    elif y - 1 < 0:
        return True
    elif grid[x + 1][y - 1] == '.':
        return dfs(x + 1, y - 1, grid)
    elif y + 1 >= grid_size:
        return True
    elif grid[x + 1][y + 1] == '.':
        return dfs(x + 1, y + 1, grid)

    grid[x][y] = 'o'
    return False


def solve():
    # sys.stderr.write(f"{grid}\n")
    paths = []
    line = read_line()
    while line:
        path = line.split('->')
        path = [coords.strip() for coords in path]
        path = [tuple(map(int, coords.split(','))) for coords in path]
        paths.append(path)

        line = read_line()

    rest = 0
    grid, _ = create_grid(paths)
    while grid[0][grid_size // 2] == '+' and not dfs(0, grid_size // 2, grid):
        rest += 1
    # for i in range(10):
    #     sys.stderr.write(f"{grid[i][493:504]}\n")
    print(f"Part 1: {rest}")

    rest = 0
    grid, highest_point = create_grid(paths)
    grid[highest_point + 2] = list('#' * grid_size)
    while grid[0][grid_size // 2] == '+' and not dfs(0, grid_size // 2, grid):
        rest += 1
    print(f"Part 2: {rest}")


if __name__ == '__main__':
    solve()
