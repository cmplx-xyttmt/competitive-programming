import sys

fast_input = sys.stdin.readline
fast_print = sys.stdout.write

if __name__ == '__main__':
    n = int(fast_input())
    nums = []
    for _ in range(n):
        nums.append(int(fast_input()))
    goal = max(nums)
    INF = float('inf')
    jumps = [INF for _ in range(n)]
    for _i in range(n):
        if nums[_i] == goal:
            jumps[_i] = 0

    def update_jumps(left, right, step):
        prev_highest = []
        for i in range(left, right, step):
            while prev_highest and nums[i] >= nums[prev_highest[-1]]:
                prev_highest.pop()
            if prev_highest:
                j = prev_highest[-1]
                jumps[i] = min(jumps[i], 1 + jumps[j])
            prev_highest.append(i)

    update_jumps(0, n, 1)
    print(jumps)
    update_jumps(n - 1, -1, -1)

    # fast_print(f"{' '.join(map(str, nums))}\n")
    fast_print(" ".join(map(str, jumps)))
