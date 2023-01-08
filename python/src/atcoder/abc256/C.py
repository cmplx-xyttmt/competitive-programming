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
    h1, h2, h3, w1, w2, w3 = read_ints()
    ways = 0
    for a in range(1, 30):
        for b in range(1, 30):
            for c in range(1, 30):
                for d in range(1, 30):
                    e = h1 - a - b
                    f = h2 - c - d
                    g = w1 - a - c
                    h = w2 - b - d
                    i = h3 - g - h
                    i2 = w3 - e - f
                    if i == i2 and all([x > 0 for x in [e, f, g, h, i]]):
                        ways += 1
    print_(f"{ways}\n")


if __name__ == '__main__':
    solve()
