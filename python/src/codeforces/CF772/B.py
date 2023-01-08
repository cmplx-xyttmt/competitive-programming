from typing import List
import sys

input_ = sys.stdin.readline
print_ = sys.stdout.write
flush = sys.stdout.flush


def readline() -> str:
    return input_().strip()


def read_int() -> int:
    return int(readline())


def read_strings() -> List[str]:
    return list(readline().split())


def read_ints():
    return list(map(int, readline().split()))


def solve():
    t = read_int()

    for _ in range(t):
        n = read_int()
        a = read_ints() + [0]
        ops = 0
        for i in range(2, n):
            if a[i - 2] < a[i - 1] and a[i - 1] > a[i]:
                a[i] = max(a[i - 1], a[i + 1])
                ops += 1

        print_(f"{ops}\n")
        print_(f"{' '.join(map(str, a[:-1]))}\n")


if __name__ == '__main__':
    solve()
