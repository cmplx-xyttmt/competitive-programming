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
        a = read_ints()
        s = read_line()
        left = 0
        right = n - 1
        to_add = []
        while left < right:
            if s[left] == 'L' and s[right] == 'R':
                to_add.append((left, right))
                left += 1
                right -= 1
            elif s[left] == 'L' and s[right] == 'L':
                right -= 1
            elif s[left] == 'R' and s[right] == 'R':
                left += 1
            else:
                left += 1
                right -= 1
        prefix = [a[0]]
        for i in range(1, n):
            prefix.append(prefix[i - 1] + a[i])

        ans = 0
        for (left, right) in to_add:
            ans += prefix[right] - (0 if left == 0 else prefix[left - 1])
        print_(f"{ans}\n")


if __name__ == '__main__':
    solve()
