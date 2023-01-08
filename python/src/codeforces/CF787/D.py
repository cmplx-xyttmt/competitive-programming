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
def dfs(node, adj, prev, is_first_child, ans):
    if not is_first_child:
        ans.append([node])
    else:
        ans[-1].append(node)

    first = True
    for v in adj[node]:
        if v != prev:
            yield dfs(v, adj, node, first, ans)
            first = False

    yield None


def solve():
    t = read_int()
    for _ in range(t):
        n = read_int()
        p = read_ints()
        adj = [[] for _ in range(n + 1)]
        root = 0
        for i in range(n):
            if i + 1 == p[i]:
                root = i + 1
                continue
            adj[i + 1].append(p[i])
            adj[p[i]].append(i + 1)
        ans = []
        dfs(root, adj, 0, False, ans)
        print_(f"{len(ans)}\n")
        for lst in ans:
            print_(f"{len(lst)}\n")
            print_(f"{' '.join(map(str, lst))}\n")


if __name__ == '__main__':
    solve()
