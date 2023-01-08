from typing import List
import sys

sys.stdin = open("blocks.in", "r")
sys.stdout = open("blocks.out", "w")

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
    n = read_int()
    letters = [0 for _ in range(26)]

    for _ in range(n):
        word1, word2 = read_strings()
        occ = [0 for _ in range(26)]
        for c in word1:
            occ[ord(c) - ord('a')] += 1
        occ2 = [0 for _ in range(26)]
        for c in word2:
            occ2[ord(c) - ord('a')] += 1

        for i in range(26):
            letters[i] += max(occ[i], occ2[i])

    for i in range(26):
        print_(f"{letters[i]}\n")


if __name__ == '__main__':
    solve()
