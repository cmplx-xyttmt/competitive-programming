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
        n, q = read_ints()
        s = read_line()
        pref = [[0] * (n + 1) for _ in range(26)]
        for i in range(1, n + 1):
            ch = ord(s[i - 1]) - ord('A')
            for c in range(26):
                pref[c][i] = pref[c][i - 1]
                if c == ch:
                    pref[c][i] += 1

        yeses = 0
        for _ in range(q):
            l, r = read_ints()
            range_even = (r - l + 1) % 2 == 0
            evens, odds = 0, 0
            for c in range(26):
                if (pref[c][r] - pref[c][l - 1]) % 2 == 0:
                    evens += 1
                else:
                    odds += 1
            if range_even:
                yeses += (0 if odds else 1)
            else:
                yeses += (1 if odds == 1 else 0)
        print_(f"Case #{test}: {yeses}\n")


if __name__ == '__main__':
    solve()
