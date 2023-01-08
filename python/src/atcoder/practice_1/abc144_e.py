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


def can(target_ans, k, a, f):
    training = 0
    for i in range(len(a)):
        val = target_ans // f[i]
        training += max(0, a[i] - val)
    return training <= k


def solve():
    n, k = read_ints()
    a = read_ints()
    f = read_ints()
    a.sort(reverse=True)
    f.sort()
    lo, hi = -1, max([a[i] * f[i] for i in range(n)])

    while hi - lo > 1:
        mid = (hi + lo) // 2
        if can(mid, k, a, f):
            hi = mid
        else:
            lo = mid

    print_(f"{hi}\n")


if __name__ == '__main__':
    solve()
