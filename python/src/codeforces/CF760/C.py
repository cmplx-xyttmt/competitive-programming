from typing import List
import sys
from math import gcd

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
        a = read_ints()
        odd_gcd = a[1]
        even_gcd = a[0]
        for i in range(2, n):
            if i % 2 == 0:
                even_gcd = gcd(even_gcd, a[i])
            else:
                odd_gcd = gcd(odd_gcd, a[i])

        even_valid = True
        odd_valid = True

        for i in range(n):
            if i % 2 == 0 and a[i] % odd_gcd == 0:
                odd_valid = False
            if i % 2 == 1 and a[i] % even_gcd == 0:
                even_valid = False

        if even_valid or odd_valid:
            print_(f"{odd_gcd if odd_valid else even_gcd}\n")
        else:
            print_("0\n")


if __name__ == '__main__':
    solve()
