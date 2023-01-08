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
    s = list(read_line())
    t = list(read_line())
    can = True
    moves = 0
    for i in range(n - 1, -1, -1):
        if s[i] == '0' and t[i] == '1':
            can = False
            break
        elif s[i] != t[i]:
            if i == 0:
                can = False
            else:
                moves += 1
                s[i - 1] = '1' if s[i - 1] == '0' else '0'
    print_(f"{moves if can else -1}\n")


if __name__ == '__main__':
    solve()
