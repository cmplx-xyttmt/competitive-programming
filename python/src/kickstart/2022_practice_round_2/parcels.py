from collections import deque
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


def get_max_distance(r, c, grid):
    q = deque()
    seen = [[False for _ in range(c)] for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if grid[i][j] == '1':
                q.append((i, j, 0))
                seen[i][j] = True

    neighbors = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    while q:
        i, j, dist = q.popleft()
        for di, dj in neighbors:
            ni, nj = i + di, j + dj
            if 0 <= ni < r and 0 <= nj < c and not seen[ni][nj]:
                seen[ni][nj] = True
                q.append((ni, nj, dist + 1))
        if not q:
            return i, j, dist
    return 0, 0, 0


def solve():
    t = read_int()

    for test in range(1, t + 1):
        r, c = read_ints()
        grid = []
        for _ in range(r):
            grid.append(list(read_line()))
        _, _, dist = get_max_distance(r, c, grid)
        ans = dist
        for i in range(r):
            for j in range(c):
                if grid[i][j] == '0':
                    grid[i][j] = '1'
                    _, _, dist = get_max_distance(r, c, grid)
                    ans = min(ans, dist)
                    grid[i][j] = '0'
        print_(f"Case #{test}: {ans}\n")


if __name__ == '__main__':
    solve()
