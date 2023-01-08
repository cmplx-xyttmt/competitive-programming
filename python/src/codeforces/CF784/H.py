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
        n, k = read_ints()
        a = read_ints()
        required = [0 for _ in range(31)]
        for num in a:
            for i in range(30, -1, -1):
                if num & (1 << i) == 0:
                    required[i] += 1

        to_set = []
        for i in range(30, -1, -1):
            if k >= required[i]:
                to_set.append(i)
                k -= required[i]

        ans = (1 << 31) - 1
        for num in a:
            new_num = num
            for i in to_set:
                new_num = new_num | (1 << i)
            ans = ans & new_num

        print_(f"{ans}\n")


if __name__ == '__main__':
    solve()
