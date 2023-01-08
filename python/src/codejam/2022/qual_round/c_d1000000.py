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

    for case in range(t):
        n = read_int()
        s = read_ints()
        s.sort()
        ans = 0
        need = 1
        for i in range(n):
            if s[i] >= need:
                ans += 1
                need += 1

        print_(f"Case #{case + 1}: {ans}\n")


if __name__ == '__main__':
    solve()
