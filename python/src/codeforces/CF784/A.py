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
    bounds = [1900, 1600, 1400]
    t = read_int()

    for _ in range(t):
        rating = read_int()
        division = 1
        for bound in bounds:
            if rating >= bound:
                break
            division += 1

        print_(f"Division {division}\n")


if __name__ == '__main__':
    solve()
