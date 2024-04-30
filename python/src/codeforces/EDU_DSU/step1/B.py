from types import GeneratorType
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
        self.minimum = [i for i in range(size + 1)]
        self.maximum = [i for i in range(size + 1)]

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
        self.minimum[second] = min(self.minimum[first], self.minimum[second])
        self.maximum[second] = max(self.maximum[first], self.maximum[second])

    def get_size(self, node: int):
        return self.size[self.get_parent(node)]

    def get_minimum(self, node: int):
        return self.minimum[self.get_parent(node)]

    def get_maximum(self, node: int):
        return self.maximum[self.get_parent(node)]


def solve():
    n, m = read_ints()
    dsu = DSU(n)
    for _ in range(m):
        line = read_strings()
        op = line[0]
        if op == 'union':
            a, b = map(int, line[1:])
            dsu.union(a, b)
        else:
            a = int(line[1])
            minimum, maximum, size = dsu.get_minimum(a), dsu.get_maximum(a), dsu.get_size(a)
            print_(f"{minimum} {maximum} {size}\n")


if __name__ == '__main__':
    solve()
