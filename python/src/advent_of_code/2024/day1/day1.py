from collections import Counter
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
    line = read_line()
    left = []
    right = []
    while line:
        l, r = list(map(int, line.split()))
        left.append(l)
        right.append(r)
        line = read_line()

    left.sort()
    right.sort()
    distance = 0
    for l, r in zip(left, right):
        distance += abs(l - r)
    print(f"Day 1: {distance}")

    counter = Counter(right)
    similarity = 0
    for num in left:
        similarity += num * counter[num]

    print(f"Day 2: {similarity}")



if __name__ == '__main__':
    solve()
