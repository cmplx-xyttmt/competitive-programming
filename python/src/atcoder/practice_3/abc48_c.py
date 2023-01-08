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
    n, x = read_ints()
    a = read_ints()

    ops = 0
    for i in range(1, n):
        rem = max(0, a[i] + a[i - 1] - x)
        ops += rem
        a[i] -= min(a[i], rem)

    print_(f"{ops}\n")


if __name__ == '__main__':
    solve()
