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

    for test in range(t):
        n = read_int()
        coverage = read_ints()
        buses = []
        for i in range(0, 2 * n, 2):
            buses.append((coverage[i], coverage[i + 1]))

        p = read_int()
        ans = []
        for _ in range(p):
            c = read_int()
            covered = 0
            for a, b in buses:
                if a <= c <= b:
                    covered += 1
            ans.append(covered)
        print_(f"Case #{test + 1}: {' '.join(map(str, ans))}\n")
        read_line()


if __name__ == '__main__':
    solve()
