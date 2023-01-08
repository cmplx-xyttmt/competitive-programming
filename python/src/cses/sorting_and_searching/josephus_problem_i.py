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
    seen = set()
    ans = []
    skipped = 0
    while len(seen) < n:
        for i in range(1, n + 1):
            if i not in seen:
                if skipped:
                    ans.append(i)
                    seen.add(i)
                    skipped = 0
                else:
                    skipped = 1
    print_(f"{' '.join(map(str, ans))}\n")


if __name__ == '__main__':
    solve()
