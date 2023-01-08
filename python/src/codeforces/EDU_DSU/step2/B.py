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


def get_parent(slot, parent):
    path = []

    while slot != parent[slot]:
        path.append(slot)
        slot = parent[slot]

    for p in path:
        parent[p] = slot

    return slot


def solve():
    n = read_int()

    p = read_ints()

    parent = [i for i in range(n + 1)]

    ans = []
    for i in range(n):
        next_free_slot = get_parent(p[i], parent)
        ans.append(next_free_slot)
        parent[next_free_slot] = (next_free_slot + 1) % (n + 1)
        if parent[next_free_slot] == 0:
            parent[next_free_slot] = 1

    print_(f"{' '.join(map(str, ans))}\n")


if __name__ == '__main__':
    solve()
