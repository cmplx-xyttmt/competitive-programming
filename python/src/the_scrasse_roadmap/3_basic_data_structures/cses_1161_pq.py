from typing import List
import sys
from queue import PriorityQueue

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


def solve():
    read_ints()
    # solution: do the operations in reverse order. Always combine the smallest sticks since they have the lowest cost.
    sticks = PriorityQueue()
    for stick in read_ints():
        sticks.put(stick)
    cost = 0
    while sticks.qsize() >= 2:
        new_stick = sticks.get() + sticks.get()
        cost += new_stick
        sticks.put(new_stick)

    print_(f"{cost}\n")


if __name__ == '__main__':
    solve()
