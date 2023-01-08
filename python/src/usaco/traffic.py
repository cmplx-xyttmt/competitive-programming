from typing import List
import sys

sys.stdin = open("traffic.in", "r")
sys.stdout = open("traffic.out", "w")

input_ = sys.stdin.readline
print_ = sys.stdout.write
flush = sys.stdout.flush


def readline() -> str:
    return input_().strip()


def read_int() -> int:
    return int(readline())


def read_strings() -> List[str]:
    return list(readline().split())


def read_ints():
    return list(map(int, readline().split()))


def solve():
    n = read_int()
    lo, hi, add_lo, add_hi, off_lo, off_hi = -1, int(1e6), 0, 0, 0, 0

    for _ in range(n):
        line = read_strings()
        lower, upper = map(int, line[1:])
        if line[0] == "none":
            lo = max(lower - add_lo + off_lo, lo)
            hi = min(upper - add_hi + off_hi, hi)
        elif line[0] == "on":
            add_lo += lower
            add_hi += upper
        else:
            if lo != -1:
                upper = min(upper, lo + add_lo)
                lower = min(lower, hi + add_hi)
            off_lo += upper
            off_hi += lower
        sys.stderr.write(f"{lo} {hi} {add_lo} {add_hi} {off_lo} {off_hi}\n")

    print_(f"{lo} {hi}\n")
    print_(f"{lo + add_lo} {hi + add_hi}\n")


if __name__ == '__main__':
    solve()
