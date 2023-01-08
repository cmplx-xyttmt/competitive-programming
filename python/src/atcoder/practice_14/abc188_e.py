from typing import List
import sys

sys.setrecursionlimit(int(2e5))
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
    n, m = read_ints()
    a = [0] + read_ints()
    adj: List[List[int]] = [[] for _ in range(n + 1)]

    for _ in range(m):
        x, y = read_ints()
        adj[x].append(y)

    inf = -int(1e9)
    maxs = [inf] * (n + 1)

    def get_max(node):
        mx = inf
        for nxt in adj[node]:
            mx = max(a[nxt], mx)
            if maxs[nxt] == inf:
                mx = max(mx, get_max(nxt))
            else:
                mx = max(mx, maxs[nxt])
        maxs[node] = mx
        return mx

    ans = inf
    for i in range(1, n + 1):
        if maxs[i] == inf:
            ans = max(ans, get_max(i) - a[i])
        else:
            ans = max(ans, maxs[i] - a[i])
    print_(f"{ans}\n")


if __name__ == '__main__':
    solve()
