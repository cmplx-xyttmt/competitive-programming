from functools import cmp_to_key
from typing import List
import sys

sys.stdin = open("day13.in", "r")
sys.stdout = open("day13.out", "w")

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


def compare_lists(list1, list2):
    if type(list1) == int and type(list2) == int:
        return -1 if list1 < list2 else (0 if list1 == list2 else 1)

    if type(list1) == int:
        list1 = [list1]
    if type(list2) == int:
        list2 = [list2]

    size = min(len(list1), len(list2))
    for i in range(size):
        comp = compare_lists(list1[i], list2[i])
        if comp != 0:
            return comp
    if size < len(list1):
        return 1
    if size < len(list2):
        return -1
    return 0


def solve():
    line = read_line()
    right_order = []
    idx = 0
    lists = []
    while line:
        list1 = eval(line)
        list2 = eval(read_line())
        lists.append(list1)
        lists.append(list2)
        idx += 1
        if compare_lists(list1, list2) == -1:
            right_order.append(idx)
        read_line()
        line = read_line()

    print(f"Part 1: {sum(right_order)}")
    lists.append([[2]])
    lists.append([[6]])
    lists.sort(key=cmp_to_key(compare_lists))
    dividers = []
    for i in range(len(lists)):
        if str(lists[i]) == "[[2]]" or str(lists[i]) == "[[6]]":
            dividers.append(i + 1)

    print(f"Part 2: {dividers[0] * dividers[1]}")


if __name__ == '__main__':
    solve()
