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
    n = read_int()

    dp = [float('inf') for _ in range(n + 1)]
    dp[0] = 0
    for i in range(1, n + 1):
        six = 1
        while six <= i:
            dp[i] = min(dp[i], 1 + dp[i - six])
            six *= 6
        nine = 9
        while nine <= i:
            dp[i] = min(dp[i], 1 + dp[i - nine])
            nine *= 9
    print_(f"{dp[n]}\n")


if __name__ == '__main__':
    solve()
