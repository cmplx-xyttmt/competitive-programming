from typing import List
import sys

# https://atcoder.jp/contests/dp/tasks/dp_g
input_ = sys.stdin.readline
print_ = sys.stdout.write
flush = sys.stdout.flush

sys.setrecursionlimit(200000)


def read_line() -> str:
    return input_().strip()


def read_int() -> int:
    return int(read_line())


def read_strings() -> List[str]:
    return list(read_line().split())


def read_ints():
    return list(map(int, read_line().split()))


def solve():
    n, m = read_ints()
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        x, y = read_ints()
        adj[x].append(y)

    longest = [0 for _ in range(n + 1)]

    def get_longest(node):
        if longest[node]:
            return longest[node]
        for nxt in adj[node]:
            longest[node] = max(longest[node], 1 + get_longest(nxt))
        return longest[node]

    ans = 0
    for node in range(1, n + 1):
        ans = max(ans, get_longest(node))
    print(ans)


if __name__ == '__main__':
    solve()
