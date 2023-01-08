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
    intervals = []
    for _ in range(n):
        l, r = read_ints()
        intervals.append((l, r))
    intervals.sort()
    x, y = intervals[0]
    ans = []

    for i in range(1, n):
        l, r = intervals[i]
        if l > y:
            ans.append(f"{x} {y}")
            x, y = l, r
        else:
            y = max(r, y)
    ans.append(f"{x} {y}")
    pnt = '\n'.join(ans)
    print_(f"{pnt}\n")


if __name__ == '__main__':
    solve()
