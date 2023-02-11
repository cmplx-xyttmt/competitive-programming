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
    n, q = read_ints()
    a = [i + 1 for i in range(n)]
    index = dict()
    for i, num in enumerate(a):
        index[num] = i

    for _ in range(q):
        x = read_int()
        idx = index[x]
        nxt = idx + 1 if idx < n - 1 else idx - 1
        y = a[nxt]
        index[x], index[y] = nxt, idx
        a[idx] = y
        a[nxt] = x

    ans = ' '.join(map(str, a))
    print_(f"{ans}\n")


if __name__ == '__main__':
    solve()
