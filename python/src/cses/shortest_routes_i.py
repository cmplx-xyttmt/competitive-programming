import heapq
from typing import List, Tuple

if __name__ == '__main__':
    n, m = map(int, input().split())
    adj: List[List[Tuple[int, int]]] = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        adj[a].append((b, c))
    pq = []
    ans = [-1 for _ in range(n + 1)]
    heapq.heappush(pq, (0, 1))

    while pq:
        dist, city = heapq.heappop(pq)
        if ans[city] != -1:
            continue
        ans[city] = dist
        for neighbor, length in adj[city]:
            if ans[neighbor] == -1:
                heapq.heappush(pq, (dist + length, neighbor))

    print(" ".join(map(str, ans[1:])))
