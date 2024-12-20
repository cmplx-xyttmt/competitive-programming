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


def is_safe(nums):
    if nums[0] == nums[1]:
        return False
    increments = 0
    decrements = 0
    prev = nums[0]
    for i in range(1, len(nums)):
        if 1 <= abs(nums[i] - prev) <= 3:
            if nums[i] > prev:
                increments += 1
            else:
                decrements += 1
        else:
            return False
        if increments > 0 and decrements > 0:
            return False
        prev = nums[i]
    return True


def is_safe_rem(nums):
    if is_safe(nums):
        return True
    for i in range(len(nums)):
        if is_safe(nums[0:i] + nums[i + 1:]):
            return True
    return False


def solve():
    nums = read_ints()
    safe = 0
    safe_rem = 0
    while nums:
        safe += is_safe(nums)
        safe_rem += is_safe_rem(nums)
        nums = read_ints()
    print(f"Part 1: {safe}")
    print(f"Part 2: {safe_rem}")


if __name__ == '__main__':
    solve()
