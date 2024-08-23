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
        a = read_line()
        important = False
        if len(a) > 2 and a.startswith('10'):
            x = a[2:]
            important = not x.startswith('0') and int(x) >= 2
        print_(f"{'YES' if important else 'NO'}\n")


if __name__ == '__main__':
    solve()
