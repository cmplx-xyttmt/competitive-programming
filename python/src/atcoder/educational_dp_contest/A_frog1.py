from typing import List
import sys
# https://atcoder.jp/contests/dp/tasks/dp_a
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
    h = read_ints()
    costs = [float('inf')] * n  # minimum cost to arrive at stone i.
    costs[0] = 0
    for i in range(1, n):
        costs[i] = costs[i - 1] + abs(h[i] - h[i - 1])
        if i >= 2:
            costs[i] = min(costs[i], costs[i - 2] + abs(h[i] - h[i - 2]))
    print(costs[-1])


if __name__ == '__main__':
    solve()
