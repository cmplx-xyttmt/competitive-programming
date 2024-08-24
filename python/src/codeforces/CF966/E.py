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


def solve():
    t = read_int()
    for _ in range(t):
        n, m, k = read_ints()
        w = read_int()
        a = read_ints()
        a.sort(reverse=True)
        grid = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if i + k <= n and j + k <= m:
                    grid[i][j] += 1
                    if i + k < n and j + k < m:
                        grid[i + k][j] -= 1
                        grid[i][j + k] -= 1
                        grid[i + k][j + k] += 1
                    else:
                        if i + k < n:
                            grid[i + k][j] -= 1
                        if j + k < m:
                            grid[i][j + k] -= 1

        values = []
        for i in range(n):
            for j in range(m):
                if i - 1 >= 0 and j - 1 >= 0:
                    grid[i][j] += grid[i - 1][j] + grid[i][j - 1] - grid[i - 1][j - 1]
                else:
                    if i - 1 >= 0:
                        grid[i][j] += grid[i - 1][j]
                    if j - 1 >= 0:
                        grid[i][j] += grid[i][j - 1]
                values.append(grid[i][j])

        values.sort(reverse=True)
        ans = 0
        for i, val in enumerate(a):
            ans += val * values[i]
        print_(f"{ans}\n")


if __name__ == '__main__':
    solve()
