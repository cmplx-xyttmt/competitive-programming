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


def repeat_twice(left, right):
    mul = 10
    lower = 1
    upper = 9
    repeats = []
    while (lower * mul + lower) <= right:
        # smallest = (lower * mul + lower)
        # largest = (upper * mul + upper)
        for num in range(lower, upper + 1):
            repeat_number = num * mul + num
            if left <= repeat_number <= right:
                repeats.append(repeat_number)
        mul *= 10
        lower = mul // 10
        upper = mul - 1
    return repeats


def repeat_multiple_times(left, right):
    #      1                         2                            3
    # 2 -> 10x + x                   100x + x
    # 3 -> 100x + 10x + x            10000x + 100x + 10x
    # 4 -> 1000x + 100x + 10x + x    1000000x + 10000x + 100x + x
    pass


def solve():
    line = read_line()
    ranges = line.split(",")
    ranges = list(map(lambda rge: list(map(int, rge.split("-"))), ranges))
    part1 = 0
    for rge in ranges:
        repeats = repeat_twice(rge[0], rge[1])
        part1 += sum(repeats)
    print(part1)


if __name__ == '__main__':
    solve()
