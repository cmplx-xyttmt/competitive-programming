from collections import deque
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


def bfs(node, adj, seen):
    q = deque()
    q.append(node)
    seen[node] = True
    edges = 0
    nodes = 0
    while q:
        u = q.popleft()
        nodes += 1
        edges += len(adj[u])
        for v in adj[u]:
            if not seen[v]:
                q.append(v)
                seen[v] = True

    return 1 if edges // 2 == nodes - 1 else 0


def solve():
    n, m = read_ints()
    adj: List[List[int]] = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = read_ints()
        adj[u].append(v)
        adj[v].append(u)

    ans = 0
    seen = [False for _ in range(n + 1)]
    for i in range(1, n + 1):
        if not seen[i]:
            ans += bfs(i, adj, seen)

    print_(f"{ans}\n")


if __name__ == '__main__':
    solve()
