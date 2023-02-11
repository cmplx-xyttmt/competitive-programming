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
    parents = read_ints()
    gens = [0, 0]
    for p in parents:
        gens.append(1 + gens[p])
    print_(f"{gens[n]}\n")


if __name__ == '__main__':
    solve()
