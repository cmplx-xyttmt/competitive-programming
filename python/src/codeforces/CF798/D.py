import math
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
    t = read_int()
    for test in range(t):
        n, m = read_ints()
        grid = []
        blacks = []
        for row in range(n):
            grid.append(read_line())
            for col in range(m):
                if grid[row][col] == 'B':
                    blacks.append((col + 1, n - row))
        # print(blacks)
        coord_sum = [x + y for x, y in blacks]
        coord_diff = [x - y for x, y in blacks]
        min_sum, max_sum = min(coord_sum), max(coord_sum)
        min_diff, max_diff = min(coord_diff), max(coord_diff)

        range_sum = max_sum - min_sum
        range_diff = max_diff - min_diff
        s, b = min(range_sum, range_diff), max(range_sum, range_diff)
        if s % 2 == 0 and b % 2 == 0 and ((s - b) // 2) % 2 == 1:
            min_max = b // 2 + 1
        else:
            min_max = math.ceil((b + 1) / 2)
        found = False
        for i in range(max_sum - min_max, min_sum + min_max + 1):
            for j in range(max_diff - min_max, min_diff + min_max + 1):
                if (i + j) % 2 == 0:
                    # found = True
                    x, y = (i + j) // 2, (i - j) // 2
                    row, col = n - y, x
                    print_(f"Test: {test}: {row} {col}\n")
                    break
            if found:
                break


if __name__ == '__main__':
    solve()
