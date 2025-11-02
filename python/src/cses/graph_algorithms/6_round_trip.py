from collections import defaultdict
from types import GeneratorType
from typing import List
import sys


def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to

    return wrappedfunc


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


def find_cycle(start, parent):
    cycle = [start]
    node = parent[start]
    while node != start:
        cycle.append(node)
        node = parent[node]
    cycle.append(start)
    return cycle


def solve():
    n, m = read_ints()
    adj = defaultdict(list)
    for _ in range(m):
        a, b = read_ints()
        adj[a].append(b)
        adj[b].append(a)
    cycle = []
    parent = [None for _ in range(n + 1)]
    visited = [False for _ in range(n + 1)]

    @bootstrap
    def dfs(u, prev_node):
        visited[u] = True
        # print(f"Exploring {u} from {prev_node}")
        # print("State: \n", "prev -> ", prev_node, "parent -> ", parent)
        # print(f"Neighbors: {adj[u]}")
        for neigh in adj[u]:
            # print(f"Neighbor of {u}: ", neigh)
            if neigh == prev_node:
                continue
            if visited[neigh]:
                # parent[neigh] = u
                # cycle.append(neigh)
                curr = u
                while curr != neigh:
                    cycle.append(curr)
                    curr = parent[curr]
                cycle.append(neigh)
                cycle.append(u)
                yield True
            else:
                parent[neigh] = u
                found_cycle = yield dfs(neigh, u)
                if found_cycle:
                    yield True
        yield False

    for node in range(1, n + 1):
        if not parent[node] and dfs(node, None):
            break

    if cycle:
        print(len(cycle))
        print(f"{' '.join(map(str, cycle))}")
    else:
        print("IMPOSSIBLE")


if __name__ == '__main__':
    solve()
