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
        a = read_ints()
        even = a[0] % 2
        odd = a[1] % 2
        can = True
        for i, num in enumerate(a):
            if (i % 2 == 0 and num % 2 != even) or (i % 2 == 1 and num % 2 != odd):
                can = False
                break

        print_(f"{'YES' if can else 'NO'}\n")


if __name__ == '__main__':
    solve()
