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
    n, k = read_ints()
    a = read_ints()
    b = set(read_ints())
    max_tastiness = max(a)

    max_indices = {i + 1 for i in range(n) if a[i] == max_tastiness}

    print_(f"{'Yes' if max_indices.intersection(b) else 'No'}\n")


if __name__ == '__main__':
    solve()
