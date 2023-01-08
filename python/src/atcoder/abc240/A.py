from typing import List
import sys

input_ = sys.stdin.readline
print_ = sys.stdout.write
flush = sys.stdout.flush


def readline() -> str:
    return input_().strip()


def read_int() -> int:
    return int(readline())


def read_strings() -> List[str]:
    return list(readline().split())


def read_ints():
    return list(map(int, readline().split()))


def solve():
    a, b = read_ints()
    diff = b - a
    print("Yes" if diff == 1 or diff == 9 else "No")


if __name__ == '__main__':
    solve()
