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
    n, q = read_ints()
    adj = defaultdict(list)
    for _ in range(n - 1):
        a, b = read_ints()
        adj[a].append(b)
        adj[b].append(a)

    to_add = [0] * (n + 1)
    for _ in range(q):
        p, x = read_ints()
        to_add[p] += x

    q = deque()
    q.append((1, -1))
    final_values = [0] * (n + 1)
    while q:
        node, prev_node = q.popleft()
        final_values[node] = to_add[node]
        for nxt_node in adj[node]:
            if nxt_node != prev_node:
                to_add[nxt_node] += to_add[node]
                q.append((nxt_node, node))

    ans = " ".join(map(str, final_values[1:]))
    print_(f"{ans}\n")


if __name__ == '__main__':
    solve()
