from typing import List
import sys

sys.stdin = open("gymnastics.in", "r")
sys.stdout = open("gymnastics.out", "w")

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


def solve():
    k, n = read_ints()
    positions = [[] for _ in range(n + 1)]

    for _ in range(k):
        ranking = read_ints()
        for index, num in enumerate(ranking):
            positions[num].append(index)

    consistent = 0

    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            relative_ranking = positions[i][0] < positions[j][0]
            is_consistent = True
            for p in range(1, k):
                if (positions[i][p] < positions[j][p]) != relative_ranking:
                    is_consistent = False
                    break

            if is_consistent:
                consistent += 1

    print_(f"{consistent}\n")


if __name__ == '__main__':
    solve()
