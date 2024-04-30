import copy
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
        self.time_to_join = [-1 for _ in range(size + 1)]
        self.time_to_join[1] = 0

    def get_parent(self, node: int):
        path = []
        while node != self.parents[node]:
            path.append(node)
            node = self.parents[node]

        parent = node
        return parent

    def get_time(self, node: int):
        while node != self.parents[node]:
            prev_node = node
            node = self.parents[node]
            if node == 1:
                return self.time_to_join[prev_node]
        return -1

    def union(self, first: int, second: int, time: int):
        first, second = self.get_parent(first), self.get_parent(second)
        if first == second:
            return
        if first == 1 or (self.size[first] > self.size[second] and second != 1):
            first, second = second, first

        self.parents[first] = second
        self.size[second] += self.size[first]
        if second == 1:
            self.time_to_join[first] = time

    def get_size(self, node: int):
        return self.size[self.get_parent(node)]


def solve():
    # go in reverse order
    #   - in order to do this, we need to determine config at the end
    #   - after that, calculate the time t at which each monkey joins the leaders' connected component.
    #          - go in reverse order of drops
    #          - avoid path compression, so answer can be time of node just before they join parent.
    #                - or do path compression only if the parent is the leader
    #   - final answer is m - t
    n, m = read_ints()
    hands = [[0, 0]] + [read_ints() for _ in range(n)]
    hands_at_end = copy.deepcopy(hands)
    drops = [read_ints() for _ in range(m)]
    for monkey, hand in drops:
        hands_at_end[monkey][hand - 1] = -1
    dsu = DSU(n)
    for i, (left, right) in enumerate(hands_at_end):
        if left >= 1:
            dsu.union(i, left, -1)
        if right >= 1:
            dsu.union(i, right, -1)

    total_time = 0
    drops.reverse()
    for monkey, hand in drops:
        next_monkey = hands[monkey][hand - 1]
        if next_monkey != -1:
            dsu.union(monkey, next_monkey, total_time)
        total_time += 1

    times = [dsu.get_time(monkey) for monkey in range(n + 1)]
    time_for_fall = []
    for time in times:
        if time >= 0:
            time_for_fall.append(total_time - time - 1)
        else:
            time_for_fall.append(time)
    ans = "\n".join(map(str, time_for_fall[1:]))
    print_(f"{ans}\n")


if __name__ == '__main__':
    solve()
