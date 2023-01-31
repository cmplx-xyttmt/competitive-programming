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
    # a <= cube_root(n)
    # a <= b <= root(n / a)
    # b <= c <= n / ab
    a = 1
    ans = 0
    while a * a * a <= n:
        b = a
        while b * b <= n // a:
            ans += (n // (a * b)) - b + 1
            b += 1
        a += 1

    print_(f"{ans}\n")


if __name__ == '__main__':
    solve()
