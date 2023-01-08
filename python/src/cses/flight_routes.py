import heapq
from typing import Tuple, List

if __name__ == '__main__':
    n, m, k = map(int, input().split())
    adj: List[List[Tuple[int, int]]] = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b, c = map(int, input().split())
        adj[a].append((b, c))

    pq = []
    heapq.heappush(pq, (0, 1))
    seen_times = [0 for _ in range(n + 1)]
    ans = []
    while pq:
        dist, node = heapq.heappop(pq)
        if seen_times[node] == k:
            continue
        if node == n:
            ans.append(dist)
        seen_times[node] += 1
        if node == n and seen_times[node] == k:
            break
        for v, w in adj[node]:
            if seen_times[v] < k:
                heapq.heappush(pq, (w + dist, v))
    print(" ".join(map(str, ans)))
