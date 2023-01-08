from typing import List, Optional, Tuple
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
    for _ in range(t):
        n, m = read_ints()
        grid = []
        for i in range(n):
            grid.append(read_ints())
            for j in range(m):
                if grid[i][j] == -1:
                    grid[i][j] = 0
        if (n + m - 1) % 2 == 1:
            print_('NO\n')
            continue
        ranges: List[List[Optional[Tuple[int, int]]]] = [[None for _ in range(m)] for _ in range(n)]
        ranges[0][0] = (1, 1) if grid[0][0] == 1 else (0, 0)
        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    continue
                num = grid[i][j]
                if i == 0:
                    l, r = ranges[i][j - 1]
                    ranges[i][j] = l + num, r + num
                elif j == 0:
                    l, r = ranges[i - 1][j]
                    ranges[i][j] = l + num, r + num
                else:
                    l1, r1 = ranges[i - 1][j]
                    l2, r2 = ranges[i][j - 1]
                    ranges[i][j] = min(l1, l2) + num, max(r1, r2) + num
        # print(ranges)
        need = (n + m - 1)//2
        l, r = ranges[n - 1][m - 1]
        print_(f"{'YES' if l <= need <= r else 'NO'}\n")


if __name__ == '__main__':
    solve()
