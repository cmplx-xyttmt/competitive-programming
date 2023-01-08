from collections import defaultdict
from typing import List, Set
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
    adj = [[] for _ in range(n + 1)]
    edge_colors = dict()  # (a, b) -> c

    edges = []
    for _ in range(n - 1):
        a, b = read_ints()
        edges.append((a, b))
        adj[a].append(b)
        adj[b].append(a)

    nodes_seen: List[Set[int]] = [set() for _ in range(n + 1)]
    max_color = 1
    for u in range(n + 1):
        seen_u = nodes_seen[u]
        least_unseen = 1
        for v in adj[u]:
            if u > v:
                continue
            seen_v = nodes_seen[v]
            while least_unseen in seen_u or least_unseen in seen_v:
                least_unseen += 1
            max_color = max(max_color, least_unseen)
            edge_colors[(u, v)] = least_unseen
            seen_u.add(least_unseen)
            seen_v.add(least_unseen)

    ans = []
    for u, v in edges:
        ans.append(edge_colors[(u, v)])
    ans_str = '\n'.join(map(str, ans))
    print_(f"{max_color}\n{ans_str}\n")


if __name__ == '__main__':
    solve()
