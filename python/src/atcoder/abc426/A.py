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
    oses = {
        "Ocelot": 1,
        "Serval": 2,
        "Lynx": 3
    }
    x, y = read_strings()
    print("Yes" if oses[x] >= oses[y] else "No")


if __name__ == '__main__':
    solve()
