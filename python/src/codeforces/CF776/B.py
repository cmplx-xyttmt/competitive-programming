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
        l, r, a = read_ints()
        ans = r // a + r % a
        k = r - (r % a) - 1
        if k >= l:
            ans = max(ans, k // a + k % a)
        print_(f"{ans}\n")


if __name__ == '__main__':
    solve()
