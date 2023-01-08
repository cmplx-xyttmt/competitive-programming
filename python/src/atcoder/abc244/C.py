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


def get_next_unseen(prev_int, seen_ints):
    while seen_ints[prev_int]:
        prev_int += 1

    return prev_int


def solve():
    n = read_int()
    seen_ints = [False for _ in range(2 * n + 2)]
    prev_index = 1
    for _ in range(n):
        print_(f"{prev_index}\n")
        flush()
        comp = read_int()
        seen_ints[prev_index] = True
        seen_ints[comp] = True
        prev_index = get_next_unseen(prev_index, seen_ints)

    print(prev_index)
    flush()
    read_int()


if __name__ == '__main__':
    solve()
