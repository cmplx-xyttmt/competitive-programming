from typing import List
import sys

input_ = sys.stdin.readline
print_ = sys.stdout.write
flush = sys.stdout.flush


# https://atcoder.jp/contests/dp/tasks/dp_e

def read_line() -> str:
    return input_().strip()


def read_int() -> int:
    return int(read_line())


def read_strings() -> List[str]:
    return list(read_line().split())


def read_ints():
    return list(map(int, read_line().split()))


def solve():
    # dp[i][v] -> minimum weight that gives value v
    n, W = read_ints()
    items = [read_ints() for _ in range(n)]
    max_v = sum(v for _, v in items)
    prev = [float('inf')] * (max_v + 1)
    prev[0] = 0
    for w, v in items:
        curr = list(prev)
        for j in range(v, len(prev)):
            curr[j] = min(w + prev[j - v], prev[j])
        prev = curr

    print(next(j for j in range(max_v, -1, -1) if prev[j] <= W))


if __name__ == '__main__':
    solve()
