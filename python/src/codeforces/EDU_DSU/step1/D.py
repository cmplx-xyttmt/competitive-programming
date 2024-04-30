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


class DSU:

    def __init__(self, size: int):
        self.parents = [i for i in range(size + 1)]
        self.size = [1 for _ in range(size + 1)]

    def get_parent(self, node: int):
        path = []
        while node != self.parents[node]:
            path.append(node)
            node = self.parents[node]

        parent = node
        for node in path:
            self.parents[node] = parent
        return parent

    def union(self, first: int, second: int):
        first, second = self.get_parent(first), self.get_parent(second)
        if first == second:
            return
        if self.size[first] > self.size[second]:
            first, second = second, first

        self.parents[first] = second
        self.size[second] += self.size[first]

    def get_size(self, node: int):
        return self.size[self.get_parent(node)]


def solve():
    n, m, k = read_ints()
    for _ in range(m):
        read_ints()

    queries = []
    for _ in range(k):
        query, u, v = read_strings()
        u, v = map(int, [u, v])
        queries.append((query, u, v))

    dsu = DSU(n)
    ans = []
    for query, u, v in queries[::-1]:
        if query == 'ask':
            ans.append('YES' if dsu.get_parent(u) == dsu.get_parent(v) else "NO")
        else:
            dsu.union(u, v)

    ans_string = '\n'.join(ans[::-1])
    print_(f"{ans_string}\n")


if __name__ == '__main__':
    solve()
