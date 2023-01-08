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
    max_n = 4 * int(1e4)
    pal_ints = []
    for i in range(1, max_n + 1):
        if i == int(''.join(reversed(str(i)))):
            pal_ints.append(i)

    ways = [0 for _ in range(max_n + 1)]
    ways[0] = 1
    mod = int(1e9) + 7
    for pal in pal_ints:
        for num in range(1, max_n + 1):
            if num - pal >= 0:
                ways[num] = (ways[num] + ways[num - pal]) % mod

    t = read_int()
    for _ in range(t):
        n = read_int()
        print_(f"{ways[n]}\n")


if __name__ == '__main__':
    solve()
