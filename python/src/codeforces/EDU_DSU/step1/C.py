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
        self.points = [0 for _ in range(size + 1)]

    def get_parent(self, node: int):
        path = []
        while node != self.parents[node]:
            path.append(node)
            node = self.parents[node]

        parent = node
        # no path compression for this problem
        return parent

    def union(self, first: int, second: int):
        first, second = self.get_parent(first), self.get_parent(second)
        if first == second:
            return
        if self.size[first] > self.size[second]:
            first, second = second, first

        self.parents[first] = second
        self.size[second] += self.size[first]
        self.points[first] -= self.points[second]

    def get_size(self, node: int):
        return self.size[self.get_parent(node)]

    def get_points(self, node: int):
        points = self.points[node]
        while node != self.parents[node]:
            node = self.parents[node]
            points += self.points[node]
        return points

    def add_points(self, node: int, points: int):
        parent = self.get_parent(node)
        self.points[parent] += points


def solve():
    n, m = read_ints()
    dsu = DSU(n)
    for _ in range(m):
        line = read_strings()
        op = line[0]
        if op == 'add':
            a, score = map(int, line[1:])
            dsu.add_points(a, score)
        elif op == 'join':
            a, b = map(int, line[1:])
            dsu.union(a, b)
        else:
            a = int(line[1])
            print_(f"{dsu.get_points(a)}\n")


if __name__ == '__main__':
    solve()
