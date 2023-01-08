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
    fives = 0
    pow5 = 5
    while pow5 <= n:
        fives += n // pow5
        pow5 *= 5

    print_(f"{fives}\n")


if __name__ == '__main__':
    solve()
