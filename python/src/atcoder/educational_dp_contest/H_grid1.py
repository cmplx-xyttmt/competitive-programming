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
    h, w = read_ints()
    grid = [read_line() for _ in range(h)]
    dp = [[0] * (w + 1) for _ in range(h + 1)]
    dp[0][1] = 1
    MOD = int(1e9) + 7
    for i in range(1, h + 1):
        for j in range(1, w + 1):
            if grid[i - 1][j - 1] == '.':
                dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % MOD

    print(dp[h][w])


if __name__ == '__main__':
    solve()
