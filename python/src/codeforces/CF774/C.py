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
    factorials = [math.factorial(i) for i in range(1, 15)]
    poss = 1 << 14
    for _ in range(t):
        n = read_int()
        ans = n
        for mask in range(poss):
            total = 0
            ones = 0
            for i in range(14):
                if mask & (1 << i):
                    total += factorials[i]
                    ones += 1
            if total <= n:
                twos = bin(n - total)[2:].count('1')
                ans = min(ans, ones + twos)

        print(ans)


if __name__ == '__main__':
    solve()
