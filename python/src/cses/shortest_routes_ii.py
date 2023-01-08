from typing import Tuple, List
import sys

input = sys.stdin.readline
print = sys.stdout.write

if __name__ == '__main__':
    n, m, q = map(int, input().split())
    adj: List[List[Tuple[int, int]]] = [[] for _ in range(n + 1)]
    distances = [[float('INF') for _ in range(n + 1)] for _ in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        distances[a][b] = min(distances[a][b], c)
        distances[b][a] = min(distances[b][a], c)
        adj[a].append((b, c))
        adj[b].append((a, c))

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])

    ans = []
    for _ in range(q):
        a, b = map(int, input().split())
        if distances[a][b] == float('INF'):
            ans.append(-1)
        else:
            ans.append(distances[a][b])

    print("\n".join(map(str, ans)))
