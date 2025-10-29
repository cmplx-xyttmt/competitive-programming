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
    component = [-1 for _ in range(n + 1)]
    curr_comp = 0
    parents = []
    for node in range(1, n + 1):
        if component[node] != -1:
            continue
        parents.append(node)
        curr_comp += 1
        component[node] = curr_comp
        queue = deque()
        queue.append(node)
        while queue:
            node = queue.popleft()
            for neighbor in adj[node]:
                if component[neighbor] == -1:
                    component[neighbor] = curr_comp
                    queue.append(neighbor)
    roads = []
    for i in range(1, len(parents)):
        roads.append(f"{parents[i]} {parents[i - 1]}")
    print_(f"{len(roads)}\n")
    for road in roads:
        print_(f"{road}\n")


if __name__ == '__main__':
    solve()
