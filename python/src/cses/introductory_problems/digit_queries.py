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
    q = read_int()
    for _ in range(q):
        k = read_int()
        total_digits = 0
        digits = 0
        pow_10 = 1
        pow_10_prev = 0
        new_digits = (pow_10 - pow_10_prev) * digits
        while total_digits + new_digits < k:
            total_digits += new_digits
            digits += 1
            pow_10_prev = pow_10
            pow_10 *= 10
            new_digits = (pow_10 - pow_10_prev) * digits
        c, rem = divmod(k - total_digits, digits)
        c = (c + 1) if rem else c
        # print(c)
        rem = (k - total_digits) % digits
        # print(pow_10_prev, c, total_digits)
        print_(f"{str(pow_10_prev + c - 1)[(rem + digits - 1) % digits]}\n")


if __name__ == '__main__':
    solve()
