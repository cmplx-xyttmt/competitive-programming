from typing import List
import sys

sys.stdin = open("file_template.in", "r")
sys.stdout = open("file_template.out", "w")

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
    pass


if __name__ == '__main__':
    solve()
    