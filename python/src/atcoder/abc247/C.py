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
    n = read_int()
    sequences = [[], ['1']]
    for i in range(2, n + 1):
        sequences.append(sequences[i - 1] + [str(i)] + sequences[i - 1])

    ans = " ".join(sequences[n])
    print_(f"{ans}\n")


if __name__ == '__main__':
    solve()
