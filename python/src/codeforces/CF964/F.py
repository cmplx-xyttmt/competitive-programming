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
    # TODO: Solve https://codeforces.com/contest/1999/problem/F
    # Initial thoughts:
    #   -> count subsequences of length k that have > (k/2 + 1) 1s.
    pass


if __name__ == '__main__':
    solve()
