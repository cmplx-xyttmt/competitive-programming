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
        a, b, c, d = read_ints()
        s = read_line()
        n = len(s)
        a_count = s.count('A')
        b_count = s.count('B')
        if a_count != (a + c + d) or b_count != (b + c + d):
            print_("NO\n")
            continue
        ab_indices = []
        skip = True
        for i in range(n - 1):
            if skip:
                skip = False
                continue
            if s[i:i+2] == 'AB':
                skip = True
                if i + 3 <= n and s[i:i + 3] == 'ABA':
                    if i + 4 <= n and s[i:i + 3] == 'ABAB':
                        ab_indices.append(1)
                    else:
                        ab_indices.append(0)


if __name__ == '__main__':
    solve()
