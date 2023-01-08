from collections import defaultdict
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
    board = []
    board_size = 8
    for _ in range(board_size):
        board.append(list(read_line()))

    rows = [False] * board_size
    cols = [False] * board_size
    diagonals = [False] * (board_size * 2 - 1)
    antidiagonals = defaultdict(bool)

    def place_queens(row):
        if row == board_size:
            return 1
        ways = 0
        for col in range(board_size):
            if board[row][col] == '.':
                diag = row + col
                antidiag = row - col
                if not (rows[row] or cols[col] or diagonals[diag] or antidiagonals[antidiag]):
                    # place queen
                    rows[row] = cols[col] = diagonals[diag] = antidiagonals[antidiag] = True
                    ways += place_queens(row + 1)
                    # remove queen
                    rows[row] = cols[col] = diagonals[diag] = antidiagonals[antidiag] = False
        return ways

    print_(f"{place_queens(0)}\n")


if __name__ == '__main__':
    solve()
