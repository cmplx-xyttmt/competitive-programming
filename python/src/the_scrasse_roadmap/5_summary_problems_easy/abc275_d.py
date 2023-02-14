from collections import deque
from typing import List
from functools import lru_cache
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


@lru_cache(maxsize=None)
def recurse(n):
    if n == 0:
        return 1
    return recurse(n // 2) + recurse(n // 3)


def solve():
    n = read_int()
    print(recurse(n))


if __name__ == '__main__':
    solve()
