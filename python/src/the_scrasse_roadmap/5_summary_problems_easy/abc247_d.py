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
    queries = read_int()
    q = deque()

    for _ in range(queries):
        query = read_ints()
        if query[0] == 1:
            q.append((query[1], query[2]))
        else:
            total = 0
            c = query[1]
            while c > 0:
                x, items = q.popleft()
                rem = min(c, items)
                total += x * rem
                c -= rem
                if items > rem:
                    q.appendleft((x, items - rem))
            print_(f"{total}\n")


if __name__ == '__main__':
    solve()
