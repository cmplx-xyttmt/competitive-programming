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


def get_parent(a, parents):
    path = []
    while a != parents[a]:
        path.append(a)
        a = parents[a]

    p = a
    for a in path:
        parents[a] = p

    return p


def union(a, b, parents, minimum, maximum, size):
    a, b = get_parent(a, parents), get_parent(b, parents)
    if a == b:
        return

    if size[a] > size[b]:
        a, b = b, a

    parents[a] = b
    size[b] += size[a]
    minimum[b] = min(minimum[a], minimum[b])
    maximum[b] = max(maximum[a], maximum[b])


def solve():
    n, m = read_ints()
    size = [1 for _ in range(n + 1)]
    minimum = [i for i in range(n + 1)]
    maximum = [i for i in range(n + 1)]
    parents = [i for i in range(n + 1)]
    for _ in range(m):
        line = read_strings()
        op = line[0]
        if op == 'union':
            a, b = map(int, line[1:])
            union(a, b, parents, minimum, maximum, size)
        else:
            a = int(line[1])
            p = get_parent(a, parents)
            print_(f"{minimum[p]} {maximum[p]} {size[p]}\n")


if __name__ == '__main__':
    solve()
