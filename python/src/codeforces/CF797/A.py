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
        n = read_int()
        start = n // 3
        h1, h2, h3 = 0, 0, 0
        found = False
        while True:
            h1 = start
            for sub in range(1, h1):
                h2 = h1 - sub
                h3 = n - h1 - h2
                if h1 > h2 > h3 > 0:
                    found = True
                    break
                if h3 >= h2:
                    break
            if found:
                break
            start += 1
        print_(f"{h2} {h1} {h3}\n")


if __name__ == '__main__':
    solve()
