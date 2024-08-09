import math
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
        pow_3 = 3
        steps = 1
        while pow_3 <= l:
            pow_3 *= 3
            steps += 1
        total_steps = steps * 2
        prev = l + 1
        # print(f"==={l},{r}===")
        while pow_3 <= r:
            # print(f"{prev} -> {pow_3 - 1} = {steps} steps")
            total_steps += (pow_3 - prev) * steps
            prev = pow_3
            pow_3 *= 3
            steps += 1
        # print(f"{prev} -> {r} = {steps} steps")
        total_steps += (r - prev + 1) * steps
        print_(f"{total_steps}\n")
        # print(f"=========")


if __name__ == '__main__':
    solve()
