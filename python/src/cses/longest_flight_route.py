from typing import List
import sys


sys.setrecursionlimit(int(1e6))


def longest_path(u):
    seen[u] = True
    # print(u)
    for v in adj[u]:
        dist = dists[v] if seen[v] else longest_path(v)
        if dist == -1:
            continue
        if dist + 1 > dists[u]:
            dists[u] = dist + 1
            nxt[u] = v
    return dists[u]


if __name__ == '__main__':
    n, m = map(int, input().split())
    # edge_list: List[Tuple[int, int]] = []
    adj: List[List[int]] = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        # edge_list.append((a, b))
        adj[a].append(b)

    dists = [-1 for _ in range(n + 1)]
    seen = [False for _ in range(n + 1)]
    dists[n] = 0
    nxt = [0 for _ in range(n + 1)]
    p = longest_path(1)
    if p == -1:
        print("IMPOSSIBLE")
    else:
        path = []
        u = 1
        while u != n:
            path.append(u)
            u = nxt[u]
        path.append(u)
        print(len(path))
        print(" ".join(map(str, path)))
