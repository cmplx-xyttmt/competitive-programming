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
        a, b, c, x, y = read_ints()
        x = max(0, x - a)
        y = max(0, y - b)
        c -= x
        c -= y
        print_(f"{'YES' if c >= 0 else 'NO'}\n")


if __name__ == '__main__':
    solve()
