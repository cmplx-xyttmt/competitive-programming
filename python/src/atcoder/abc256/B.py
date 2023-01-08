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
    pieces = [0] * 4
    p = 0
    for ai in a:
        pieces[0] += 1
        for rem in range(4 - ai, 4):
            p += pieces[rem]
            pieces[rem] = 0
        for stay in range(4 - ai - 1, -1, -1):
            pieces[stay + ai] += pieces[stay]
            pieces[stay] = 0
        # print(pieces)
    print_(f"{p}\n")


if __name__ == '__main__':
    solve()
