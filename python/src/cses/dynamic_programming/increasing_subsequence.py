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
    x = read_ints()
    lis = []
    for num in x:
        idx = bisect_left(lis, num)
        if idx == len(lis):
            lis.append(num)
        else:
            lis[idx] = num

    print(len(lis))


if __name__ == '__main__':
    solve()
