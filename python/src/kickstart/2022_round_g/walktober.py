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

    for test in range(1, t + 1):
        m, n, p = read_ints()
        maximums = [-sys.maxsize for _ in range(n)]
        johns_scores = []
        for i in range(m):
            scores = read_ints()
            for j in range(n):
                maximums[j] = max(maximums[j], scores[j])
            if i == p - 1:
                johns_scores = scores

        ans = sum([max(0, maximums[j] - johns_scores[j]) for j in range(n)])
        print_(f"Case #{test}: {ans}\n")


if __name__ == '__main__':
    solve()
