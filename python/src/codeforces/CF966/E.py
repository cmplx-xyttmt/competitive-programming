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
    # for each cell, we want to find out how many k x k grids it belongs to.
    #   xxxxx
    #   xxxxx
    #   xxxxx
    #   xxxxx
    #   a, b
    #   min(a, k), min(b, k)
    # start with a = k..n, b = k..m  (n - k + 1) * (m - k + 1)
    # then a = k - 1, b = k..m  (m - k + 1)
    # then a = k..n, b = k - 1  (n - k + 1)
    # a = k, b = k - 1
    # a = k - 1, b = k - 1
    # k, k - 1
    # k - 1, k
    # k, k - 2
    # k - 2, k
    # k - 1, k - 1

    t = read_int()
    for _ in range(t):
        n, m, k = read_ints()
        w = read_int()
        a = read_ints()
        a.sort(reverse=True)
        i = 0
        spectacle = 0
        for x in range(k - 1, n):
            if i < w:
                for y in range(k - 1, m):
                    print(x, y)
                    if i < w:
                        spectacle += a[i] * k * k
                        i += 1
                    else:
                        break

        diff = 1
        while i < w:
            for diffx in range(diff + 1):
                diffy = diff - diffx
                print(k - diffx - 1, k - diffy - 1)
                if i < w:
                    spectacle += a[i] * (k - diffx) * (k - diffy)
                    i += 1
                else:
                    break
            diff += 1
        print_(f"{spectacle}\n")


if __name__ == '__main__':
    solve()
