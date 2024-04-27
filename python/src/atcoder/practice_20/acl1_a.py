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


def get_parent(node, parents):
    path = []
    while node != parents[node]:
        path.append(node)
        node = parents[node]

    new_parent = node
    for node in path:
        parents[node] = new_parent

    return new_parent


def union(first, second, parents, size):
    first, second = get_parent(first, parents), get_parent(second, parents)
    if first == second:
        return

    if size[first] > size[second]:
        parents[second] = first
        size[first] += size[second]
    else:
        parents[first] = second
        size[second] += size[first]


def solve():
    n = read_int()
    ys = [(None, None)] * (n + 1)
    for idx in range(n):
        x, y = read_ints()
        ys[x] = (y, idx + 1)

    parents = [p for p in range(n + 1)]
    size = [1 for _ in range(n + 1)]
    stack = []
    for x in range(1, n + 1):
        y, idx = ys[x]
        z = y
        while stack and stack[-1][0] < y:
            z = min(z, stack[-1][0])
            union(idx, stack[-1][1], parents, size)
            stack.pop()
        stack.append((z, idx))

    ans = [size[get_parent(idx, parents)] for idx in range(1, n + 1)]
    ans_str = "\n".join(map(str, ans))
    print_(f"{ans_str}\n")


if __name__ == '__main__':
    solve()
