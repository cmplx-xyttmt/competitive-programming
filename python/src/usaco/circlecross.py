from typing import List
import sys

sys.stdin = open("circlecross.in", "r")
sys.stdout = open("circlecross.out", "w")

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
    circle = list(map(lambda c: ord(c) - ord('A'), readline()))
    first = [-1] * 26
    second = [-1] * 26

    for i in range(26):
        for j in range(len(circle)):
            if circle[j] == i:
                if first[i] == -1:
                    first[i] = j
                else:
                    second[i] = j

    crossing = 0

    for i in range(26):
        for j in range(i + 1, 26):
            # i1 j1 i2 j2 or j1 i1 j2 i2
            # cross = first[i] < first[j] < second[i] < second[j] or first[j] < first[i] < second[j] < second[i]
            dont_cross = second[i] < first[j] or second[j] < first[i] \
                         or first[i] < first[j] < second[j] < second[i] or first[j] < first[i] < second[i] < second[j]
            if not dont_cross:
                crossing += 1

    print_(f"{crossing}\n")


if __name__ == '__main__':
    solve()
