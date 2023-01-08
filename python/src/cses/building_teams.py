from typing import List
from collections import deque


def bfs(pupil):
    q = deque()
    teams[pupil] = 1
    q.append(pupil)
    can = True
    while q:
        p = q.popleft()
        color = teams[p]
        for neighbor in adj[p]:
            if teams[neighbor] == 0:
                teams[neighbor] = color % 2 + 1
                q.append(neighbor)
            elif teams[neighbor] == color:
                can = False
                break
        if not can:
            break
    return can


if __name__ == '__main__':
    n, m = map(int, input().split())
    adj: List[List[int]] = [[] for _ in range(n + 1)]
    teams = [0 for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)
    cn = True
    for i in range(1, n + 1):
        if teams[i] == 0:
            cn = bfs(i)
            if not cn:
                break
    if not cn:
        print("IMPOSSIBLE")
    else:
        print(" ".join(map(str, teams[1:])))
