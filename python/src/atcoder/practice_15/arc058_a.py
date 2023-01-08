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
    n, k = read_ints()
    d = set(read_ints())

    def is_valid(num):
        while num:
            num, rem = divmod(num, 10)
            if rem in d:
                return False
        return True

    while True:
        if is_valid(n):
            break
        n += 1

    print_(f"{n}\n")


if __name__ == '__main__':
    solve()
