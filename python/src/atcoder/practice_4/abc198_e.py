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


def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to

    return wrappedfunc


@bootstrap
def dfs(vertex, prev_vertex, tree, colors, seen_colors, good_vertices):
    if not seen_colors[colors[vertex]]:
        good_vertices[vertex] = True

    seen_colors[colors[vertex]] += 1

    for node in tree[vertex]:
        if node != prev_vertex:
            yield dfs(node, vertex, tree, colors, seen_colors, good_vertices)

    seen_colors[colors[vertex]] -= 1
    yield None


def solve():
    n = read_int()
    c = [-1] + read_ints()
    tree = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a, b = read_ints()
        tree[a].append(b)
        tree[b].append(a)

    max_color = int(1e5)
    seen_colors = [0 for _ in range(max_color + 1)]
    good_vertices = [False for _ in range(n + 1)]

    dfs(1, -1, tree, c, seen_colors, good_vertices)

    print('\n'.join(map(str, [i for i in range(n + 1) if good_vertices[i]])))


if __name__ == '__main__':
    solve()
