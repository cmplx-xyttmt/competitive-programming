from typing import List
import sys
from collections import deque

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
    t = read_int()
    for test in range(1, t + 1):
        n = read_int()
        d = read_ints()
        max_left = [0 for _ in range(n)]
        max_left[0] = d[0]
        max_right = [0 for _ in range(n)]
        max_right[n - 1] = d[n - 1]
        for i in range(1, n):
            max_left[i] = max(d[i], max_left[i - 1])
        for i in range(n - 2, -1, -1):
            max_right[i] = max(d[i], max_right[i + 1])
        paid = 0
        for i in range(n):
            if d[i] >= max_left[i] or d[i] >= max_right[i]:
                paid += 1
        # print(left_index, right_index)
        print_(f"Case #{test}: {paid}\n")


if __name__ == '__main__':
    solve()
