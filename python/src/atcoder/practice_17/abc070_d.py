from collections import deque
from typing import List, Tuple
import sys

input_ = sys.stdin.readline
print_ = sys.stdout.write
flush = sys.stdout.flush


def read_line() -> str:
    return input_().strip()


def read_int() -> int:
    return int(read_line())


def read_strings() -> List[str]:
    return list(read_line().split())


def read_ints():
    return list(map(int, read_line().split()))


def solve():
    n = read_int()
    adj: List[List[Tuple]] = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a, b, c = read_ints()
        adj[a].append((b, c))
        adj[b].append((a, c))

    dists = [-1] * (n + 1)
    q, k = read_ints()
    queue = deque()
    queue.append((k, 0))
    dists[k] = 0
    while queue:
        node, dist = queue.popleft()
        for neighbor, length in adj[node]:
            if dists[neighbor] == -1:
                dists[neighbor] = dist + length
                queue.append((neighbor, dist + length))
    for _ in range(q):
        x, y = read_ints()
        print_(f"{dists[x] + dists[y]}\n")


if __name__ == '__main__':
    solve()
