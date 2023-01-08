from typing import List
import sys

sys.stdin = open("measurement.in", "r")
sys.stdout = open("measurement.out", "w")

input_ = sys.stdin.readline
print_ = sys.stdout.write
flush = sys.stdout.flush


def readline() -> str:
    return input_().strip()


def read_int() -> int:
    return int(readline())


def read_strings() -> List[str]:
    return list(readline().split())


def read_ints():
    return list(map(int, readline().split()))


class Measurement:

    def __init__(self, day, cow_name, change):
        self.day = int(day)
        self.cow_name = cow_name
        sign, value = change[0], int(change[1:])
        self.change = value if sign == '+' else -value


def solve():
    n = read_int()
    measurements = []
    curr_top = {'Mildred', 'Elsie', 'Bessie'}
    output = {
        'Mildred': 7,
        'Elsie': 7,
        'Bessie': 7
    }

    for _ in range(n):
        day, cow_name, change = read_strings()
        measurements.append(Measurement(day, cow_name, change))

    measurements.sort(key=lambda m: m.day)

    change_display = 0

    for m in measurements:
        output[m.cow_name] += m.change
        best = max(output.values())
        new_top = {cow_name for cow_name in output.keys() if output[cow_name] == best}
        if new_top != curr_top:
            change_display += 1
        curr_top = new_top

    print_(f"{change_display}\n")


if __name__ == '__main__':
    solve()
