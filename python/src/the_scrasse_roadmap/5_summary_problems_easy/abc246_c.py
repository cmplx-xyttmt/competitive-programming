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
    n, k, x = read_ints()
    a = read_ints()
    for i in range(n):
        coups = min(a[i] // x, k)
        a[i] -= coups * x
        k -= coups
    a.sort(reverse=True)
    for i in range(min(n, k)):
        a[i] = 0
    print_(f"{sum(a)}\n")


if __name__ == '__main__':
    solve()
