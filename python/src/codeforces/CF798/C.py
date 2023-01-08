from collections import deque
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


class TreeNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


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
def dfs(node):
    if not (node.left or node.right):
        yield 1, 0
    if not node.left or not node.right:
        yield 1, 1
    infected_left, removed_left = yield dfs(node.left)
    infected_right, removed_right = yield dfs(node.right)
    if infected_left + removed_left < infected_right + removed_right:
        yield 1 + infected_left, 1 + removed_left
    else:
        yield 1 + infected_right, 1 + removed_right


def solve():
    t = read_int()
    for _ in range(t):
        n = read_int()
        adj = [[] for _ in range(n + 1)]
        for _ in range(n - 1):
            u, v = read_ints()
            adj[u].append(v)
            adj[v].append(u)

        root = TreeNode(1)
        q = deque()
        q.append(root)
        seen = set()
        while q:
            node = q.popleft()
            seen.add(node.value)
            for neighbor in adj[node.value]:
                if neighbor not in seen:
                    if not node.left:
                        node.left = TreeNode(neighbor)
                        q.append(node.left)
                    else:
                        node.right = TreeNode(neighbor)
                        q.append(node.right)
        print_(f"{n - sum(dfs(root))}\n")


if __name__ == '__main__':
    solve()
