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
        n, k = read_ints()
        stripe = read_line()
        whites = [0]
        for c in stripe:
            if c == 'W':
                whites.append(1 + whites[-1])
            else:
                whites.append(whites[-1])
        ans = float('inf')
        for i in range(len(whites)):
            if i + k == len(whites):
                break
            ans = min(ans, whites[i + k] - whites[i])
        print_(f"{ans}\n")


if __name__ == '__main__':
    solve()
