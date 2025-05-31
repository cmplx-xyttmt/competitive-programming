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
    S = read_line()
    # print(len(S) + sum([int(a) for a in S]))
    total_b_presses = 0
    moves = 0
    for digit in reversed(S):
        local_presses = (10 + int(digit) - total_b_presses) % 10
        moves += 1 + local_presses
        total_b_presses = (total_b_presses + local_presses) % 10

    print(moves)


if __name__ == '__main__':
    solve()
