from typing import List
import sys

sys.stdin = open("day6.in", "r")
sys.stdout = open("day6.out", "w")

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
    signal = read_line()
    ans1 = -1
    ans2 = -1
    for i in range(4, len(signal)):
        if len(set(signal[i - 4:i])) == 4 and ans1 == -1:
            ans1 = i
        if i >= 14 and len(set(signal[i - 14:i])) == 14:
            ans2 = i
            break

    print(f"Part 1: {ans1}")
    print(f"Part 2: {ans2}")


if __name__ == '__main__':
    solve()
