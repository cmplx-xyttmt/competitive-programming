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
    a = read_ints()

    generations = [0] * (2 * n + 2)

    for i in range(n):
        prev = a[i]
        nxt_1 = 2 * (i + 1)
        nxt_2 = nxt_1 + 1
        generations[nxt_1] = generations[prev] + 1
        generations[nxt_2] = generations[prev] + 1

    ans = '\n'.join(map(str, generations[1:]))

    print_(f"{ans}\n")


if __name__ == '__main__':
    solve()
