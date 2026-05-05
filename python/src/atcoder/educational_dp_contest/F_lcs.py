from typing import List
import sys

input_ = sys.stdin.readline
print_ = sys.stdout.write
flush = sys.stdout.flush


# https://atcoder.jp/contests/dp/tasks/dp_f

def read_line() -> str:
    return input_().strip()


def read_int() -> int:
    return int(read_line())


def read_strings() -> List[str]:
    return list(read_line().split())


def read_ints():
    return list(map(int, read_line().split()))


def solve():
    s = read_line()
    t = read_line()

    # dp[i][j] = lcs s[0:i] and t[0:j]
    # dp[i][j] = max((1 if s[i] == t[j] else 0) + dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j])
    prev = [0] * (len(t) + 1)
    index = [[(0, 0)] * (len(t) + 1) for _ in range(len(s) + 1)]
    for i in range(1, len(s) + 1):
        curr = list(prev)
        for j in range(1, len(t) + 1):
            if curr[j - 1] >= prev[j]:
                index[i][j] = index[i][j - 1]
            else:
                index[i][j] = index[i - 1][j]
            curr[j] = max(curr[j - 1], prev[j])
            curr_max = curr[j]
            prev_max = prev[j - 1]
            if s[i - 1] == t[j - 1]:
                if 1 + prev_max >= curr_max:
                    curr[j] = 1 + prev_max
                    index[i][j] = (i, j)

        prev = curr
    r, c = index[-1][-1]
    ans = []
    while r > 0 or c > 0:
        nxt_r, nxt_c = index[r][c]
        if nxt_r == r and nxt_c == c:
            ans.append(s[r - 1])
            r, c = r - 1, c - 1
        else:
            r, c = nxt_r, nxt_c
    print("".join(reversed(ans)))


if __name__ == '__main__':
    solve()
