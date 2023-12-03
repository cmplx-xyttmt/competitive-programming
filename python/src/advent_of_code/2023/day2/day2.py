from typing import List
from collections import defaultdict
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


colors = ["red", "green", "blue"]

def power_of_set(cube_sets_list):
    mins = [0, 0, 0]
    for cube_set in cube_sets_list:
        for i, color in enumerate(colors):
            mins[i] = max(mins[i], cube_set[color])
    return mins[0] * mins[1] * mins[2]


def is_game_possible(cube_sets_list, limits):
    for cube_set in cube_sets_list:
        for color in colors:
            if cube_set[color] > limits[color]:
                return False

    return True


def parse_game(line: str):
    game_id_str, cube_sets_str = line.split(":")
    game_id = int(game_id_str.split(" ")[-1])
    cube_sets_str_list = cube_sets_str.split(";")
    cube_sets_list = []
    for cube_set_str in cube_sets_str_list:
        colors_str_list = cube_set_str.split(",")
        cube_set = defaultdict(int)
        for color_str in colors_str_list:
            num, color = color_str.strip().split(" ")
            cube_set[color] = int(num)
        cube_sets_list.append(cube_set)

    return game_id, cube_sets_list


def solve():
    line = read_line()
    ans1 = 0
    ans2 = 0
    limits = {
        "red": 12,
        "green": 13,
        "blue": 14
    }
    while line:
        game_id, cube_sets_list = parse_game(line)
        if is_game_possible(cube_sets_list, limits):
            ans1 += game_id

        ans2 += power_of_set(cube_sets_list)
        line = read_line()
    print(f"Part 1: {ans1}")
    print(f"Part 2: {ans2}")


if __name__ == '__main__':
    solve()
