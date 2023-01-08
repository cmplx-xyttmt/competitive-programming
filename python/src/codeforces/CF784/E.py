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
        first = defaultdict(int)
        second = defaultdict(int)
        all_ = defaultdict(int)
        words = []
        for _ in range(n):
            s = read_line()
            first[s[0]] += 1
            second[s[1]] += 1
            all_[s] += 1
            words.append(s)

        total = 0
        for s in words:
            total += first[s[0]] + second[s[1]] - 2 * all_[s]

        print_(f"{total // 2}\n")


if __name__ == '__main__':
    solve()
