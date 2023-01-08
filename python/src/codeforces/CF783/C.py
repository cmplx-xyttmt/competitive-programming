from typing import List
import sys
import math

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


def steps(first, a):
    curr = a[0] * -first
    moves = first
    for i in range(1, len(a)):
        b = math.ceil(curr / a[i])
        if b * a[i] == curr:
            b += 1
        curr = b * a[i]
        moves += abs(b)
    return moves


def solve():
    read_int()
    a = read_ints()
    left = 0
    right = 5000 * int(1e9)
    while right - left > 1:
        mid = (left + right) // 2
        # print(left, right, mid)
        moves = steps(mid, a)
        moves1 = steps(mid + 1, a)
        if moves < moves1:
            right = mid
        else:
            left = mid

    print(steps(right, a))


if __name__ == '__main__':
    solve()
