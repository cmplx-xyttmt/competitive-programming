from collections import deque
from typing import List
import sys

sys.stdin = open("day7.in", "r")
sys.stdout = open("day7.out", "w")

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


class Node:

    def __init__(self, parent=None):
        self.parent = parent
        self.children = dict()  # dirname -> Node
        self.files = dict()  # filename -> size
        self.size = 0


def calculate_size(node: Node, sizes: List[int]):
    node.size = sum(node.files.values())
    for child in node.children.values():
        child_size = calculate_size(child, sizes)
        node.size += child_size

    sizes.append(node.size)
    return node.size


def sum_size_less_than(root, limit):
    q = deque()
    q.append(root)
    total_size = 0
    while q:
        node = q.popleft()
        if node.size <= limit:
            total_size += node.size
        for child in node.children.values():
            q.append(child)

    return total_size


def solve():
    root = Node()
    root.children['/'] = Node(root)
    curr_node = root
    for line in sys.stdin.readlines():
        output = line.strip().split(" ")
        if output[0] == '$':
            command = output[1]
            if command == 'cd':
                if output[2] == '..':
                    curr_node = curr_node.parent
                else:
                    curr_node = curr_node.children[output[2]]
        else:
            if output[0] == 'dir':
                curr_node.children[output[1]] = Node(curr_node)
            else:
                curr_node.files[output[1]] = int(output[0])

    sizes = []
    total_size = calculate_size(root, sizes)
    print(total_size)

    limit = 100000
    print(f"Part 1: {sum_size_less_than(root, limit)}")

    free_space = 70_000_000 - total_size
    min_freeable_space = 30_000_000 - free_space
    print(f"Part 2: {min([size for size in sizes if size >= min_freeable_space])}")


if __name__ == '__main__':
    solve()
