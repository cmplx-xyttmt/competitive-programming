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
    n, x = read_ints()
    reach = [False for _ in range(x + 1)]
    reach[0] = True
    for _ in range(n):
        a, b = read_ints()
        new_reach = [False for _ in range(x + 1)]
        for i in range(x + 1):
            if reach[i]:
                if i + a <= x:
                    new_reach[i + a] = True
                if i + b <= x:
                    new_reach[i + b] = True
        reach = new_reach
    print("Yes" if reach[x] else "No")


if __name__ == '__main__':
    solve()
