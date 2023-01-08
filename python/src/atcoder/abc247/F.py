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
    path = []
    while a != parent[a]:
        path.append(a)
        a = parent[a]
    for node in path:
        parent[node] = a
    return a


def union(a, b, parent, size):
    a, b = get_parent(a, parent), get_parent(b, parent)
    if a == b:
        return
    if size[a] > size[b]:
        a, b = b, a

    size[b] += size[a]
    parent[a] = b


def solve():
    n = read_int()
    p = read_ints()
    q = read_ints()

    size = [1 for _ in range(n + 1)]
    parent = [i for i in range(n + 1)]

    for i in range(n):
        union(p[i], q[i], parent, size)

    parents = set()
    for i in range(1, n +1 ):
        parents.add(get_parent(i, parent))

    f = [0, 1, 3]
    g1 = [0, 2, 3]
    mod = 998244353
    for i in range(3, n + 1):
        f.append((f[i - 1] + f[i - 2]) % mod)
        g1.append((g1[i - 1] + g1[i - 2]) % mod)

    g = [0, 1, 3, 4]
    for i in range(4, n + 1):
        g.append((g1[i - 1] + g1[i - 3]) % mod)
    print(f"f = {f}")
    print(f"g = {g}")
    ans = 1
    ans_g = 1

    for p in parents:
        print(size[p])
        ans = (ans * f[size[p]]) % mod
        ans_g = (ans_g * g[size[p]]) % mod

    print_(f"{ans} vs {ans_g}\n")


if __name__ == '__main__':
    solve()
