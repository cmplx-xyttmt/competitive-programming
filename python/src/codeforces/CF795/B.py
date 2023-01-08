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
        s = read_ints()
        groups = defaultdict(list)
        for i, si in enumerate(s):
            groups[si].append((i + 1, si))

        min_ = min([len(lst) for lst in groups.values()])
        perm = [0] * (n + 1)
        if min_ == 1:
            print_("-1\n")
        else:
            for lst in groups.values():
                k = len(lst)
                for i in range(k):
                    if k - i - 1 <= i:
                        break
                    a, _ = lst[i]
                    b, _ = lst[k - i - 1]
                    perm[a] = b
                    perm[b] = a
                if k % 2 == 1:
                    a, _ = lst[0]
                    c, _ = lst[-1]
                    # perm[a] = c, perm[c] = a
                    b, _ = lst[k // 2]
                    perm[a] = b
                    perm[b] = c
            print_(f"{' '.join(map(str, perm[1:]))}\n")


if __name__ == '__main__':
    solve()
