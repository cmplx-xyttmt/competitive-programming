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


def solve_case() -> int:
    s = read_int()
    for _ in range(s):
        readline()

    q = read_int()
    seen_engines = set()
    switches = 0
    for _ in range(q):
        engine = readline()
        seen_engines.add(engine)
        if len(seen_engines) == s:
            switches += 1
            seen_engines = {engine}

    return switches


def solve():
    t = read_int()

    for test in range(t):
        print_(f"Case #{test + 1}: {solve_case()}\n")


if __name__ == '__main__':
    solve()
