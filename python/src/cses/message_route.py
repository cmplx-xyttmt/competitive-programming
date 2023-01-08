from typing import List
from collections import deque


if __name__ == '__main__':
    n, m = map(int, input().split())
    adj: List[List[int]] = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)
    prev = [-1 for _ in range(n + 1)]
    prev[1] = 1

    q = deque()
    q.append(1)

    while q:
        comp = q.popleft()
        if comp == n:
            break
        for neighbor in adj[comp]:
            if prev[neighbor] == -1:
                prev[neighbor] = comp
                q.append(neighbor)
    if prev[n] == -1:
        print("IMPOSSIBLE")
    else:
        x = n
        path = [str(x)]
        while x != 1:
            path.append(str(prev[x]))
            x = prev[x]
        print(len(path))
        print(" ".join(reversed(path)))
