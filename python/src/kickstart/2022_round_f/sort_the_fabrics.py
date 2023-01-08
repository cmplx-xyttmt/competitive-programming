from typing import List
import sys

input_ = sys.stdin.readline
print_ = sys.stdout.write
flush = sys.stdout.flush


class Fabric:

    def __init__(self, color: str, durability: int, id_: int):
        self.color = color
        self.durability = durability
        self.id_ = id_


def read_line() -> str:
    return input_().strip()


def read_int() -> int:
    return int(read_line())


def read_strings() -> List[str]:
    return list(read_line().split())


def read_ints():
    return list(map(int, read_line().split()))


def solve():
    t = read_int()
    for test in range(1, t + 1):
        n = read_int()
        fabrics: List[Fabric] = []
        for _ in range(n):
            color, d, id_ = read_strings()
            fabrics.append(Fabric(color, int(d), int(id_)))

        fabrics.sort(key=lambda f: (f.color, f.id_))
        sorted_color = [fabric.id_ for fabric in fabrics]
        fabrics.sort(key=lambda f: (f.durability, f.id_))
        sorted_durability = [fabric.id_ for fabric in fabrics]
        same_position = 0
        for i in range(n):
            if sorted_color[i] == sorted_durability[i]:
                same_position += 1

        print_(f"Case #{test}: {same_position}\n")


if __name__ == '__main__':
    solve()
