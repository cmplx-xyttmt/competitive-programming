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

def expand_grid(grid: List[str]):
    rows_with_galaxies = set()
    columns_with_galaxies = set()
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == '#':
                rows_with_galaxies.add(r)
                columns_with_galaxies.add(c)

    new_grid = []
    for r in range(len(grid)):
        new_col = []
        for c in range(len(grid[r])):
            new_col.append(grid[r][c])
            if c not in columns_with_galaxies:
                new_col.append(grid[r][c])
        new_grid.append("".join(new_col))
        if r not in rows_with_galaxies:
            new_grid.append(new_grid[-1])

    return new_grid, rows_with_galaxies, columns_with_galaxies


def get_galaxies(grid: List[str]):
    galaxies = []
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == '#':
                galaxies.append((r, c))

    return galaxies


def get_pairwise_distances_sum(grid: List[str]):
    galaxies = get_galaxies(grid)

    # print(len(galaxies))
    total = 0
    for galaxy1 in galaxies:
        for galaxy2 in galaxies:
            if galaxy1 != galaxy2:
                total += abs(galaxy1[0] - galaxy2[0]) + abs(galaxy1[1] - galaxy2[1])

    return total // 2


def empty_counts(rows:int, cols: int, galaxy_rows: Set[int], galaxy_cols: Set[int]):
    # returns prefix sum of empty rows and columns
    empty_cols = [0 for _ in range(rows)]
    empty_rows = [0 for _ in range(cols)]
    for r in range(rows):
        empty_rows[r] = (1 if r not in galaxy_rows else 0) + empty_rows[r - 1]
    for c in range(cols):
        empty_cols[c] = (1 if c not in galaxy_cols else 0) + empty_cols[c - 1]

    return empty_rows, empty_cols


def pairwise_distance_with_expansion(grid: List[str], empty_rows_pref: List[int], empty_cols_pref: List[int], expansion_factor: int):
    total = 0
    galaxies = get_galaxies(grid)
    for i in range(len(galaxies)):
        for j in range(i + 1, len(galaxies)):
            g1, g2 = galaxies[i], galaxies[j]
            total_rows_between = abs(g1[0] - g2[0])
            empty_rows = empty_rows_pref[max(g2[0], g1[0])] - empty_rows_pref[min(g2[0], g1[0])]
            distance = empty_rows * expansion_factor + (total_rows_between - empty_rows)

            total_cols_between = abs(g1[1] - g2[1])
            empty_cols = empty_cols_pref[max(g2[1], g1[1])] - empty_cols_pref[min(g2[1], g1[1])]
            distance += empty_cols * expansion_factor + (total_cols_between - empty_cols)
            total += distance
    return total


def solve():
    grid = []
    line = read_line()
    while line:
        grid.append(line)
        line = read_line()

    new_grid, galaxy_rows, galaxy_cols = expand_grid(grid)
    # new_grid_display = '\n'.join(new_grid)
    # print(new_grid_display)
    print(f"Part 1: {get_pairwise_distances_sum(new_grid)}")
    empty_rows_pref, empty_cols_pref = empty_counts(len(grid), len(grid[0]), galaxy_rows, galaxy_cols)
    print(f"Part 1 (efficient): {pairwise_distance_with_expansion(grid, empty_rows_pref, empty_cols_pref, 2)}")
    print(f"(expansion = 10): {pairwise_distance_with_expansion(grid, empty_rows_pref, empty_cols_pref, 10)}")
    print(f"(expansion = 100): {pairwise_distance_with_expansion(grid, empty_rows_pref, empty_cols_pref, 100)}")
    print(f"Part 2: {pairwise_distance_with_expansion(grid, empty_rows_pref, empty_cols_pref, 1000000)}")


if __name__ == '__main__':
    solve()
