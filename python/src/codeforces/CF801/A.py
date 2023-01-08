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
        n, m = read_ints()
        max_i, max_j = -1, -1
        inf = int(1e9) + 1
        curr_max = -inf
        for i in range(n):
            nums = read_ints()
            for j in range(m):
                if nums[j] > curr_max:
                    max_i, max_j = i, j
                    curr_max = nums[j]

        print_(f"{max(max_i + 1, n - max_i) * max(max_j + 1, m - max_j)}\n")


if __name__ == '__main__':
    solve()
