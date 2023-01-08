from typing import List, Tuple, Optional
from types import GeneratorType
import sys

sys.setrecursionlimit(int(1e6))
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


def get_range(node, prev, start):
    low, high = start, start
    nxt_low = start
    for nxt in tree[node]:
        if nxt != prev:
            r = yield get_range(nxt, node, nxt_low)
            high = max(high, r)
            nxt_low = high + 1

    ans[node] = (low, high)
    yield high


def solve():
    for _ in range(n - 1):
        u, v = read_ints()
        tree[u].append(v)
        tree[v].append(u)

    boot_get_range = bootstrap(get_range)
    boot_get_range(1, -1, 1)
    answer = []
    for i in range(1, n + 1):
        answer.append(f"{ans[i][0]} {ans[i][1]}\n")

    print_(f"{''.join(answer)}")


if __name__ == '__main__':
    n = read_int()
    tree = [[] for _ in range(n + 1)]
    ans: List[Optional[Tuple[int, int]]] = [None for _ in range(n + 1)]
    solve()
