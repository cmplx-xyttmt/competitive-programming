from collections import defaultdict
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
        n = read_int()
        a = read_ints()
        majority = 0
        occ = defaultdict(int)
        for num in a:
            occ[num] += 1
            majority = max(majority, occ[num])

        ans = 0
        while majority < n:
            ans += 1
            ans += min(n - majority, majority)
            majority += min(n - majority, majority)

        print(ans)


if __name__ == '__main__':
    solve()
