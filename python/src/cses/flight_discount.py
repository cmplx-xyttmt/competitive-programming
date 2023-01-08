from typing import List, Tuple
import heapq

import sys

input = sys.stdin.readline
print = sys.stdout.write


def shortest_path(start, graph, distances):
    pq = []
    heapq.heappush(pq, (0, start))

    while pq:
        dist, city = heapq.heappop(pq)
        if distances[city] != -1:
            continue
        distances[city] = dist
        for next_city, length in graph[city]:
            if distances[next_city] == -1:
                heapq.heappush(pq, (length + dist, next_city))


if __name__ == '__main__':
    n, m = map(int, input().split())
    adj: List[List[Tuple[int, int]]] = [[] for _ in range(n + 1)]
    reverse_adj: List[List[Tuple[int, int]]] = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        adj[a].append((b, c))
        reverse_adj[b].append((a, c))

    from_1 = [-1 for _ in range(n + 1)]
    from_n = [-1 for _ in range(n + 1)]

    shortest_path(1, adj, from_1)
    shortest_path(n, reverse_adj, from_n)
    # print(from_1)
    # print(from_n)
    ans = int(1e18)
    for _city in range(1, n + 1):
        for _next_city, _length in adj[_city]:
            if from_1[_city] != -1 and from_n[_next_city] != -1:
                ans = min(ans, from_1[_city] + from_n[_next_city] + _length // 2)

    print(str(ans))
