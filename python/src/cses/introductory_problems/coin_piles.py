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
        a, b = read_ints()
        if (a + b) % 3 != 0 or max(a, b) > 2 * min(a, b):
            print_(f"NO\n")
        else:
            print_(f"YES\n")


if __name__ == '__main__':
    solve()
