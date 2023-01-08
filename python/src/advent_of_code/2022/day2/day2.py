from typing import List
import sys

sys.stdin = open("day2.in", "r")
sys.stdout = open("day2.out", "w")

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


scores = {'A': 1, 'B': 2, 'C': 3}
win_dict = {'A': 'C', 'B': 'A', 'C': 'B'}
lose_dict = {'A': 'B', 'B': 'C', 'C': 'A'}


def calc_score(opp, me):
    my_score = 0
    if opp == me:
        my_score += 3
    elif win_dict[opp] != me:
        my_score += 6
    return my_score


def solve():
    line = read_line()

    eq_dict = {'X': 'A', 'Y': 'B', 'Z': 'C'}

    my_score = 0
    elf_strat_score = 0
    while line:
        opp, me = line.split()
        elf = opp if me == 'Y' else (win_dict[opp] if me == 'X' else lose_dict[opp])
        me = eq_dict[me]
        my_score += scores[me] + calc_score(opp, me)
        elf_strat_score += scores[elf] + calc_score(opp, elf)
        line = read_line()

    print(f"Part 1: {my_score}")
    print(f"Part 2: {elf_strat_score}")


if __name__ == '__main__':
    solve()
