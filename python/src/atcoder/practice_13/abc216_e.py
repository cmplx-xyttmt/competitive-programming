import heapq
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
    n, k = read_ints()
    a = read_ints()
    heap = []  # key=-val, occ, val
    for num in a:
        heapq.heappush(heap, (-num, 1, num))

    ans = 0
    while heap and heap[0][2] > 0 and k >= 0:
        # print("Before: ", heap)
        _, occ, num = heapq.heappop(heap)
        diff = num if len(heap) == 0 else num - heap[0][2]
        if occ * diff <= k:
            ans += occ * ((diff * (diff + 1)) // 2 + (num - diff) * diff)
            k -= (occ * diff)
            new_num = 0 if not heap else heap[0][2]
            while heap and heap[0][2] == new_num:
                heapq.heappop(heap)
                occ += 1
            heapq.heappush(heap, (-new_num, occ, new_num))
        else:
            q, rem = divmod(k, occ)
            diff = q
            ans += occ * ((diff * (diff + 1)) // 2 + (num - diff) * diff)
            ans += rem * (num - diff)
            k = 0
        # print("After: ", heap, ans, k)
    print_(f"{ans}\n")


if __name__ == '__main__':
    solve()
