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


def mod_exp(num, p, mod):
    ans = 1
    while p > 0:
        if p % 2 == 1:
            ans = (ans * num) % mod
        num = (num * num) % mod
        p //= 2
    return ans


def solve():
    n = read_int()
    mod = int(1e9) + 7
    print_(f"{mod_exp(2, n, mod)}\n")


if __name__ == '__main__':
    solve()
