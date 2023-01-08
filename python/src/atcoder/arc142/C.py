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


def get_distance(u, v):
    print_(f"? {u} {v}\n")
    flush()
    return read_int()


def solve():
    n = read_int()
    add = n + 1
    threes = []
    for u in range(3, n + 1):
        x = get_distance(1, u)
        y = get_distance(2, u)
        add = min(x + y, add)
        if x + y == 3:
            threes.append(u)

    if add != 3:
        ans = add
    elif len(threes) != 2:
        ans = 1
    else:
        dist = get_distance(threes[0], threes[1])
        ans = 3 if dist == 1 else 1
    print_(f"! {ans}\n")
    flush()


if __name__ == '__main__':
    solve()
