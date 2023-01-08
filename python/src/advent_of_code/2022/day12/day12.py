from typing import List
import sys
from collections import deque

sys.stdin = open("day12.in", "r")
sys.stdout = open("day12.out", "w")

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


def check_elevation(fro, to):
    if fro == 'S':
        fro = 'a'
    if to == 'E':
        to = 'z'
    return ord(fro) - ord(to) >= -1


def bfs(h, w, start, gx, gy, grid):
    # sys.stderr.write(f"{(h, w)} {(sx, sy)} {(gx, gy)}\n")
    q = deque()
    for sx, sy in start:
        q.append((sx, sy, 0))
        seen = {(sx, sy)}
    d = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    while q:
        x, y, dist = q.popleft()
        if x == gx and y == gy:
            return dist
        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if 0 <= nx < h and 0 <= ny < w and (nx, ny) not in seen and check_elevation(grid[x][y], grid[nx][ny]):
                q.append((nx, ny, dist + 1))
                seen.add((nx, ny))
        # sys.stderr.write(f"{q}\n")
    return -1


def solve():
    grid = []
    line = read_line()
    sx, sy = -1, -1
    gx, gy = -1, -1
    row = 0
    while line:
        grid.append(line)
        for col in range(len(line)):
            if grid[row][col] == 'S':
                sx, sy = row, col
            elif grid[row][col] == 'E':
                gx, gy = row, col
        row += 1
        line = read_line()

    ans = bfs(len(grid), len(grid[0]), {(sx, sy)}, gx, gy, grid)
    print(f"Part 1: {ans}")
    all_as = [(x, y) for y in range(len(grid[0])) for x in range(len(grid)) if grid[x][y] in {'a', 'S'}]
    ans = bfs(len(grid), len(grid[0]), all_as, gx, gy, grid)
    print(f"Part 2: {ans}")


if __name__ == '__main__':
    solve()
