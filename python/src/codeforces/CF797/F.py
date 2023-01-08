import math
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


def find_rotations(s):
    tmp = s + s
    n = len(s)
    for i in range(1, n + 1):
        if s == tmp[i:i + n]:
            return i
    return n


def get_lcm(nums):
    lcm = nums[0]
    for i in range(1, len(nums)):
        lcm = lcm * nums[i] // math.gcd(lcm, nums[i])
    return lcm


def solve():
    t = read_int()
    for _ in range(t):
        n = read_int()
        s = read_line()
        p = read_ints()
        indices = dict()
        for i, num in enumerate(p):
            indices[num] = i + 1
        cycles = []
        seen = set()
        for i in range(1, n + 1):
            if i in seen:
                continue
            cycle = []
            k = i
            while k not in seen:
                seen.add(k)
                cycle.append(s[k - 1])
                k = indices[k]
            cycles.append(''.join(cycle))
        nums = [find_rotations(cycle) for cycle in cycles]
        print(get_lcm(nums))


if __name__ == '__main__':
    solve()
