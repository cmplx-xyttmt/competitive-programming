from typing import List
import sys

sys.stdin = open("tttt.in", "r")
sys.stdout = open("tttt.out", "w")

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


def get_rows_and_diags(grid):
    ret = []
    for i in range(3):
        ret.append(set(grid[i]))
        ret.append(set([grid[j][i] for j in range(3)]))
    ret.append(set([grid[i][i] for i in range(3)]))
    ret.append(set(grid[i][2 - i] for i in range(3)))
    return ret


def individual_win(letter, rows_and_diags):
    for row in rows_and_diags:
        if letter in row and len(row) == 1:
            return 1

    return 0


def cow_team_win(first, second, rows_and_diags):
    for row in rows_and_diags:
        if first in row and second in row and len(row) == 2:
            return 1
    return 0


def solve():
    grid = []
    for _ in range(3):
        grid.append(list(readline()))

    rows_and_diags = get_rows_and_diags(grid)

    indie = sum([individual_win(chr(ord('A') + letter), rows_and_diags) for letter in range(26)])
    team = sum([cow_team_win(chr(ord('A') + first), chr(ord('A') + second), rows_and_diags)
                for first in range(26) for second in range(first + 1, 26)])

    print_(f"{indie}\n{team}\n")


if __name__ == '__main__':
    solve()
