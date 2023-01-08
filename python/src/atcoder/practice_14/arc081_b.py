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
    grid = [read_line(), read_line()]
    skip = False
    pattern = []
    for i in range(n):
        if skip:
            skip = False
            continue
        if grid[0][i] == grid[1][i]:
            pattern.append('x')
        else:
            pattern.append('y')
            skip = True

    ans = 3 if pattern[0] == 'x' else 6
    mod = int(1e9) + 7
    for i in range(1, len(pattern)):
        if pattern[i - 1] == 'x':
            nxt = 2
        elif pattern[i] == 'y':
            nxt = 3
        else:
            nxt = 1
        ans = (ans * nxt) % mod
    print_(f"{ans}\n")


if __name__ == '__main__':
    solve()
