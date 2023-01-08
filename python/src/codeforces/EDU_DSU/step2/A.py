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


def get_parent(num, parent):
    path = []
    while num is not None and num != parent[num]:
        path.append(num)
        num = parent[num]

    if not num:
        return -1

    for a in path:
        parent[a] = num

    return num


def solve():
    n, m = read_ints()

    parent = [i for i in range(n + 1)]

    for _ in range(m):
        op, num = read_strings()
        num = int(num)
        if op == '-':
            parent[num] = None if num == n else num + 1
        else:
            print_(f"{get_parent(num, parent)}\n")


if __name__ == '__main__':
    solve()
