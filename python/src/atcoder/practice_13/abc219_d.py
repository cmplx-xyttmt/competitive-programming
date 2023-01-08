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
    x, y = read_ints()
    ab = []
    all_x, all_y = 0, 0
    for _ in range(n):
        a, b = read_ints()
        ab.append((a, b))
        all_x, all_y = all_x + a, all_y + b

    if all_x < x or all_y < y:
        print_(f"-1\n")
        return

    inf = int(1e9)
    dp = [[[inf for _ in range(y + 1)] for _ in range(x + 1)] for _ in range(n)]
    for i in range(n):
        dp[i][0][0] = 0

    for i in range(n):
        for a in range(x + 1):
            for b in range(y + 1):
                u, v = ab[i]
                prev_a = max(0, a - u)
                prev_b = max(0, b - v)
                if prev_a == 0 and prev_b == 0:
                    prev = 0
                else:
                    prev = inf if i == 0 else dp[i - 1][prev_a][prev_b]
                # print(a, b, i)
                dp[i][a][b] = min(1 + prev, inf if i == 0 else dp[i - 1][a][b])

    print_(f"{dp[n - 1][x][y]}\n")


if __name__ == '__main__':
    solve()
