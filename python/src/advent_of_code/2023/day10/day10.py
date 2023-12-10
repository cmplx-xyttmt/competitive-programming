from typing import List, Tuple, Set
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


def next_tiles(curr: Tuple[int, int], grid: List[str]) -> List[Tuple[int, int]]:
    i, j = curr
    if grid[i][j] == "|":
        return [(i - 1, j), (i + 1, j)]
    if grid[i][j] == "-":
        return [(i, j - 1), (i, j + 1)]
    if grid[i][j] == "L":
        return [(i - 1, j), (i, j + 1)]
    if grid[i][j] == "J":
        return [(i - 1, j), (i, j - 1)]
    if grid[i][j] == "7":
        return [(i + 1, j), (i, j - 1)]
    if grid[i][j] == "F":
        return [(i + 1, j), (i, j + 1)]
    return []


def can_move(fro: Tuple[int, int], to: Tuple[int, int], grid: List[str]) -> bool:
    return fro in next_tiles(to, grid)


def find_farthest(start: Tuple[int, int], grid: List[str]):
    seen = dict()
    diff = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    possible_nexts = [(start[0] + dr, start[1] + dc) for dr, dc in diff]
    nexts = [to for to in possible_nexts if can_move(start, to, grid)]
    # print(nexts)
    seen[start] = 0
    for nxt in nexts:
        seen[nxt] = 1
    while len(nexts) > 0:
        new_nexts = []
        # print(nexts)
        for curr in nexts:
            next_list = next_tiles(curr, grid)
            for nxt in next_list:
                if nxt not in seen:
                    seen[nxt] = seen[curr] + 1
                    new_nexts.append(nxt)
        nexts = new_nexts

    return max(seen.values()), set(seen.keys())


def find_enclosed_area(loop_tiles: Set[Tuple[int, int]], grid: List[str]) -> int:
    inside_tiles = 0

    # left to right sweep line
    for r in range(len(grid)):
        poly_intersections = 0
        for c in range(len(grid[r])):
            if (r, c) in loop_tiles:
                if grid[r][c] in ["|", "L", "J"]:
                    poly_intersections += 1
            else:
                inside_tiles += int(poly_intersections % 2 == 1)
    return inside_tiles


def solve():
    grid = []
    line = read_line()
    while line:
        grid.append(line)
        line = read_line()

    start = (0, 0)
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == 'S':
                start = (r, c)

    farthest, loop_tiles = find_farthest(start, grid)
    print(f"Part 1: {farthest}")
    print(f"Part 2: {find_enclosed_area(loop_tiles, grid)}")


if __name__ == '__main__':
    solve()
