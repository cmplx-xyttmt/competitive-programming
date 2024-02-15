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
    k, a, b = read_ints()
    if b - a <= 1:
        print_(f"{1 + k}\n")
    else:
        k = k - a + 1
        ans = a + ((b - a) * (k // 2) if k % 2 == 0 else (b - a) * ((k - 1) // 2) + 1)
        if ans < 1 + k:
            ans = 1 + k
        print_(f"{ans}\n")


if __name__ == '__main__':
    solve()
