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
    n = read_int()
    info = []
    for _ in range(n):
        x, y, h = read_ints()
        info.append((x, y, h))
    ans = None
    for cx, cy in [(cx, cy) for cx in range(101) for cy in range(101)]:
        max_height = float('inf')
        actual_height = None
        found = True
        for x, y, h in info:
            if h == 0:
                max_height = min(abs(x - cx) + abs(y - cy), max_height)
                if max_height <= 0 or (actual_height and max_height < actual_height):
                    found = False
                    break
            else:
                H = h + abs(x - cx) + abs(y - cy)
                if H > max_height or (actual_height and actual_height != H):
                    found = False
                    break
                else:
                    actual_height = H
        if found:
            H = actual_height if actual_height else max_height
            ans = (cx, cy, H)
            break
    cx, cy, H = ans
    print(cx, cy, H)


if __name__ == '__main__':
    solve()
