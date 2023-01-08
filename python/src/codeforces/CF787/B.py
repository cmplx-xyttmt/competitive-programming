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
        ops = 0
        can = True
        for i in range(n - 2, -1, -1):
            while a[i] > 0 and a[i] >= a[i + 1]:
                a[i] //= 2
                ops += 1
            if a[i] == a[i + 1]:
                can = False
                break

        print_(f"{ops if can else -1}\n")


if __name__ == '__main__':
    solve()
