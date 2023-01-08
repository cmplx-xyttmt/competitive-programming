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
        s = read_line()
        if len(s) < 2:
            print_(f"Bob {ord(s) - ord('a') + 1}\n")
        else:
            end = 0
            if len(s) % 2 == 1:
                end = 1
            al = sum((ord(c) - ord('a') + 1) for c in s)
            score1 = sum((ord(c) - ord('a') + 1) for c in s[:len(s) - end])
            score2 = sum((ord(c) - ord('a') + 1) for c in s[end:])
            alice = max(score1, score2)
            print_(f"Alice {alice - (al - alice)}\n")


if __name__ == '__main__':
    solve()
