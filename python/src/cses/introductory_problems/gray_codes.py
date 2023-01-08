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
    length = 1 << n
    start = 1
    ans = [0] * length
    for _ in range(n):
        for i in range(start):
            ans[start + i] = start + ans[start - i - 1]
        start <<= 1

    ans = '\n'.join(map(lambda x: bin(x)[2:].zfill(n), ans))
    print_(f"{ans}\n")


if __name__ == '__main__':
    solve()
