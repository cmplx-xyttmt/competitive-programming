import time
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


def calc_x(a, b):
    # ab = a + b
    # return ab * (2 * (ab ** 2) - 2 * a * b)
    return a ** 3 + (a ** 2) * b + a * (b ** 2) + b ** 3


def get_b(a, n):
    if calc_x(a, a) >= n:
        return a
    left = a
    right = int(1e6)

    while right - left > 1:
        b = (left + right) // 2
        if calc_x(a, b) >= n:
            right = b
        else:
            left = b

    return right


def solve():
    # binary search
    n = read_int()
    start = round(time.time())
    ans = float('inf')
    for a in range(int(1e6)):
        b = get_b(a, n)
        ans = min(ans, calc_x(a, b))

    print_(f"{ans}\n")
    print(f"Time taken: {round(time.time()) - start} seconds")


def solution2():
    # two pointers
    n = read_int()
    # start = round(time.time())
    j = int(1e6)
    ans = float('inf')
    for i in range(int(1e6) + 1):
        while calc_x(i, j) >= n and j >= 0:
            # print(i, j)
            ans = min(ans, calc_x(i, j))
            j -= 1

    print_(f"{ans}\n")
    # print(f"Time taken: {round(time.time()) - start} seconds")


if __name__ == '__main__':
    # solve()
    solution2()
