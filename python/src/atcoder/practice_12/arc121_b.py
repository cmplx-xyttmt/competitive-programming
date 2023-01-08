import bisect
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


def closest_diff(num, array):
    idx = bisect.bisect_left(array, num)
    idx1 = idx - 1
    # print(num, array, idx)
    ans = int(1e18)
    if 0 <= idx < len(array):
        ans = min(ans, abs(array[idx] - num))
    if 0 <= idx1 < len(array):
        ans = min(ans, abs(array[idx1] - num))
    return ans


def solve():
    n = read_int()
    colors = defaultdict(list)
    for _ in range(2 * n):
        a, c = read_strings()
        a = int(a)
        colors[c].append(a)

    all_even = all([len(lst) % 2 == 0 for lst in colors.values()])
    if all_even:
        print_(f"0\n")
    else:
        rg, gb, rb = [int(1e18)] * 3
        even = 'R' if len(colors['R']) % 2 == 0 else ('G' if len(colors['G']) % 2 == 0 else 'B')
        colors['R'].sort()
        colors['G'].sort()
        colors['B'].sort()
        for num in colors['R']:
            rg = min(rg, closest_diff(num, colors['G']))
            rb = min(rb, closest_diff(num, colors['B']))

        for num in colors['G']:
            gb = min(gb, closest_diff(num, colors['B']))
        # print(even, rg, gb, rb)
        if even == 'R':
            if not colors['R']:
                ans = gb
            else:
                ans = min(rg + rb, gb)
        elif even == 'G':
            if not colors['G']:
                ans = rb
            else:
                ans = min(rg + gb, rb)
        else:
            if not colors['B']:
                ans = rg
            else:
                ans = min(rb + gb, rg)
        print_(f"{ans}\n")


if __name__ == '__main__':
    solve()
