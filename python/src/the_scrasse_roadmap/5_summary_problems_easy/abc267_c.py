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
    n, m = read_ints()
    a = read_ints()
    curr = sum([(i + 1) * a[i] for i in range(m)])

    subsum = sum(a[:m])
    ans = curr
    for i in range(m, n):
        subsum += a[i]
        curr += (m + 1) * a[i] - subsum
        ans = max(ans, curr)
        subsum -= a[i - m]

    print_(f"{ans}\n")


if __name__ == '__main__':
    solve()
