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
    s = read_line()
    sequence = [-1] * (n + 1)
    left, right = 0, n
    for i in range(n):
        if s[i] == 'L':
            sequence[right] = i
            right -= 1
        else:
            sequence[left] = i
            left += 1
    assert left == right
    sequence[left] = n
    print_(f"{' '.join(map(str, sequence))}\n")


if __name__ == '__main__':
    solve()
