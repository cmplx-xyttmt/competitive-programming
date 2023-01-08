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
        if s > 'atcoder':
            print(0)
            continue
        n = len(s)
        found = False
        for i in range(n):
            if s[i] != 'a':
                found = True
                print(i if i == 1 or ord(s[i]) <= ord('t') else i - 1)
                break
        if not found:
            print(-1)


if __name__ == '__main__':
    solve()
