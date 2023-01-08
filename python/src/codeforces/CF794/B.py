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
        p = read_ints()
        skip = False
        ans = 0
        for i in range(1, n):
            if skip:
                skip = False
                continue
            if p[i] < p[i - 1]:
                skip = True
                ans += 1
        print_(f"{ans}\n")


if __name__ == '__main__':
    solve()
