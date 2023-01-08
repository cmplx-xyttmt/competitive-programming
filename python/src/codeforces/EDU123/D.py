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


def solve():
    t = read_int()
    MOD = 998244353

    for _ in range(t):
        n, m, k, q = read_ints()
        queries = []
        for _ in range(q):
            x, y = read_ints()
            queries.append((x, y))

        seen_rows = set()
        seen_cols = set()
        groups = 0
        for (r, c) in queries[::-1]:
            seen = (r in seen_rows and c in seen_cols) or len(seen_cols) == m or len(seen_rows) == n
            if not seen:
                groups += 1
            seen_rows.add(r)
            seen_cols.add(c)

        ans = 1
        for _ in range(groups):
            ans = (k * ans) % MOD
        print(ans)


if __name__ == '__main__':
    solve()
