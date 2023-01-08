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
        v = read_ints()
        max_prev = -1
        rec = 0
        for i in range(n):
            if v[i] > max_prev and (i == n - 1 or v[i] > v[i + 1]):
                rec += 1
            max_prev = max(max_prev, v[i])
        print_(f"Case #{test + 1}: {rec}\n")


if __name__ == '__main__':
    solve()
