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
        n, x = read_ints()
        if n % 2 == 0:
            print("YES")
        else:
            print("YES" if x % 2 == 1 else "NO")


if __name__ == '__main__':
    solve()
