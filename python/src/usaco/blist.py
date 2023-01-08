from typing import List
import sys

sys.stdin = open("blist.in", "r")
sys.stdout = open("blist.out", "w")

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
    n = read_int()
    times = []  # (time, buckets, starting)
    for _ in range(n):
        start, end, buckets = read_ints()
        times.append((start, buckets, True))
        times.append((end, buckets, False))

    times.sort()
    available_buckets, total_buckets = 0, 0
    for time, buckets, starting in times:
        if starting:
            if available_buckets < buckets:
                available_buckets, total_buckets = 0, total_buckets + buckets - available_buckets
            else:
                available_buckets -= buckets
        else:
            available_buckets += buckets

    print_(f"{total_buckets}\n")


if __name__ == '__main__':
    solve()
