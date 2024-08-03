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
        n, k = read_ints()
        grid = [read_line() for _ in range(n)]
        reduced_grid = []
        for i in range(0, n, k):
            # print("row", grid[i])
            row = []
            for j in range(0, n, k):
                row.append(grid[i][j])
            reduced_grid.append(row)

        ans = '\n'.join(map(lambda list: ''.join(list), reduced_grid))
        print_(f"{ans}\n")


if __name__ == '__main__':
    solve()
