import math
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
    ms = [1] * (n + 1)
    is_prime = [True] * (n + 1)
    for p in range(2, n + 1):
        if not is_prime[p]:
            continue
        ms[p] = p
        for num in range(2 * p, n + 1, p):
            is_prime[num] = False
            times = 0
            b = num
            while b % p == 0:
                b //= p
                times += 1
            ms[num] *= (p ** (math.ceil(times/2)))

    for i in range(1, n + 1):
        m = math.floor(math.sqrt(i * n))
        ans += 1 + 2 * ((m - i) // ms[i])
    print_(f"{ans}\n")


if __name__ == '__main__':
    solve()
