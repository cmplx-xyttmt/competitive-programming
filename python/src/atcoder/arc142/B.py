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


def fill_row(start, row):
    for i in range(0, len(row), 2):
        row[i] = start
        start += 1
    for i in range(1, len(row), 2):
        row[i] = start
        start += 1


def solve():
    n = read_int()
    grid = [[0 for _ in range(n)] for _ in range(n)]
    start = 1
    for i in range(n):
        fill_row(start, grid[i])
        start += n
    ans = '\n'.join(map(lambda x: ' '.join(map(str, x)), grid))
    print_(f"{ans}\n")


if __name__ == '__main__':
    solve()
