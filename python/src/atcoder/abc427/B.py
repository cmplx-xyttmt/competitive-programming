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

    def f(x):
        if x == 0:
            return 1
        x = str(x)
        return sum(map(int, x))

    n = read_int()
    a_i = 1

    f_a_i1 = 1
    total_i1 = 1
    total_i2 = 0
    for i in range(1, n + 1):
        a_i = total_i2 + f_a_i1
        f_a_i1 = f(a_i)
        total_i2 = total_i1
        total_i1 += f_a_i1

    print(a_i)


if __name__ == '__main__':
    solve()
