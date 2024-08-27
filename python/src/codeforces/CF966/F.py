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


def get_minimum_operations(k, a, b):
    ops = 0
    for _ in range(k):
        if a < b:
            ops += a
            b -= 1
        else:
            ops += b
            a -= 1
    return ops


def solve():
    INF = int(1e18)
    t = read_int()
    for _ in range(t):
        n, K = read_ints()
        rectangles = []
        for _ in range(n):
            a, b = read_ints()
            if a > b:
                a, b = b, a
            rectangles.append((a, b))
        dp = [[INF for _ in range(K + 1)] for _ in range(n)]
        ans = INF
        for i in range(n):
            for k in range(K + 1):
                a, b = rectangles[i]
                if i == 0:
                    dp[i][k] = INF if k > a + b else get_minimum_operations(k, a, b)
                else:
                    if k <= a + b:
                        take = get_minimum_operations(k, a, b)
                    else:
                        take = INF
                    if dp[i - 1][k - min(k, a + b)] == INF or take == INF:
                        take = INF
                    else:
                        take += dp[i - 1][k - min(k, a + b)]
                    dp[i][k] = min(take, dp[i - 1][k])
                if k == K:
                    ans = min(dp[i][k], ans)
        ans = -1 if ans == INF else ans
        print_(f"{ans}\n")


if __name__ == '__main__':
    solve()
