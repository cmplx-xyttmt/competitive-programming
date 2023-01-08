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
    n, m = read_ints()
    adj: List[List[Tuple[int, int]]] = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v, w = read_ints()
        adj[u].append((v, w))
        adj[v].append((u, w))

    num = [-1 for _ in range(n + 1)]
    seen = set()

    def dfs(node, weight):
        num[node] = weight
        seen.add(node)
        for nxt, w in adj[node]:
            if nxt not in seen:
                dfs(nxt, w)


if __name__ == '__main__':
    solve()
