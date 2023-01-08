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
    x = [0] + read_ints()
    c = [0] + read_ints()
    seen = [0 for _ in range(n + 1)]
    ans = 0
    for i in range(1, n + 1):
        if seen[i]:
            continue
        seen[i] = 1
        j = x[i]
        new = set()
        new.add(i)
        while seen[j] == 0:
            new.add(j)
            seen[j] = 1
            j = x[j]
        if seen[j] == 1:
            k = x[j]
            cost = c[j]
            while k != j:
                cost = min(c[k], cost)
                k = x[k]
            ans += cost
        for k in new:
            seen[k] = 2
    print_(f"{ans}\n")


if __name__ == '__main__':
    solve()
