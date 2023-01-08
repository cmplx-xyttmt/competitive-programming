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


def get_parent(a, parent):
    parents_on_path = []
    while a != parent[a]:
        parents_on_path.append(a)
        a = parent[a]
    p = a
    for a in parents_on_path:
        parent[a] = p
    return p


def union(a, b, parent, size):
    a, b = get_parent(a, parent), get_parent(b, parent)

    if size[a] > size[b]:
        a, b = b, a

    parent[a] = b
    size[b] += size[a]


def solve():
    n, m, k = read_ints()
    for _ in range(m):
        read_ints()

    queries = []
    for _ in range(k):
        query, u, v = read_strings()
        u, v = map(int, [u, v])
        queries.append((query, u, v))

    size = [1 for _ in range(n + 1)]
    parent = [i for i in range(n + 1)]
    ans = []
    for query, u, v in queries[::-1]:
        if query == 'ask':
            ans.append('YES' if get_parent(u, parent) == get_parent(v, parent) else "NO")
        else:
            union(u, v, parent, size)

    ans_string = '\n'.join(ans[::-1])
    print_(f"{ans_string}\n")


if __name__ == '__main__':
    solve()
