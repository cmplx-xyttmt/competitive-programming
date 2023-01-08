from collections import defaultdict
from typing import List
import sys
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
    for test in range(1, t + 1):
        d, n, x = read_ints()
        groups = defaultdict(list)
        for _ in range(n):
            q, l, v = read_ints()
            groups[d - l].append((-v, q))

        heap = []
        days = list(groups.keys())
        days.sort(reverse=True)
        profit = 0
        # print(groups)
        for i in range(len(days)):
            curr_day = days[i]
            for plant in groups[curr_day]:
                heapq.heappush(heap, plant)

            nxt_day = 0 if i == len(days) - 1 else days[i + 1]
            days_available = curr_day - nxt_day
            can_plant = days_available * x
            # print(curr_day, nxt_day, can_plant)
            while heap and can_plant > 0:
                v, q = heapq.heappop(heap)
                v = -v
                profit += v * min(can_plant, q)
                # print(curr_day, (v, q))
                if q > can_plant:
                    heapq.heappush(heap, (-v, q - can_plant))
                can_plant -= min(can_plant, q)

        print_(f"Case #{test}: {profit}\n")


if __name__ == '__main__':
    solve()
