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


def nums_less(num, n):
    less = 0
    for div in range(1, n + 1):
        less += min(n, num // div)
    return less


def brute(n):
    nums = []
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            nums.append(i * j)

    nums.sort()
    # print(nums)
    return nums[len(nums) // 2]


def solve():
    n = read_int()
    lo = 1
    hi = n * n
    midpoint = hi // 2
    while (hi - lo) > 1:
        mid = (hi + lo) // 2
        less_equal = nums_less(mid, n)
        # print(mid, less_equal)
        if less_equal >= midpoint + 1:
            hi = mid
        else:
            lo = mid

    print_(f"{hi}\n")
    # print(f"Brute: {brute(n)}")


if __name__ == '__main__':
    solve()
