from typing import List
import sys

# https://atcoder.jp/contests/dp/tasks/dp_c
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
    prev = read_ints()
    for i in range(1, n):
        happiness = read_ints()
        curr = [happiness[j] + max(prev[k] for k in range(3) if k != j)
                for j in range(3)]
        prev = curr
    print(max(prev))


if __name__ == '__main__':
    solve()
