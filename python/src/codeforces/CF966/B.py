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
        seen = set()
        followed = True
        for i, seat in enumerate(a):
            if i > 0:
                left = seat - 1
                right = seat + 1
                followed = followed and (left in seen or right in seen)
            seen.add(seat)
        print_(f"{'YES' if followed else 'NO'}\n")


if __name__ == '__main__':
    solve()
