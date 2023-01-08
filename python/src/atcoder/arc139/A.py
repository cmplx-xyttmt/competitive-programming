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


def find_min_add(shift, p2, prev):
    left = -1
    right = (2 * prev) // (1 << shift)
    while right - left > 1:
        mid = (left + right) // 2
        val = (mid << shift) + p2
        if val > prev:
            right = mid
        else:
            left = mid

    return right


def solve():
    n = read_int()
    t = read_ints()
    a = (1 << t[0])
    for i in range(1, n):
        # print(a, bin(a)[2:])
        min_add = find_min_add(t[i] + 1, (1 << t[i]), a)
        a = (min_add << (t[i] + 1)) + (1 << t[i])
    # print(a, bin(a)[2:])
    print_(f"{a}\n")


if __name__ == '__main__':
    solve()
