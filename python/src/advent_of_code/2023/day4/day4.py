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
    line = read_line()
    ans1 = 0
    ans2 = 0
    copies = defaultdict(lambda: 1)
    card_no = 1
    while line:
        _, numbers = line.split(":")
        winning_nums_str, my_nums_str = numbers.split("|")
        winning_nums = set(map(int, winning_nums_str.strip().split()))
        my_nums = set(map(int, my_nums_str.strip().split()))
        intersection = winning_nums.intersection(my_nums)
        ans2 += copies[card_no]
        if len(intersection) > 0:
            point_value = 2 ** (len(intersection) - 1)
            ans1 += point_value
            print_(f"{card_no} ({copies[card_no]}) -> ")
            for next_card in range(card_no + 1, card_no + len(intersection) + 1):
                print_(f" {next_card}")
                copies[next_card] += copies[card_no]
            print_("\n")
        line = read_line()
        card_no += 1
    print(f"Part 1: {ans1}")
    print(f"Part 2: {ans2}")


if __name__ == '__main__':
    solve()
