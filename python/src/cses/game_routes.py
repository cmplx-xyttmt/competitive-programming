from typing import List
import sys

sys.setrecursionlimit(int(1e6))
MOD = int(1e9) + 7


def dfs(u):
    seen[u] = True
    ways = 0
    for v in adj[u]:
        if seen[v]:
            ways = (ways + cache[v]) % MOD
        else:
            ways = (ways + dfs(v)) % MOD
    cache[u] = ways
    return ways


if __name__ == '__main__':
    n, m = map(int, input().split())
    adj: List[List[int]] = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        adj[a].append(b)

    seen = [False for _ in range(n + 1)]
    cache = [0 for _ in range(n + 1)]
    cache[n] = 1
    seen[n] = True
    print(dfs(1))
