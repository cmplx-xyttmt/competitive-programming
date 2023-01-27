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


def can_invite(k, constraints):
    invited = 0
    n = len(constraints)
    for i, (a, b) in enumerate(constraints):
        # print(k, "-> ", i, invited, min(a, n - i - 1))
        if invited <= b and invited + min(a, n - i - 1) + 1>= k:
            invited += 1
    # check this old submission for a saner approach: https://codeforces.com/contest/1610/submission/136688698
    return invited >= k


def solve():
    t = read_int()

    for _ in range(t):
        n = read_int()
        constraints = []
        for _ in range(n):
            a, b = read_ints()
            constraints.append((a, b))
        low = 1
        high = n + 1
        while high - low > 1:
            mid = (low + high) // 2
            if can_invite(mid, constraints):
                low = mid
            else:
                high = mid
        print_(f"{low}\n")


if __name__ == '__main__':
    solve()
