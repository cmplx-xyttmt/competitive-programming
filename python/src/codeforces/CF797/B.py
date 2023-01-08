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
        b = read_ints()
        diffs = []
        zeros = []
        for i in range(n):
            if b[i] > 0:
                diffs.append(a[i] - b[i])
            else:
                zeros.append(a[i])

        diff = diffs[0] if diffs else float('inf')
        can = diff >= 0 and all([d == diff for d in diffs]) and (len(zeros) == 0 or max(zeros) <= diff)

        print_(f"{'YES' if  can else 'NO'}\n")


if __name__ == '__main__':
    solve()
