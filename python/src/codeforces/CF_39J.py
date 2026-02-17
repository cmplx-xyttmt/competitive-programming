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
    s1 = read_line()
    s2 = read_line()

    n = len(s1)
    m = len(s2)

    prefix_len = 0
    while prefix_len < m and s1[prefix_len] == s2[prefix_len]:
        prefix_len += 1

    suffix_len = 0
    while suffix_len < m and s1[n - 1 - suffix_len] == s2[m - 1 - suffix_len]:
        suffix_len += 1

    results = []

    for i in range(1, n + 1):
        if (prefix_len >= i - 1) and (suffix_len >= n - i):
            results.append(i)

    print(len(results))
    print(*results)


if __name__ == '__main__':
    solve()
