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
        s = read_line()
        n = len(s)
        l_to_r = [False] * n
        l_to_r[0] = s[0] == '1' or s[0] == '?'  # seen only 1s or ?s
        for i in range(1, n):
            l_to_r[i] = (s[i] == '1' or s[i] == '?') and l_to_r[i - 1]
        r_to_l = [False] * n
        r_to_l[n - 1] = s[n - 1] == '0' or s[n - 1] == '?'  # seen only 0s or ?s
        for i in range(n - 2, -1, -1):
            r_to_l[i] = (s[i] == '0' or s[i] == '?') and r_to_l[i + 1]

        # print(l_to_r, r_to_l)
        thieves = 0
        for i in range(n):
            left = True if i == 0 else l_to_r[i - 1]
            right = True if i == n - 1 else r_to_l[i + 1]
            if left and right:
                thieves += 1
        print_(f"{thieves}\n")


if __name__ == '__main__':
    solve()
