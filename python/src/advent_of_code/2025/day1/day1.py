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
    dial = 50
    line = read_line()
    zeros = 0
    zeros2 = 0
    while line:
        direction, distance = line[0], int(line[1:])
        if direction == 'L':
            if distance >= dial:
                rem = distance - dial
                if dial != 0:
                    zeros2 += 1
            else:
                rem = 0
            zeros2 += rem // 100
            # print(f"{dial} {direction}{distance} -> {rem} {zeros2}")
            dial = (100 + dial - distance) % 100
        else:
            if distance >= (100 - dial):
                rem = distance - (100 - dial) % 100
                if dial != 0:
                    zeros2 += 1
            else:
                rem = 0
            zeros2 += rem // 100
            # print(f"{dial} {direction}{distance} -> {rem} {zeros2}")
            dial = (dial + distance) % 100
        if dial == 0:
            zeros += 1
        line = read_line()
    print(f"Part 1: {zeros}")
    print(f"Part 2: {zeros2}")


if __name__ == '__main__':
    solve()
