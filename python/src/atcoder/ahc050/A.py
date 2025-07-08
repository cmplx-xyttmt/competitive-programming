from typing import List
import sys
import random

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


INF = int(1e18)


def get_least_likely_robot_end(n, rink):
    """
    Get cell with the lowest probability to have a robot on it.
    """
    # num_end[i][j] -> number of (cell, direction) pairs that end up at cell i, j
    num_end = []
    for i in range(n):
        num_end.append([])
        for j in range(n):
            if rink[i][j] == '#':
                num_end[i].append(INF)
            else:
                num_end[i].append(0)

    for i in range(n):
        for j in range(n):
            if num_end[i][j] == '#':
                continue
            for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                x, y = i, j
                dir_x, dir_y = direction
                nxt_x, nxt_y = x + dir_x, y + dir_y
                while 0 <= nxt_x < n and 0 <= nxt_y < n:
                    x, y = nxt_x, nxt_y
                    nxt_x, nxt_y = x + dir_x, y + dir_y
                num_end[x][y] += 1

    minimum = INF
    best = (0, 0)
    for i in range(n):
        for j in range(n):
            if num_end[i][j] < minimum:
                minimum = num_end[i][j]
                best = (i, j)

    return best


def solve():
    n, m = read_ints()
    ice_rink = [list(read_line()) for _ in range(n)]
    free_cells = [(i, j) for i in range(n) for j in range(n) if ice_rink[i][j] == '.']

    # # random_strategy
    # shuffled_free_cells = [cell for cell in free_cells]
    # random.shuffle(shuffled_free_cells)
    # for x, y in shuffled_free_cells:
    #     print_(f"{x} {y}\n")

    ordering = []
    while len(ordering) < n ** 2 - m:
        px, py = get_least_likely_robot_end(n, ice_rink)
        ice_rink[px][py] = '#'
        ordering.append((px, py))

    for x, y in ordering:
        print_(f"{x} {y}\n")


if __name__ == '__main__':
    solve()
