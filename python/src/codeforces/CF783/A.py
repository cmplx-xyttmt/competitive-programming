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
        n, m = read_ints()
        # print("params: ", n, m)
        if min(n, m) == 1:
            # print("params 2: ", n, m)
            if max(n, m) == 1:
                print_(f"0\n")
            elif max(n, m) == 2:
                print_(f"1\n")
            else:
                print_(f"-1\n")
        else:
            rem = max(n, m) - min(n, m)
            # print("rem: ", rem)
            ans = 2 * min(n - 1, m - 1) + 1
            if rem % 2 == 0:
                ans += rem * 2 - 1
            else:
                ans += (rem - 1) * 2
            print_(f"{ans}\n")


if __name__ == '__main__':
    solve()
