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
    moves = []

    def hanoi(n, fro, inter, to):
        if n == 1:
            moves.append(f"{fro} {to}")
        else:
            hanoi(n - 1, fro, to, inter)
            moves.append(f"{fro} {to}")
            hanoi(n - 1, inter, fro, to)
    n_ = read_int()
    hanoi(n_, 1, 2, 3)
    ans = '\n'.join(moves)
    print_(f"{len(moves)}\n")
    print_(f"{ans}\n")


if __name__ == '__main__':
    solve()
