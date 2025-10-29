from collections import defaultdict, deque
from typing import List
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
    adj = defaultdict(list)
    for _ in range(m):
        a, b = read_ints()
        adj[a].append(b)
        adj[b].append(a)
    queue = deque()
    queue.append(1)
    prev = [None for _ in range(n + 1)]
    path = []
    while queue:
        node = queue.popleft()
        for neighbor in adj[node]:
            if not prev[neighbor] and neighbor != 1:
                queue.append(neighbor)
                prev[neighbor] = node
                if neighbor == n:
                    u = neighbor
                    while u:
                        path.append(str(u))
                        u = prev[u]
                    break
        if path:
            break
    if not path:
        print_("IMPOSSIBLE\n")
    else:
        print_(f"{len(path)}\n")
        print_(f"{' '.join(reversed(path))}\n")


if __name__ == '__main__':
    solve()
