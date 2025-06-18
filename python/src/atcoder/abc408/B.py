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
    a = list(set(read_ints()))
    a.sort()
    print(len(a))
    a = [str(num) for num in a]
    print(f"{' '.join(a)}")


if __name__ == '__main__':
    solve()
