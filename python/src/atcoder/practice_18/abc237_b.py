from typing import List
import sys
import numpy as np

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
    n, m = read_ints()
    matrix = []
    for _ in range(n):
        matrix.append(read_ints())
    matrix = np.array(matrix)
    np.savetxt(sys.stdout, matrix.T, fmt='%d')


if __name__ == '__main__':
    solve()
