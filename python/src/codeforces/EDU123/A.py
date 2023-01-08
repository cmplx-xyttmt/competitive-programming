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
        s = readline()
        keys = set()
        can = True
        for c in s:
            if c in {'r', 'g', 'b'}:
                keys.add(c)
            if c == 'R' and 'r' not in keys:
                can = False
            if c == 'G' and 'g' not in keys:
                can = False
            if c == 'B' and 'b' not in keys:
                can = False
            if not can:
                break

        print("YES" if can else "NO")


if __name__ == '__main__':
    solve()
