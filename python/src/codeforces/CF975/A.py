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
        n = read_int()
        a = read_ints()
        odd_max, odd_num = 0, 0
        even_max, even_num = 0, 0
        for i in range(n):
            if i % 2 == 1:
                odd_num += 1
                odd_max = max(odd_max, a[i])
            else:
                even_num += 1
                even_max = max(even_max, a[i])
        print_(f"{max(even_max + even_num, odd_max + odd_num)}\n")


if __name__ == '__main__':
    solve()
