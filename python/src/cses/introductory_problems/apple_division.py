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
    n = read_int()
    p = read_ints()
    total = sum(p)
    min_diff = int(1e18)
    for mask in range(1 << n):
        mask_sum = 0
        for j in range(n):
            if (1 << j) & mask:
                mask_sum += p[j]
        other_sum = total - mask_sum
        min_diff = min(abs(mask_sum - other_sum), min_diff)
    print_(f"{min_diff}\n")


if __name__ == '__main__':
    solve()
