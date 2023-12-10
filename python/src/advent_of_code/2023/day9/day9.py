from typing import List, Tuple
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


def extrapolate(sequence: List[int]) -> Tuple[int, int]:
    next_val = sequence[-1]
    prev_value = sequence[0]
    mul = -1
    while True:
        diff_array = []
        all_0 = True
        for i in range(1, len(sequence)):
            diff_array.append(sequence[i] - sequence[i - 1])
            if diff_array[-1] != 0:
                all_0 = False
        if all_0:
            break
        next_val += diff_array[-1]
        prev_value += (mul * diff_array[0])
        mul *= -1
        sequence = diff_array
    return next_val, prev_value


def solve():
    line = read_line()
    sequences = []
    while line:
        sequence = list(map(int, line.split()))
        sequences.append(sequence)
        line = read_line()

    extrapolate_results = list(map(extrapolate, sequences))
    ans1 = sum(map(lambda res: res[0], extrapolate_results))
    print(f"Part 1: {ans1}")

    ans2 = sum(map(lambda res: res[1], extrapolate_results))
    print(f"Part 2: {ans2}")


if __name__ == '__main__':
    solve()
