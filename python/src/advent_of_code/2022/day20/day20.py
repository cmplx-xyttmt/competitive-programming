from typing import List
import sys

sys.stdin = open("day20.in", "r")
sys.stdout = open("day20.out", "w")

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


def mix(new_nums):

    for i in range(len(new_nums)):
        curr_i = [idx for _, idx in new_nums].index(i)
        orig_num, _ = new_nums.pop(curr_i)
        new_i = (curr_i + orig_num) % len(new_nums)
        new_nums.insert(new_i, (orig_num, i))
        # sys.stderr.write(f"To: {orig_num} {[n for n, _, in new_nums]}\n=====\n")

    zero = [num for num, _ in new_nums].index(0)
    one = new_nums[(zero + 1000) % len(new_nums)][0]
    two = new_nums[(zero + 2000) % len(new_nums)][0]
    three = new_nums[(zero + 3000) % len(new_nums)][0]
    return one + two + three


def solve():

    line = read_line()
    nums = []
    while line:
        nums.append(int(line))
        line = read_line()

    sys.stderr.write(f"Size: {len(nums)} Unique: {len(set(nums))} Max: {max(nums)} Min: {min(nums)}\n")

    new_nums = [(num, i) for i, num in enumerate(nums)]

    print(f"Part 1: {mix(new_nums)}")
    # 5974 too low

    new_nums = [(num * 811589153, i) for i, num in enumerate(nums)]

    ans = 0
    for i in range(10):
        ans = mix(new_nums)
    print(f"Part 1: {ans}")


if __name__ == '__main__':
    solve()
