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
    special_chars = ['#', '@', '*', '&']
    for test in range(1, t + 1):
        n = read_int()
        p = read_line()
        uppercase = 0
        lowercase = 0
        digits = 0
        special = 0
        for c in p:
            if c in special_chars:
                special += 1
            if 0 <= ord(c) - ord('A') < 26:
                uppercase += 1
            if 0 <= ord(c) - ord('a') < 26:
                lowercase += 1
            if c.isdigit():
                digits += 1

        if uppercase == 0:
            p += 'A'
        if lowercase == 0:
            p += 'a'
        if digits == 0:
            p += '0'
        if special == 0:
            p += '#'

        if len(p) < 7:
            p = p + 'a' * (7 - len(p))

        print_(f"Case #{test}: {p}\n")


if __name__ == '__main__':
    solve()
