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
        s = read_line()
        unique_letters = set(list(s))
        balanced = True
        for c in unique_letters:
            max_occur = 0
            occ = defaultdict(int)
            for ch in s:
                if ch == c:
                    occ = defaultdict(int)
                else:
                    occ[ch] += 1
                    max_occur = max(occ[ch], max_occur)
            if max_occur >= 2:
                balanced = False
                break

        print_(f"{'YES' if balanced else 'NO'}\n")


if __name__ == '__main__':
    solve()
