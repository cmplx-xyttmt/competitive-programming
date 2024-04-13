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
    s = read_line()
    c = Counter(s)
    c = Counter(c.values())
    print_(f"{'Yes' if all(map(lambda x: x == 2, c.values())) else 'No'}\n")


if __name__ == '__main__':
    solve()
