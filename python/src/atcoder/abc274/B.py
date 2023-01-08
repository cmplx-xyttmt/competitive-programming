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
    h, w = read_ints()
    grid = []
    for _ in range(h):
        grid.append(read_line())

    x = [0] * w
    for i in range(h):
        for j in range(w):
            if grid[i][j] == '#':
                x[j] += 1

    print_(f"{' '.join(map(str, x))}\n")


if __name__ == '__main__':
    solve()
