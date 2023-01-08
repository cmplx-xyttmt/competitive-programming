from typing import List
import sys

sys.stdin = open("cownomics.in", "r")
sys.stdout = open("cownomics.out", "w")

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
    n, m = read_ints()

    spotty = []
    plain = []

    for _ in range(n):
        spotty.append(readline())

    for _ in range(n):
        plain.append(readline())

    ans = 0
    for j in range(m):
        chars_spotty = set([spotty[i][j] for i in range(n)])
        chars_plain = set([plain[i][j] for i in range(n)])

        if len(chars_plain.intersection(chars_spotty)) == 0:
            ans += 1

    print_(f"{ans}\n")


if __name__ == '__main__':
    solve()
