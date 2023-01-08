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

    for _ in range(t):
        n = read_int()
        a = read_ints()
        s = sum(a)
        can = False
        for i in range(n):
            if (s - a[i]) % (n - 1) == 0 and (s - a[i]) // (n - 1) == a[i]:
                can = True
                break

        print_(f"{'YES' if can else 'NO'}\n")


if __name__ == '__main__':
    solve()
