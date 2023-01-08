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
        w = read_ints()
        prefix = 0
        suffix = 0
        alice = dict()
        bob = dict()
        alice[0] = -1
        bob[0] = n
        ans = 0
        for i in range(n):
            j = n - i - 1
            prefix += w[i]
            suffix += w[j]
            alice[prefix] = i
            bob[suffix] = j

        for prefix, i in alice.items():
            if prefix in bob:
                j = bob[prefix]
                if i < j:
                    ans = max(ans, i + 1 + n - j)

        print_(f"{ans}\n")


if __name__ == '__main__':
    solve()
