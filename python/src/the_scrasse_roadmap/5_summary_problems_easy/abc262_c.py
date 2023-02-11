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
    n = read_int()
    a = [-1] + read_ints()

    # a[i] = i, a[j] = j
    # a[i] = j, a[j] = i
    same = 0
    alt = 0
    for i in range(1, n + 1):
        if a[i] == i:
            same += 1
        elif i == a[a[i]]:
            alt += 1

    print_(f"{alt // 2 + (same * (same - 1)) // 2}\n")


if __name__ == '__main__':
    solve()
