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


def safe_get2d(array, i, j):
    return 0 if not (0 <= i < len(array)) else array[i][j]


def num_operations(prefix_a, prefix_b, l, r):
    ops = 0
    for char in range(26):
        a_freq = prefix_a[r][char] - safe_get2d(prefix_a, l - 1, char)
        b_freq = prefix_b[r][char] - safe_get2d(prefix_b, l - 1, char)
        ops += abs(a_freq - b_freq)
    return ops // 2


def solve():
    t = read_int()
    for _ in range(t):
        n, q = read_ints()
        a = read_line()
        b = read_line()
        prefix_a = [[0 for _ in range(26)] for _ in range(n)]
        prefix_b = [[0 for _ in range(26)] for _ in range(n)]
        for i in range(n):
            value_a = ord(a[i]) - ord('a')
            value_b = ord(b[i]) - ord('a')
            for j in range(26):
                prefix_a[i][j] = safe_get2d(prefix_a, i - 1, j) + int(value_a == j)
                prefix_b[i][j] = safe_get2d(prefix_b, i - 1, j) + int(value_b == j)

        for _ in range(q):
            l, r = read_ints()
            print_(f"{num_operations(prefix_a, prefix_b, l - 1, r - 1)}\n")


if __name__ == '__main__':
    solve()
