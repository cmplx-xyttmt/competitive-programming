from typing import Callable
import sys


sys.stdin = open("cowsignal.in", "r")
sys.stdout = open("cowsignal.out", "w")


input_: Callable[[int], str] = sys.stdin.readline
print_: Callable[[str], int] = sys.stdout.write
flush: Callable[[None], None] = sys.stdout.flush


def solve():
    m, n, k = map(int, input_().strip().split())

    grid = [input_().strip() for _ in range(m)]
    ans = []
    for i in range(m):
        ans.append([])
        for j in range(n):
            ans[-1].append(grid[i][j] * k)
        # sys.stderr.write(f"{i} -> {ans[i]}\n")
        for rep in range(1, k):
            ans.append(ans[-1])
    # sys.stderr.write(f"{ans}")
    print_("\n".join(map(lambda row: "".join(row), ans)))
    print_("\n")


if __name__ == '__main__':
    solve()
