from typing import List
import sys

sys.stdin = open("cbarn.in", "r")
sys.stdout = open("cbarn.out", "w")

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
    r = [read_int() for _ in range(n)]
    best_distance = float('inf')
    for start in range(n):
        total_distance = 0
        curr = (start + 1) % n
        dist = 1
        while curr != start:
            total_distance += r[curr] * dist
            dist += 1
            curr = (curr + 1) % n
        best_distance = min(best_distance, total_distance)

    print_(f"{best_distance}\n")


if __name__ == '__main__':
    solve()
