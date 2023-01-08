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
        l, r = read_ints()
        if l % 2 == 0:
            print(l, l + 1, l + 2, l + 3)
        elif l + 4 <= r:
            print(l + 1, l + 2, l + 3, l + 4)
        else:
            print(-1)


if __name__ == '__main__':
    solve()
