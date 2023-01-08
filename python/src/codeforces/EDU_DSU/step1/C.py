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


def get_parent(a, parent, points):
    score = points[a]
    while a != parent[a]:
        a = parent[a]
        score += points[a]
    return a, score


def add(a, score, parent, points):
    a = get_parent(a, parent, points)[0]
    points[a] += score


def union(a, b, parent, points, size):
    a, b = get_parent(a, parent, points)[0], get_parent(b, parent, points)[0]
    if a == b:
        return

    if size[a] > size[b]:
        a, b = b, a

    size[b] += size[a]
    points[a] -= points[b]
    parent[a] = b


def solve():
    n, m = read_ints()
    points = [0 for _ in range(n + 1)]
    size = [1 for _ in range(n + 1)]
    parent = [i for i in range(n + 1)]
    for _ in range(m):
        line = read_strings()
        op = line[0]
        if op == 'add':
            a, score = map(int, line[1:])
            add(a, score, parent, points)
        elif op == 'join':
            a, b = map(int, line[1:])
            union(a, b, parent, points, size)
        else:
            a = int(line[1])
            _, score = get_parent(a, parent, points)
            print_(f"{score}\n")


if __name__ == '__main__':
    solve()
