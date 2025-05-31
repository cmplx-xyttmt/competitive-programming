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
    a, b = read_ints()
    floor, rem = divmod(a, b)
    if rem * 2 > b:
        print_(f"{floor + 1}\n")
    else:
        print_(f"{floor}\n")


if __name__ == '__main__':
    solve()
