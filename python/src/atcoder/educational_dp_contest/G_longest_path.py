from typing import List
import sys
from collections import deque

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
    indegree = [0] * (n + 1)
    for _ in range(m):
        x, y = read_ints()
        adj[x].append(y)
        indegree[y] += 1

    longest = [0 for _ in range(n + 1)]

    queue = deque(i for i in range(1, n + 1) if indegree[i] == 0)
    while queue:
        node = queue.popleft()
        for nxt in adj[node]:
            longest[nxt] = max(longest[nxt], 1 + longest[node])
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                queue.append(nxt)
    print(max(longest))


if __name__ == '__main__':
    solve()
