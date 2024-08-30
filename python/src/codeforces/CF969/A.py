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
    # 3 4 5 6 7
    # 10 11 12 13 14 15 16 17 18 19 20 21
    t = read_int()
    for _ in range(t):
        l, r = read_ints()
        if l % 2 == 0:
            l += 1
        ops = 0
        while l <= r:
            l += 3
            if l <= r + 1:
                ops += 1
            l += 1
        print_(f"{ops}\n")


if __name__ == '__main__':
    solve()
