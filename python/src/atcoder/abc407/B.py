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
    x, y = read_ints()
    pxy = 0
    for a in range(1, 7):
        for b in range(1, 7):
            if a + b >= x or abs(a - b) >= y:
                pxy += 1
    print(pxy / 36)


if __name__ == '__main__':
    solve()
