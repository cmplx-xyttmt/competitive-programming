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


"""
The "sorted list" data-structure, with amortized O(n^(1/3)) cost per insert and pop.

Example:

A = SortedList()
A.insert(30)
A.insert(50)
A.insert(20)
A.insert(30)
A.insert(30)

print(A) # prints [20, 30, 30, 30, 50]

print(A.lower_bound(30), A.upper_bound(30)) # prints 1 4

print(A[-1]) # prints 50
print(A.pop(1)) # prints 30

print(A) # prints [20, 30, 30, 50]
print(A.count(30)) # prints 2

"""

from bisect import bisect_left as lower_bound
from bisect import bisect_right as upper_bound


class FenwickTree:
    def __init__(self, x):
        bit = self.bit = list(x)
        size = self.size = len(bit)
        for i in range(size):
            j = i | (i + 1)
            if j < size:
                bit[j] += bit[i]

    def update(self, idx, x):
        """updates bit[idx] += x"""
        while idx < self.size:
            self.bit[idx] += x
            idx |= idx + 1

    def __call__(self, end):
        """calc sum(bit[:end])"""
        x = 0
        while end:
            x += self.bit[end - 1]
            end &= end - 1
        return x

    def find_kth(self, k):
        """Find largest idx such that sum(bit[:idx]) <= k"""
        idx = -1
        for d in reversed(range(self.size.bit_length())):
            right_idx = idx + (1 << d)
            if right_idx < self.size and self.bit[right_idx] <= k:
                idx = right_idx
                k -= self.bit[idx]
        return idx + 1, k


class SortedList:
    block_size = 700

    def __init__(self, iterable=()):
        self.macro = []
        self.micros = [[]]
        self.micro_size = [0]
        self.fenwick = FenwickTree([0])
        self.size = 0
        for item in iterable:
            self.insert(item)

    def insert(self, x):
        i = lower_bound(self.macro, x)
        j = upper_bound(self.micros[i], x)
        self.micros[i].insert(j, x)
        self.size += 1
        self.micro_size[i] += 1
        self.fenwick.update(i, 1)
        if len(self.micros[i]) >= self.block_size:
            self.micros[i:i + 1] = self.micros[i][:self.block_size >> 1], self.micros[i][self.block_size >> 1:]
            self.micro_size[i:i + 1] = self.block_size >> 1, self.block_size >> 1
            self.fenwick = FenwickTree(self.micro_size)
            self.macro.insert(i, self.micros[i + 1][0])

    def pop(self, k=-1):
        i, j = self._find_kth(k)
        self.size -= 1
        self.micro_size[i] -= 1
        self.fenwick.update(i, -1)
        return self.micros[i].pop(j)

    def __getitem__(self, k):
        i, j = self._find_kth(k)
        return self.micros[i][j]

    def count(self, x):
        return self.upper_bound(x) - self.lower_bound(x)

    def __contains__(self, x):
        return self.count(x) > 0

    def lower_bound(self, x):
        i = lower_bound(self.macro, x)
        return self.fenwick(i) + lower_bound(self.micros[i], x)

    def upper_bound(self, x):
        i = upper_bound(self.macro, x)
        return self.fenwick(i) + upper_bound(self.micros[i], x)

    def _find_kth(self, k):
        return self.fenwick.find_kth(k + self.size if k < 0 else k)

    def __len__(self):
        return self.size

    def __iter__(self):
        return (x for micro in self.micros for x in micro)

    def __repr__(self):
        return str(list(self))


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


def type_1(x: int, y: int, dsu: DSU):
    dsu.union(x, y)


def type_2(x: int, y: int, dsu: DSU, sorted_list: SortedList):
    to_connect = []
    val_idx = sorted_list.lower_bound(x)
    val = sorted_list[val_idx]
    while val < y:
        to_connect.append(val)
        sorted_list.pop(val_idx)
        val_idx = sorted_list.lower_bound(x)
        val = sorted_list[val_idx]

    for val in to_connect:
        dsu.union(val, val + 1)


def type_3(x: int, y: int, dsu: DSU):
    return "YES" if dsu.get_parent(x) == dsu.get_parent(y) else "NO"


def solve():
    # Solution:
    # - maintain a TreeSet of values
    # - for type 2 queries (x, y), find values in [x, y) in the TreeSet, connect them and delete them from the set.
    #     # why delete?: they're now part of another department, no need to worry about them anymore
    # - for type 1 queries, connect x and y
    n, q = read_ints()
    dsu = DSU(n + 1)
    sorted_list = SortedList()
    for i in range(1, n + 1):
        sorted_list.insert(i)
    sorted_list.insert(1 << 30)
    for _ in range(q):
        type_, x, y = read_ints()
        if type_ == 1:
            type_1(x, y, dsu)
        elif type_ == 2:
            type_2(x, y, dsu, sorted_list)
        else:
            print_(f"{type_3(x, y, dsu)}\n")


if __name__ == '__main__':
    solve()
