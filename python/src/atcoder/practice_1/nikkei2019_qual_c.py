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


class Dish:

    def __init__(self, a, b, i):
        self.a = a
        self.b = b
        self.id = i


def solve():
    n = read_int()
    dishes = []

    for i in range(n):
        a, b = read_ints()
        dishes.append(Dish(a, b, i))

    dishes.sort(key=lambda dish: dish.a + dish.b, reverse=True)
    a_total, b_total = 0, 0
    for i in range(n):
        if i % 2 == 0:
            a_total += dishes[i].a
        else:
            b_total += dishes[i].b
    print_(f"{a_total - b_total}\n")


if __name__ == '__main__':
    solve()
