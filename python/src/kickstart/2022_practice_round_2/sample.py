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

    for test in range(1, t + 1):
        n, m = read_ints()
        c = read_ints()
        print_(f"Case #{test}: {sum(c) % m}\n")


if __name__ == '__main__':
    solve()
