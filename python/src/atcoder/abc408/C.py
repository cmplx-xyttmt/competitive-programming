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
    castles = [0 for _ in range(n)]
    for _ in range(m):
        l, r = read_ints()
        l -= 1
        r -= 1
        castles[l] += 1
        if r + 1 < n:
            castles[r + 1] -= 1
    for i in range(1, n):
        castles[i] += castles[i - 1]

    print(min(castles))


if __name__ == '__main__':
    solve()
