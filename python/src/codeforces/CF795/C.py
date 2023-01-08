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
        n, k = read_ints()
        s = list(read_line())
        first_one = -1
        last_one = -1
        for i in range(n):
            if s[i] == '1':
                if first_one == -1:
                    first_one = i
                last_one = i
        if first_one != -1:
            steps = n - 1 - last_one
            if 0 < steps <= k:
                s[last_one], s[n - 1] = s[n - 1], s[last_one]
                k -= steps
            if 0 < first_one <= min(k, n - 2):
                s[0], s[first_one] = s[first_one], s[0]

        ans = 10 * int(s[0])
        for i in range(1, n - 1):
            ans += 11 * int(s[i])
        ans += int(s[n - 1])
        print_(f"{ans}\n")


if __name__ == '__main__':
    solve()
