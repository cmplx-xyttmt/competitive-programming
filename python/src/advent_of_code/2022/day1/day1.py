from typing import List
import sys

sys.stdin = open("day1.in", "r")
sys.stdout = open("day1.out", "w")

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
    lines = open("day1.in", 'r').readlines()
    elves = [[]]
    for line in lines:
        if line == '\n':
            elves.append([])
        else:
            cals = int(line.strip())
            elves[-1].append(cals)

    total_cals = [sum(all_cals) for all_cals in elves]
    total_cals.sort(reverse=True)
    max_cals = total_cals[0]
    top_three = sum(total_cals[:3])
    print(max_cals)
    print(top_three)


if __name__ == '__main__':
    solve()
