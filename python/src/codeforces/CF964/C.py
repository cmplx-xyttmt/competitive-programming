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
        n, s, m = read_ints()
        last_time_slot = 0
        can = False
        for _ in range(n):
            l, r = read_ints()
            if l - last_time_slot >= s:
                can = True
            last_time_slot = r
        if m - last_time_slot >= s:
            can = True
        print_(f"{'YES' if can else 'NO'}\n")


if __name__ == '__main__':
    solve()
