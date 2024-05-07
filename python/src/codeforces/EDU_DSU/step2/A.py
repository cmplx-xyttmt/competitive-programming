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
        if first > second:
            first, second = second, first

        self.parents[first] = second
        self.size[second] += self.size[first]

    def get_size(self, node: int):
        return self.size[self.get_parent(node)]


def solve():
    n, m = read_ints()
    dsu = DSU(n + 1)
    for _ in range(m):
        query, num = read_strings()
        num = int(num)
        if query == "?":
            nxt = dsu.get_parent(num)
            nxt = -1 if nxt > n else nxt
            print_(f"{nxt}\n")
        else:
            if num > 1 and dsu.get_parent(num - 1) != num - 1:
                dsu.union(num - 1, num + 1)
            dsu.union(num, num + 1)


if __name__ == '__main__':
    solve()
