from typing import List
import sys
from collections import Counter
import heapq

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
    t = read_int()

    for _ in range(t):
        read_int()
        groups = list(Counter([0] + read_ints()).values())
        groups.sort(reverse=True)
        m = len(groups)
        for i in range(m):
            groups[i] -= min(groups[i], m - i)

        groups = [-num for num in groups if num > 0]
        t = 0
        heapq.heapify(groups)
        while groups:
            # print(t, groups)
            biggest = -heapq.heappop(groups)
            if biggest - t > 0:
                t += 1
                biggest -= 1
                heapq.heappush(groups, -biggest)

        print_(f"{m + t}\n")


if __name__ == '__main__':
    solve()
