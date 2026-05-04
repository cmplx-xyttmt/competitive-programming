from typing import List
import sys
# https://atcoder.jp/contests/dp/tasks/dp_b
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
    n, k = read_ints()
    h = read_ints()
    costs = [float('inf')] * n  # costs[i] -> cost to reach stone i
    costs[0] = 0
    for i in range(1, n):
        for j in range(1, min(i, k) + 1):
            costs[i] = min(costs[i], costs[i - j] + abs(h[i - j] - h[i]))
    print(costs[-1])


if __name__ == '__main__':
    solve()
