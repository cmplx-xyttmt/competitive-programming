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


def reverse_int(num):
    return int(''.join(reversed(str(num))))


def get_min(num):
    rev = reverse_int(num)
    rev2 = reverse_int(rev)
    return min(num, rev, rev2)


def solve():
    n, k = read_ints()
    if k != get_min(k):
        print_(f"0\n")
        return
    ans = 0
    rev = reverse_int(k)
    equal = rev == k
    while k <= n:
        ans += 1
        k *= 10
    if not equal:
        while rev <= n:
            ans += 1
            rev *= 10
    print_(f"{ans}\n")


if __name__ == '__main__':
    solve()
