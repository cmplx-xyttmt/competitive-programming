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
        n, k = read_ints()
        a = read_ints()

        need = set()
        found = False
        for num in a:
            if num - k in need or num + k in need:
                found = True
                break
            need.add(num)

        print_(f"{'YES' if found else 'NO'}\n")


if __name__ == '__main__':
    solve()
