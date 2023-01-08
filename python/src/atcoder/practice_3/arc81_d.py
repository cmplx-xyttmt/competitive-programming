from typing import List
import sys

input_ = sys.stdin.readline
print_ = sys.stdout.write
flush = sys.stdout.flush


def readline() -> str:
    return input_().strip()


def read_int() -> int:
    return int(readline())


def read_strings() -> List[str]:
    return list(readline().split())


def read_ints():
    return list(map(int, readline().split()))


def solve():
    MOD = int(1e9) + 7
    n = read_int()
    grid = [readline(), readline()]
    # get dominoes
    # order dominoes in order of seen
    # for each domino, need to see which neighbor has already been seen to rule out colors
    #     get coordinates of dominoes: (i, j) (a, b)
    #     prev neighbors: (i - 1, j), (i, j - 1)

    seen = set()
    ans = 1
    for j in range(n):
        for i in range(2):
            if grid[i][j] in seen:
                continue
            # print(grid[i][j])
            a, b = -1, -1
            if i + 1 < 2 and grid[i + 1][j] == grid[i][j]:
                a, b = i + 1, j
            if j + 1 < n and grid[i][j + 1] == grid[i][j]:
                a, b = i, j + 1
            seen_neighbors = set()
            if i - 1 >= 0 and grid[i - 1][j] in seen:
                seen_neighbors.add(grid[i - 1][j])
            if j - 1 >= 0 and grid[i][j - 1] in seen:
                seen_neighbors.add(grid[i][j - 1])
            if a - 1 >= 0 and grid[a - 1][b] in seen:
                seen_neighbors.add(grid[a - 1][b])
            if b - 1 >= 0 and grid[a][b - 1] in seen:
                seen_neighbors.add(grid[a][b - 1])
            print(grid[i][j], seen_neighbors)
            ans = (ans * (3 - len(seen_neighbors))) % MOD
            seen.add(grid[i][j])

    print_(f"{ans}\n")


if __name__ == '__main__':
    solve()
