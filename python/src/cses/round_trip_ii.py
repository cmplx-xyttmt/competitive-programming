from typing import List
import sys

sys.setrecursionlimit(int(1e6))


def dfs(node):
    color[node] = 1
    for u in adj[node]:
        if color[u] == 1:
            return u, node
        elif color[u] == 0:
            prev[u] = node
            cycle = dfs(u)
            if cycle:
                return cycle
    color[node] = 2
    return None


if __name__ == '__main__':
    n, m = map(int, input().split())
    adj: List[List[int]] = [[] for _ in range(n + 1)]
    prev = [0 for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        adj[a].append(b)

    cycle_start, cycle_end = -1, -1
    color = [0 for _ in range(n + 1)]
    for i in range(1, n + 1):
        if color[i] == 0:
            _cycle = dfs(i)
            if _cycle:
                cycle_start, cycle_end = _cycle
                break

    if cycle_start == -1:
        print("IMPOSSIBLE")
    else:
        ans = []
        v = cycle_end
        ans.append(cycle_start)
        while v != cycle_start:
            ans.append(v)
            v = prev[v]
        ans.append(cycle_start)
        print(len(ans))
        print(" ".join(map(str, reversed(ans))))
