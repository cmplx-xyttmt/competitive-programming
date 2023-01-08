import sys

sys.stdin = open('input.in', 'r')

input = sys.stdin.readline

if __name__ == '__main__':
    nums = []
    num = int(input())
    nums.append(num)

    increases = 0
    while True:
        prev = num
        num = input()
        if not num:
            break
        else:
            num = int(num)
        nums.append(num)
        if num > prev:
            increases += 1
    print(f"Part 1: {increases}")

    increases = 0
    curr_sum = float('inf')
    for i in range(0, len(nums) - 2):
        prev_sum = curr_sum
        curr_sum = nums[i] + nums[i + 1] + nums[i + 2]
        if curr_sum > prev_sum:
            increases += 1

    print(f"Part 2: {increases}")
