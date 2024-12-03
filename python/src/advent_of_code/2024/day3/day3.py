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


def find_muls(data):
    start = 0
    total = 0
    while True:
        start = data[start:].find("mul(") + start + 3
        if 0 <= start < len(data):
            end = data[start:].find(")") + start
            if 0 <= end < len(data):
                nums = data[start + 1: end].split(",")
                if len(nums) != 2:
                    continue
                if not (nums[0].isnumeric() and nums[1].isnumeric()):
                    continue
                print("nums: ", nums[0], nums[1])
                total += int(nums[0]) * int(nums[1])
                start = end
            else:
                break
        else:
            break
    return total


def solve():
    data = read_line()
    ans1 = 0
    while data:
        ans1 += find_muls(data)
        data = read_line()
    print(f"Part 1: {ans1}")


if __name__ == '__main__':
    solve()
