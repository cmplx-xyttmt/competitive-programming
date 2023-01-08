import math
from typing import List
import sys

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
    t = read_int()

    for _ in range(t):
        n, s = read_ints()
        ans = math.ceil((s - (n - 1) * (n + 1)) / (n ** 2 - n + 1))

        print(max(0, ans))


if __name__ == '__main__':
    solve()
