from typing import List, Set
import sys

sys.stdin = open("day3.in", "r")
sys.stdout = open("day3.out", "w")

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


def get_intersection(items: List[Set[str]]):
    intersection = items[0].intersection(items[1])
    for item in items[2:]:
        intersection = intersection.intersection(item)
    return intersection


def calc_priority(item_set: Set[str]):
    priority = 0
    for item in item_set:
        if item.islower():
            priority += ord(item) - ord('a') + 1
        else:
            priority += ord(item) - ord('A') + 27
    return priority


def solve():

    line = read_line()
    priority1 = 0
    priority2 = 0
    elves = []
    while line:
        elves.append(line)
        half = len(line) // 2
        ruck1 = set(line[:half])
        ruck2 = set(line[half:])
        priority1 += calc_priority(get_intersection([ruck1, ruck2]))
        line = read_line()

    print(f"Part 1: {priority1}")

    for i in range(0, len(elves), 3):
        priority2 += calc_priority(get_intersection([set(elf) for elf in elves[i:i+3]]))

    print(f"Part 2: {priority2}")


if __name__ == '__main__':
    solve()
