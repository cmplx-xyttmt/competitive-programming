from typing import List
import sys

sys.stdin = open("shuffle.in", "r")
sys.stdout = open("shuffle.out", "w")

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


def unshuffle(perm, ids):
    result = ["" for _ in range(len(ids))]

    for i in range(1, len(ids)):
        result[i] = ids[perm[i]]

    return result


def solve():
    n = read_int()
    perm = [0] + read_ints()
    ids = [""] + read_strings()

    for _ in range(3):
        ids = unshuffle(perm, ids)

    print_("\n".join(ids[1:]))
    print_("\n")


if __name__ == '__main__':
    solve()
