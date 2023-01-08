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
    s1, s2, s3 = read_strings()
    t1, t2, t3 = read_strings()

    ordered = int(s1 == t1) + int(s2 == t2) + int(s3 == t3)

    print('No' if ordered == 1 else 'Yes')


if __name__ == '__main__':
    solve()
