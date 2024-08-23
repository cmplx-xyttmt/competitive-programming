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
        a = read_ints()
        m = read_int()
        for _ in range(m):
            st = read_line()
            matches = len(st) == n
            if matches:
                mapping_s_to_a = dict()
                mapping_a_to_s = dict()
                for i, c in enumerate(st):
                    if c in mapping_s_to_a and mapping_s_to_a[c] != a[i]:
                        matches = False
                        break
                    if a[i] in mapping_a_to_s and mapping_a_to_s[a[i]] != c:
                        matches = False
                        break
                    mapping_s_to_a[c] = a[i]
                    mapping_a_to_s[a[i]] = c
            print_(f"{'YES' if matches else 'NO'}\n")


if __name__ == '__main__':
    solve()
