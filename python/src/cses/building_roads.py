from collections import deque
from typing import List


def bfs(city):
    seen[city] = True
    q = deque()
    q.append(city)
    while q:
        city = q.popleft()
        for neighbor in adj_graph[city]:
            if not seen[neighbor]:
                seen[neighbor] = True
                q.append(neighbor)


if __name__ == '__main__':
    n, m = map(int, input().split())
    adj_graph: List[List[int]] = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        adj_graph[a].append(b)
        adj_graph[b].append(a)
    seen = [False for _ in range(n + 1)]
    to_connect = -1
    new_roads = []
    for i in range(1, n + 1):
        if not seen[i]:
            if to_connect != -1:
                new_roads.append((to_connect, i))
            to_connect = i
            bfs(i)
    print(len(new_roads))
    for road in new_roads:
        print(road[0], road[1])
