from typing import List
import sys
from bisect import bisect_left

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
    n = read_int()
    endpoints = []
    for _ in range(n):
        t, b = read_ints()
        endpoints.append((t, b))
    endpoints.sort(reverse=True)
    lis = []
    for _, num in endpoints:
        idx = bisect_left(lis, num)
        if idx == len(lis):
            lis.append(num)
        else:
            lis[idx] = num

    print_(f"{len(lis)}\n")


if __name__ == '__main__':
    solve()
