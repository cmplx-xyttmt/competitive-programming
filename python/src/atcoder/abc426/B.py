from collections import defaultdict
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
    S = read_line()
    counts = defaultdict(int)
    for c in S:
        counts[c] += 1
    for c, count in counts.items():
        if count == 1:
            print(c)
            break


if __name__ == '__main__':
    solve()
