from collections import defaultdict
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


def solve():
    n = read_int()
    people = []
    unique_names = defaultdict(int)
    for _ in range(n):
        first, last = read_strings()
        people.append((first, last))
        unique_names[first] += 1
        if first != last:
            unique_names[last] += 1

    can = True
    for first, last in people:
        if unique_names[first] > 1 and unique_names[last] > 1:
            can = False
            break

    print_(f"{'Yes' if can else 'No'}\n")


if __name__ == '__main__':
    solve()
