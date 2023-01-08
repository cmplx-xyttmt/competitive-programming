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
    s = read_line()
    n = len(s)
    k = read_int()
    candidates = set()
    for i in range(n):
        for j in range(1, k + 1):
            if i + j > n:
                break
            candidates.add(s[i:i + j])

    candidates = list(candidates)
    candidates.sort()
    # print(candidates)
    print(candidates[k - 1])


if __name__ == '__main__':
    solve()
