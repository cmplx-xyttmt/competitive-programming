from typing import Tuple, List


if __name__ == '__main__':
    n, m = map(int, input().split())
    adj: List[List[Tuple[int, int]]] = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        adj[a].append((b, c))

    dist = [int(1e18) for _ in range(n + 1)]
    prev = [0 for _ in range(n + 1)]
    dist[1] = 0
    x = -1
    for rep in range(0, n):
        x = -1
        for u in range(1, n + 1):
            for v, w in adj[u]:
                if dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w
                    prev[v] = u
                    x = v

    if x == -1:
        print("NO")
    else:
        for _ in range(n):
            x = prev[x]
        ans = []
        seen = set()
        while x not in seen:
            seen.add(x)
            ans.append(x)
            x = prev[x]
        ans.append(x)

        print("YES")
        print(" ".join(map(str, reversed(ans))))
