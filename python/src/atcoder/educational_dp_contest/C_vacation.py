from typing import List
import sys

# https://atcoder.jp/contests/dp/tasks/dp_c
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
    n = read_int()
    dp = [[0] * 3 for _ in range(n)]  # dp[i][j] -> maximum happiness on day i if he does activity j
    for i in range(n):
        happiness = read_ints()
        for j in range(3):
            dp[i][j] = happiness[j]
            if i > 0:
                dp[i][j] += max(dp[i - 1][(j + 1) % 3],
                                dp[i - 1][(j + 2) % 3])
    print(max(dp[-1]))


if __name__ == '__main__':
    solve()
