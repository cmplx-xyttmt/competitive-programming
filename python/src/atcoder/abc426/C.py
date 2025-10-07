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
    n, q = read_ints()
    version_counts = [0] + [1 for _ in range(n)]
    hx = 1
    # version_counts = [1, 1, 1, 1, 1, 1, 1, 1]
    # x, y - (2, 6), (3, 5), (1, 7), (5, 7), (7, 8)
    # 2, 6 -> [0, 0, 1, 1, 1, 3, 1, 1] -> 2
    # 3, 5 -> [0, 0, 0, 1, 2, 3, 1, 1] -> 1
    # 1, 7 -> [0, 0, 0, 1, 2, 3, 1, 1] -> 0
    # 5, 7 -> [0, 0, 0, 0, 0, 3, 4, 1] -> 3
    # 7, 8 -> [0, 0, 0, 0, 0, 0, 0, 8] -> 7
    # query: how many are <= x  -> sum(vc[hx..x])
    # update: make all <= x equal to y  vc[0..x] = 0 (update highest x, hx), vc[y] = sum(vc[hx..x])
    # sum(vc[hx..x]) = vc[hx] + ... + vc[x], hx = x, (works because updating the highest seen x leaves the time complexity linear across all queries; each index is touched at most once)
    for _ in range(q):
        x, y = read_ints()
        upgraded = 0
        if x >= hx:
            for i in range(hx, x + 1):
                upgraded += version_counts[i]
                version_counts[i] = 0
            hx = x
            version_counts[y] += upgraded
            print_(f"{upgraded}\n")
        else:
            print_("0\n")


if __name__ == '__main__':
    solve()
