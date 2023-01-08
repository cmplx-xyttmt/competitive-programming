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
        s = read_ints()
        f = read_ints()
        durations = []
        for i in range(n):
            if i == 0:
                durations.append(f[i] - s[i])
            else:
                start = max(f[i - 1], s[i])
                durations.append(f[i] - start)

        print_(f"{' '.join(map(str, durations))}\n")


if __name__ == '__main__':
    solve()
