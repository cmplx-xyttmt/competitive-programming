from typing import List
import sys
from collections import deque

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
    q = read_int()
    queue = deque()

    for _ in range(q):
        nums = read_ints()
        if nums[0] == 1:
            x, c = nums[1:]
            queue.append((x, c))
        else:
            c = nums[1]
            total = 0
            while c > 0:
                num, occ = queue.popleft()
                remove = min(c, occ)
                total += remove * num
                c -= remove
                if occ != remove:
                    queue.appendleft((num, occ - remove))
            print_(f"{total}\n")


if __name__ == '__main__':
    solve()
