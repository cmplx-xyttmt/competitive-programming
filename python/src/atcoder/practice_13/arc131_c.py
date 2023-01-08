from functools import reduce
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
    n = read_int()
    a = read_ints()

    if n % 2 == 1:
        print("Win")
    else:
        xor = reduce(lambda x, y: x ^ y, a)
        print("Win" if xor in set(a) else "Lose")


if __name__ == '__main__':
    solve()
