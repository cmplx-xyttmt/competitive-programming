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


def num_of_triangles(lines):
    first = lines // 3
    rem = lines - 3 * first
    second = first + (1 if rem == 2 else 0)
    third = first + (1 if rem >= 1 else 0)

    return third * 2 * (first + second) + 2 * second * first


def solve():
    t = read_int()
    for _ in range(t):
        n = read_int()
        low = 1
        high = n + 1
        while high - low > 1:
            mid = (low + high) // 2
            # print(mid, num_of_triangles(mid))
            if num_of_triangles(mid) >= n:
                high = mid
            else:
                low = mid
        print_(f"{high}\n")


if __name__ == '__main__':
    solve()
