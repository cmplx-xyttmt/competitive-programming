"""
ID: archime5
LANG: PYTHON3
TASK: cowtour
"""
import math
import sys
from collections import deque
from typing import Callable, List

sys.stdin = open('cowtour.in', 'r')
sys.stdout = open('cowtour.out', 'w')

_input: Callable[[], str] = sys.stdin.readline
_print: Callable[[str], int] = sys.stdout.write


def distance(p1, p2):
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]
    return math.sqrt(dx ** 2 + dy ** 2)


if __name__ == '__main__':
    n = int(_input())
    # component, coordinates, adj, distances
    coordinates = []
    for _ in range(n):
        x, y = map(int, _input().split())
        coordinates.append((x, y))

    component = [-1 for _ in range(n)]
    distances = [[float('inf') for _ in range(n)] for _ in range(n)]
    adj: List[str] = []
    for i in range(n):
        adj.append(_input())
        for j in range(n):
            if i == j:
                distances[i][j] = 0
            elif adj[i][j] == '1':
                distances[i][j] = distance(coordinates[i], coordinates[j])

    for k in range(n):
        for i in range(n):
            for j in range(n):
                distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])
    max_dists = [0.0 for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if distances[i][j] != float('inf'):
                max_dists[i] = max(max_dists[i], distances[i][j])
    comp = 0
    for i in range(n):
        if component[i] == -1:
            q = deque()
            q.append((i, comp))
            component[i] = comp
            while q:
                p, c = q.popleft()
                for j in range(n):
                    if adj[p][j] == '1' and component[j] == -1:
                        component[j] = comp
                        q.append((j, comp))
            comp += 1
    # print(distances)
    ans = float('inf')
    for i in range(n):
        for j in range(n):
            if component[i] != component[j]:
                ans = min(ans, max_dists[i] + distance(coordinates[i], coordinates[j]) + max_dists[j])

    _print(f"{ans:.6f}\n")
