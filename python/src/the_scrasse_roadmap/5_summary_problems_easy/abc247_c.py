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


def sequence(n):
    if n == 1:
        return "1"
    s_n1 = sequence(n - 1)
    return f"{s_n1} {n} {s_n1}"

def solve():
    n = read_int()
    print_(sequence(n))


if __name__ == '__main__':
    solve()
