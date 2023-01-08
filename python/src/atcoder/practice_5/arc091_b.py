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
    n, k = read_ints()
    ans = 0
    for b in range(1, n + 1):
        p, r = divmod(n, b)
        ans += (p * max(0, b - k))
        ans += max(0, r - k + 1)
        if k == 0:
            ans -= 1
    print_(f"{ans}")


if __name__ == '__main__':
    solve()
