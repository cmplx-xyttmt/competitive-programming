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
    t = read_int()
    for case in range(t):
        n, k = read_ints()
        e = read_ints()
        s = sum(e)
        sq_s = sum([a ** 2 for a in e])
        if s == 0 and sq_s == 0:
            print_(f"Case #{case + 1}: 1\n")
            continue
        num = sq_s - s ** 2
        if s == 0:
            res = int(1e18) + 1
        else:
            res = num // (2 * s)
        if (s != 0 and num % (2 * s) == 0) and abs(res) <= int(1e18):
            print_(f"Case #{case + 1}: {res}\n")
        else:
            print_(f"Case #{case + 1}: IMPOSSIBLE\n")


if __name__ == '__main__':
    solve()
