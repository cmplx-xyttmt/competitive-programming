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
        a = [(x, i) for i, x in enumerate(read_ints())]
        a.sort()
        print_(f"{a[0][1] + 1} {a[n - 1][1] + 1}\n")


if __name__ == '__main__':
    solve()
