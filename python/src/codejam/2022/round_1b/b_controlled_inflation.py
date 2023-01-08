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
    for test in range(1, t + 1):
        n, p = read_ints()
        h = []
        l = []
        for _ in range(n):
            nums = read_ints()
            h.append(max(nums))
            l.append(min(nums))

        h_dp = [h[0]]
        l_dp = [h[0] + h[0] - l[0]]
        for i in range(1, n):
            diff = abs(h[i] - l[i])
            h_dp.append(min(h_dp[i - 1] + abs(l[i] - h[i - 1]), l_dp[i - 1] + abs(l[i] - l[i - 1])) + diff)
            l_dp.append(min(h_dp[i - 1] + abs(h[i] - h[i - 1]), l_dp[i - 1] + abs(h[i] - l[i - 1])) + diff)

        # print(h_dp)
        # print(l_dp)
        print_(f"Case #{test}: {min(h_dp[-1], l_dp[-1])}\n")


if __name__ == '__main__':
    solve()
