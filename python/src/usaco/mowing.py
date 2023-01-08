from typing import List
import sys

sys.stdin = open("mowing.in", "r")
sys.stdout = open("mowing.out", "w")

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
    last_seen = dict()
    n = read_int()
    directions = {'N': (0, 1), 'S': (0, -1), 'E': (1, 0), 'W': (-1, 0)}
    curr = (0, 0)
    last_seen[curr] = 0
    t = 0
    INF = float('inf')
    x = INF
    for _ in range(n):
        direction, steps = read_strings()
        steps = int(steps)
        for _ in range(steps):
            t += 1
            dx, dy = directions[direction]
            curr = curr[0] + dx, curr[1] + dy
            if curr in last_seen:
                x = min(x, t - last_seen[curr])
            last_seen[curr] = t

    if x == INF:
        x = -1
    print_(f"{x}\n")


if __name__ == '__main__':
    solve()
