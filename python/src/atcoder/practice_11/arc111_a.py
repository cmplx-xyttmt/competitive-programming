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


def mod_exp(x, e, mod):
    if e == 0:
        return 1
    ans = 1
    while e > 0:
        if e % 2 == 1:
            ans = (ans * x) % mod
        x = (x * x) % mod
        e //= 2
    return ans


def solve():
    n, m = read_ints()
    r = mod_exp(10, n, m)
    a = mod_exp(10, n, m ** 2)
    print((a - r) // m)


if __name__ == '__main__':
    solve()
