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


def solve():
    t = read_int()
    for _ in range(t):
        n = read_int()
        p = read_ints()
        if n == 1:
            print_(f"-1\n")
            continue
        nums = [i for i in range(1, n + 1)]
        nums.reverse()
        ans = []
        while len(nums) > 2:
            if p[len(ans)] == nums[-1]:
                nums[-1], nums[-2] = nums[-2], nums[-1]
            # print(nums)
            ans.append(nums.pop())

        ans.append(nums.pop())
        ans.append(nums.pop())
        if p[-1] == ans[-1] or p[-2] == ans[-2]:
            ans[-1], ans[-2] = ans[-2], ans[-1]
        print_(f"{' '.join(map(str, ans))}\n")


if __name__ == '__main__':
    solve()
