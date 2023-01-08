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
    t = read_int()

    for test in range(t):
        n = read_int()
        ratings = read_ints()
        sorted_ratings = list(sorted(ratings))

        ans = [-1] * n
        for i, r in enumerate(ratings):
            mentor_idx = bisect_left(sorted_ratings, 2 * r + 1) - 1
            if mentor_idx >= 0:
                if r == sorted_ratings[mentor_idx]:
                    mentor_idx -= 1
                if mentor_idx >= 0:
                    ans[i] = sorted_ratings[mentor_idx]
        print_(f"Case #{test + 1}: {' '.join(map(str, ans))}\n")


if __name__ == '__main__':
    solve()
