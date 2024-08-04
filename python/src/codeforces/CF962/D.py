from typing import List
import sys

input_ = sys.stdin.readline
print_ = sys.stdout.write
flush = sys.stdout.flush

# a + b <= x - c
# ab + c(a + b) <= n
# ab <= n - c(a + b) >= n - c(x - c)


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
        n, x = read_ints()
        ans = 0
        for a in range(1, min(n, x) + 1):
            for b in range(1, n // a):
                if (a * b + a + b) > n or (a + b) > x:
                    break
                ans += min(x - (a + b), (n - a * b) // (a + b))
        print_(f"{ans}\n")


if __name__ == '__main__':
    solve()
