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


def length(n_min, n_max, in_bounds):
    if min(n_min, n_max, in_bounds) == -1:
        return 0

    return max(0, in_bounds - max(n_min, n_max) + 1)


def solve():
    n, mx, mn = read_ints()
    a = read_ints()
    n_min, n_max, in_bounds = -1, -1, -1
    ans = 0
    for i in range(n - 1, -1, -1):
        if a[i] == mn:
            n_min = i
        if a[i] == mx:
            n_max = i
        if a[i] < mn or a[i] > mx:
            in_bounds = -1
        if in_bounds == -1 and mn <= a[i] <= mx:
            in_bounds = i
        # print(f"{i} -> {length(n_min, n_max, in_bounds)} // ", n_min, n_max, in_bounds)
        ans += length(n_min, n_max, in_bounds)

    print_(f"{ans}\n")


if __name__ == '__main__':
    solve()
