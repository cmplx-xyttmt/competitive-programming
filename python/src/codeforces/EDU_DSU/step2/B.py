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


def get_parent(slot, parent):
    path = []

    while slot != parent[slot]:
        path.append(slot)
        slot = parent[slot]

    for p in path:
        parent[p] = slot

    return slot


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

        self.parents[first] = second
        self.size[second] += self.size[first]

    def get_size(self, node: int):
        return self.size[self.get_parent(node)]


def solve():
    n = read_int()

    p = read_ints()
    dsu_parking = DSU(n)
    actual_parking = []
    for i, parking_slot in enumerate(p):
        free_slot = dsu_parking.get_parent(parking_slot)
        actual_parking.append(free_slot)
        dsu_parking.union(free_slot, free_slot % n + 1)
    print_(f"{' '.join(map(str, actual_parking))}\n")


if __name__ == '__main__':
    solve()
