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


class Node:

    def __init__(self, label: str, focal_length: int):
        self.label = label
        self.focal_length = focal_length
        self.prev = None
        self.next = None

    def __repr__(self):
        return f"({self.label}, {self.focal_length})"


class LList:

    def __init__(self):
        self.start = None
        self.last = None
        self.map = dict()

    def add(self, label: str, focal_length: int):
        if label in self.map:
            node = self.map[label]
            node.focal_length = focal_length
            return

        node = Node(label, focal_length)
        if not self.start:
            self.start = node
            self.last = node
        else:
            self.last.next = node
            node.prev = self.last
            self.last = node
        self.map[node.label] = node

    def remove(self, label: str):
        if label in self.map:
            node = self.map.pop(label)
            if node.prev:
                node.prev.next = node.next
            if node.next:
                node.next.prev = node.prev
            if label == self.start.label:
                self.start = node.next
            if label == self.last.label:
                self.last = node.prev

    def to_list(self) -> List[Node]:
        node = self.start
        res = []
        while node:
            res.append(node)
            node = node.next
        return res

    def __repr__(self):
        return str(self.to_list())


def hash_(string: str) -> int:
    hash_val = 0
    for c in string:
        hash_val = ((hash_val + ord(c)) * 17) % 256
    return hash_val


def focusing_power(boxes: List[LList]) -> int:
    f_power = 0
    for i, box in enumerate(boxes):
        for j, lens in enumerate(box.to_list()):
            f_power += (i + 1) * (j + 1) * lens.focal_length
    return f_power


def solve():
    init_seq = read_line().split(",")
    print(f"Part 1: {sum(map(hash_, init_seq))}")

    boxes = [LList() for _ in range(256)]
    for instruction in init_seq:
        if '=' in instruction:
            label, focal_length = instruction.split("=")
            boxes[hash_(label)].add(label, int(focal_length))
        else:
            label = instruction[:-1]
            boxes[hash_(label)].remove(label)

    print(f"Part 2: {focusing_power(boxes)}")


if __name__ == '__main__':
    solve()
