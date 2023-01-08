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
    n, x, m = read_ints()
    f = [x]
    seen = {x: 0}
    x = (x ** 2) % m
    idx = 1
    while x not in seen:
        f.append(x)
        seen[x] = idx
        x = (x ** 2) % m
        idx += 1
    rep_idx = seen[x]
    for i in range(1, len(f)):
        f[i] += f[i - 1]

    if rep_idx >= n:
        print_(f"{f[n - 1]}\n")
    else:
        ans = 0 if rep_idx == 0 else f[rep_idx - 1]
        q, r = divmod(n - rep_idx, len(f) - rep_idx)
        ans = ans + q * (f[-1] - ans) + (0 if r == 0 else (f[rep_idx + r - 1] - ans))
        print_(f"{ans}\n")


if __name__ == '__main__':
    solve()
