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
    edges = []
    for _ in range(m):
        u, v = read_ints()
        edges.append((u - 1, v - 1))

    min_edges = m + 1
    for coloring in range(2 ** n):
        edges_to_delete = 0
        for u, v in edges:
            # if the connected edges are the same color
            color_u = int(((1 << u) & coloring) > 0)
            color_v = int(((1 << v) & coloring) > 0)
            if color_u == color_v:
                edges_to_delete += 1
        min_edges = min(min_edges, edges_to_delete)

    print(min_edges)


if __name__ == '__main__':
    solve()
