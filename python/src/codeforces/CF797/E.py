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
        a = read_ints()
        ans = 0
        rems = []
        for i in range(n):
            ans += a[i] // k
            rems.append(a[i] % k)
        rems.sort(reverse=True)
        i, j = 0, n - 1
        while i < j:
            while i < j and rems[i] + rems[j] < k:
                j -= 1
            if i < j:
                ans += 1
                j -= 1
            i += 1
        print_(f"{ans}\n")


if __name__ == '__main__':
    solve()
