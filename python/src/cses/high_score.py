from collections import deque
from typing import List


def bfs(node, adj, visited):
    q = deque()
    q.append(node)
    visited[node] = True
    while q:
        node = q.popleft()
        for neighbor in adj[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                q.append(neighbor)


if __name__ == '__main__':
    n, m = map(int, input().split())
    edges = []
    scores = [-int(1e18) for _ in range(n + 1)]
    seen = [False for _ in range(n + 1)]
    reverse_graph: List[List[int]] = [[] for _ in range(n + 1)]
    graph: List[List[int]] = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        edges.append((a, b, c))
        reverse_graph[b].append(a)
        graph[a].append(b)
    visited_n = [False for _ in range(n + 1)]
    visited_1 = [False for _ in range(n + 1)]

    bfs(n, reverse_graph, visited_n)
    bfs(1, graph, visited_1)

    arbit = False
    scores[1] = 0
    for i in range(1, n + 1):
        increase = False
        for a, b, c in edges:
            prev = scores[b]
            scores[b] = max(scores[b], scores[a] + c)
            if scores[b] > prev and visited_n[b] and visited_1[b]:
                increase = True
        arbit = increase and i == n

    # print(scores)
    if arbit:
        print(-1)
    else:
        print(scores[n])
