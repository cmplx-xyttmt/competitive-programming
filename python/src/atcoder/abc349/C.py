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


def is_airport_code(s: str, t):
    j = 0
    for c in s:
        if t[j] == c.upper():
            j += 1
        if j == 2 and t[j] == 'X':
            return "Yes"
        if j == 3:
            return "Yes"
    return "No"


def solve():
    s = read_line()
    t = read_line()
    print_(f"{is_airport_code(s, t)}\n")


if __name__ == '__main__':
    solve()
