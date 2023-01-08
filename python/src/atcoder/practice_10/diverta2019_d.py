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
    ans = 0
    for q in range(1, int(n ** 0.5) + 1):
        if n % q == 0:
            p = n // q
            if q < p - 1:
                ans += p - 1
    print_(f"{ans}\n")


if __name__ == '__main__':
    solve()
