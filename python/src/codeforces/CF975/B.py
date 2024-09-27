from collections import defaultdict
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
        n, q = read_ints()
        x = read_ints()
        counts = defaultdict(int)
        for i in range(n):
            # 0 1 2 3
            cnt = i * (n - i) + n - i - 1
            counts[cnt] += 1
            if i < n - 1:
                cnt_btn = (i + 1) * (n - i - 1)
                counts[cnt_btn] += (x[i + 1] - x[i] - 1)
        ans = map(lambda k: str(counts[k]), read_ints())
        print_(f"{' '.join(ans)}\n")


if __name__ == '__main__':
    solve()
