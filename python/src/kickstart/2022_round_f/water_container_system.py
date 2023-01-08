from typing import List
import sys
from collections import deque

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
    t = read_int()
    for test in range(1, t + 1):
        n, queries = read_ints()
        adj = [[] for _ in range(n + 1)]
        for _ in range(n - 1):
            i, j = read_ints()
            adj[i].append(j)
            adj[j].append(i)

        levels = []
        q = deque()
        q.append((0, 1))  # level, container
        seen = set()
        while q:
            level, container = q.popleft()
            seen.add(container)
            if len(levels) == level:
                levels.append(1)
            else:
                levels[level] += 1
            for nxt in adj[container]:
                if nxt not in seen:
                    q.append((level + 1, nxt))

        litres = queries
        for _ in range(queries):
            read_int()

        ans = 0
        for i in range(len(levels)):
            num_containers = levels[i]
            if litres >= num_containers:
                ans += num_containers
                litres -= num_containers
            else:
                break

        print_(f"Case #{test}: {ans}\n")


if __name__ == '__main__':
    solve()
