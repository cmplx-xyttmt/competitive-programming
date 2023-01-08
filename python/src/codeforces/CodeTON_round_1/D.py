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
        if n % 2 == 1:
            print_("2\n")
            continue
        ans = -1
        for i in range(3, n):
            if (i * (i - 1))//2 >= n:
                break
            # print(n, i)
            if i % 2 != 0 and n % i == 0:
                ans = i
                break

        print_(f"{ans}\n")


if __name__ == '__main__':
    solve()
