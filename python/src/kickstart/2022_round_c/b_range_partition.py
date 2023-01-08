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

    for test in range(1, t + 1):
        n, x, y = read_ints()
        s = (n * (n + 1))//2
        numerator = s * min(x, y)
        if numerator % (x + y) == 0:
            needed = numerator // (x + y)
        else:
            print_(f"Case #{test}: IMPOSSIBLE\n")
            continue

        ans = []
        if x > y:
            needed = s - needed
        n = min(needed, n)
        while needed > 0:
            needed -= n
            ans.append(n)
            n = min(needed, n - 1)
        # print("Sum: ", sum(ans))

        print_(f"Case #{test}: POSSIBLE\n")
        print_(f"{len(ans)}\n")
        print_(f"{' '.join(map(str, ans))}\n")


if __name__ == '__main__':
    solve()
