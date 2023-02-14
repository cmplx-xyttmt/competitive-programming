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
    n, k = read_ints()
    a = read_ints()
    mods_sorted = defaultdict(list)

    a_sorted = sorted(a)
    for i, num in enumerate(a_sorted):
        mods_sorted[num].append(i % k)

    mods = defaultdict(list)
    for i, num in enumerate(a):
        mods[num].append(i % k)

    can = True
    for num in mods.keys():
        uns = mods[num]
        sor = mods_sorted[num]
        uns.sort()
        sor.sort()
        if tuple(uns) != tuple(sor):
            can = False

    print_(f"{'Yes' if can else 'No'}\n")


if __name__ == '__main__':
    solve()
