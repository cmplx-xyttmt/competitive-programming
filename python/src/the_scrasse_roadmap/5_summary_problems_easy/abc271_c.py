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
    a = read_ints()
    unique = set(a)
    to_sell = n
    next_volume = 1
    while to_sell > 0:
        if next_volume not in unique:
            if to_sell < 2:
                break
            to_sell -= 2
        else:
            to_sell -= 1
        next_volume += 1
    print_(f"{next_volume - 1}\n")


if __name__ == '__main__':
    solve()
