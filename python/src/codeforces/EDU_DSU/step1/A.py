from types import GeneratorType
from typing import List
import sys


input_ = sys.stdin.readline
print_ = sys.stdout.write
flush = sys.stdout.flush


def readline() -> str:
    return input_().strip()


def read_int() -> int:
    return int(readline())


def read_strings() -> List[str]:
    return list(readline().split())


def read_ints():
    return list(map(int, readline().split()))


# def bootstrap(f, stack=[]):
#     def wrappedfunc(*args, **kwargs):
#         if stack:
#             return f(*args, **kwargs)
#         else:
#             to = f(*args, **kwargs)
#             while True:
#                 if type(to) is GeneratorType:
#                     stack.append(to)
#                     to = next(to)
#                 else:
#                     stack.pop()
#                     if not stack:
#                         break
#                     to = stack[-1].send(to)
#             return to
#
#     return wrappedfunc
#
#
# @bootstrap
# def get_parent(a, parent):
#     if a != parent[a]:
#         parent[a] = yield get_parent(parent[a], parent)
#
#     yield parent[a]


def get_parent(a, parents):
    path = []
    while a != parents[a]:
        path.append(a)
        a = parents[a]

    p = a
    for a in path:
        parents[a] = p

    return p


def union(a, b, parent, size):
    a, b = get_parent(a, parent), get_parent(b, parent)
    if a == b:
        return

    if size[b] > size[a]:
        a, b = b, a

    parent[a] = b
    size[b] += size[a]


def solve():
    n, m = read_ints()
    parent = [i for i in range(n + 1)]
    size = [1] * (n + 1)
    ans = []
    for _ in range(m):
        query, a, b = read_strings()
        a, b = int(a), int(b)
        if query == 'union':
            union(a, b, parent, size)
        else:
            ans.append("YES" if get_parent(a, parent) == get_parent(b, parent) else "NO")

    sep = '\n'
    print_(f"{sep.join(ans)}\n")


if __name__ == '__main__':
    solve()
