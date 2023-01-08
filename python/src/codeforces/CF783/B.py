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
        n, m = read_ints()
        a = read_ints()
        a.sort()
        required_seats = 0
        for i in range(n):
            required_seats += (1 + max(a[i], a[(i + 1) % n]))

        print_(f"{'YES' if required_seats <= m else 'NO'}\n")


if __name__ == '__main__':
    solve()
