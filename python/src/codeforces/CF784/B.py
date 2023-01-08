from collections import Counter
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
        n = read_int()
        a = Counter(read_ints())
        ans = -1
        for key, occ in a.items():
            if occ >= 3:
                ans = key
                break

        print_(f"{ans}\n")


if __name__ == '__main__':
    solve()
