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
    h, w = read_ints()
    a = [read_ints() for _ in range(h)]
    b = [[a[i][j] for i in range(h)] for j in range(w)]
    ans = '\n'.join(map(lambda row: ' '.join(map(str, row)), b))
    print_(ans)


if __name__ == '__main__':
    solve()
