import bisect
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
    n = read_int()
    a = read_ints()
    b = read_ints()
    c = read_ints()

    a.sort()
    b.sort()

    ba = []
    for i in range(n):
        ba.append(bisect.bisect_right(a, b[i] - 1))
        if len(ba) >= 2:
            ba[-1] += ba[-2]
    ans = 0
    for num in c:
        i = bisect.bisect_right(b, num - 1)
        if i - 1 >= 0:
            ans += ba[i - 1]
    print_(f"{ans}\n")


if __name__ == '__main__':
    solve()
