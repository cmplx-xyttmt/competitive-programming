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
    n, m = read_ints()
    a = read_ints()
    ans = float('inf')
    mex = 0
    seen = defaultdict(int)
    nxt_mex = mex + 1
    for i in range(n - 1, -2, -1):
        while seen[mex] > 0:
            mex += 1
        if i + m < n:
            ans = min(ans, mex)
            # print(i, mex)
            rem = a[i + m]
            seen[rem] -= 1
            if rem < mex and seen[rem] == 0:
                nxt_mex = mex
                mex = rem

        if i >= 0:
            seen[a[i]] += 1
            if i + m < n and a[i] == mex and seen[a[i]] == 1:
                mex = nxt_mex

    print_(f"{ans}\n")


if __name__ == '__main__':
    solve()
