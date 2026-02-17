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
    longer = read_line()
    shorter = read_line()
    # while longer[0..i] == shorter[0..i] check if longer[i + 1..n] == shorter[i..n]
    suffix_equal = [False] * len(longer)
    prev_true = True
    last = len(longer) - 1
    while last > 0:
        if prev_true and longer[last] == shorter[last - 1]:
            suffix_equal[last] = True
            prev_true = True
        else:
            break
        last -= 1

    first = 0
    positions = []
    if suffix_equal[1]:
        positions.append(1)

    while first < len(shorter) and longer[first] == shorter[first]:
        if (first + 2 < len(longer) and suffix_equal[first + 2]) or first == len(shorter) - 1:
            positions.append(first + 2)
        first += 1
    print(f"{len(positions)}")
    print(" ".join(map(str, positions)))


if __name__ == '__main__':
    solve()
