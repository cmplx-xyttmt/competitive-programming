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

        zero, one, two = False, False, False

        for num in a:
            zero, one, two = zero or num == 0, one or num == 1, two or num == 2

        if (zero and one) or (two and one):
            print_("NO\n")
        else:
            print_("YES\n")


if __name__ == '__main__':
    solve()
