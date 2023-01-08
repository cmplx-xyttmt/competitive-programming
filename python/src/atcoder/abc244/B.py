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
    t = read_line()
    x, y = (0, 0)
    directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    dx, dy = directions[0]
    curr_direction = 0
    for i in range(n):
        if t[i] == 'S':
            x, y = x + dx, y + dy
        else:
            curr_direction = (curr_direction + 1) % 4
            dx, dy = directions[curr_direction]

    print(x, y)


if __name__ == '__main__':
    solve()
