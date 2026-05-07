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
    # dp[i][j] = prob of having j heads after the ith coin toss
    # dp[i][j] = dp[i - 1][j] * (1 - p[i]) + dp[i - 1][j - 1] * p[i]
    p = [float(num) for num in read_strings()]
    prev = [0.0] * (n + 1)
    prev[0] = 1.0
    for i in range(1, n + 1):
        curr = list(prev)
        curr[0] = prev[0] * (1 - p[i - 1])
        for j in range(1, i + 1):
            curr[j] = prev[j] * (1 - p[i - 1]) + prev[j - 1] * p[i - 1]
        prev = curr
        # print(i, prev)

    more = n // 2
    print(sum(prev[more + 1:]))


if __name__ == '__main__':
    solve()
