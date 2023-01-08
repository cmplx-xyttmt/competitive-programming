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
        rating = read_ints()
        ans = 0
        for i in range(n):
            ans = max(ans, rating[i] + rating[(i + 1) % n] + rating[(i + 2) % n])
        print_(f"{ans}\n")


if __name__ == '__main__':
    solve()
