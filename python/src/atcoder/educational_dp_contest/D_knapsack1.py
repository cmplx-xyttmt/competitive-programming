from typing import List
import sys

# https://atcoder.jp/contests/dp/tasks/dp_d
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
    n, W = read_ints()
    items = [read_ints() for _ in range(n)]
    prev = [0] * (W + 1)
    for w, v in items:
        curr = list(prev)
        for j in range(w, W + 1):
            curr[j] = max(curr[j], v + prev[j - w])
        prev = curr
    print(prev[W])


if __name__ == '__main__':
    solve()
