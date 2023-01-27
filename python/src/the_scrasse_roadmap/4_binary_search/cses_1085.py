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


def can(s, k, array):
    curr_sum = 0
    subarrays = 0
    for num in array:
        if curr_sum + num > s:
            if num > s:
                return False
            subarrays += 1
            curr_sum = 0
        curr_sum += num
    subarrays += 1
    return subarrays <= k


def solve():
    # 1, 2, 3, ... b ..., total
    # for s >= b: can divide array into <= k subarrays
    # for s < b: can only make > k subarrays
    n, k = read_ints()
    array = read_ints()
    low = max(array) - 1
    high = sum(array)

    while high - low > 1:
        mid = (low + high) // 2
        if can(mid, k, array):
            high = mid
        else:
            low = mid

    print_(f"{high}\n")


if __name__ == '__main__':
    solve()
