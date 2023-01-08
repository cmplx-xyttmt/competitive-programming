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
    t = read_int()

    for _ in range(t):
        read_line()
        n, m = read_ints()
        a = read_ints()
        left = []  # left[i] -> no of items to left <= a[i]
        right = []  # right[i] -> no of items to right >= a[i]


if __name__ == '__main__':
    solve()
