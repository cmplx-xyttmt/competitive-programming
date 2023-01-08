from typing import List
import sys

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


# def xor(upto):
#     if upto < 4:
#         return [0, 1, 3, 0][upto]
#
#     pow_2 = 1
#     while pow_2 * 2 <= upto:
#         pow_2 *= 2
#
#     return pow_2 ^ ((pow_2 if (upto - pow_2) % 2 == 1 else 0) + xor(upto - pow_2))


def other_xor(upto):
    return [upto, 1, upto + 1, 0][upto % 4]


# def brute(upto):
#     res = 0
#     for i in range(upto + 1):
#         res ^= i
#
#     return res


def solve():
    a, b = read_ints()
    print_(f"{(0 if a == 0 else other_xor(a - 1)) ^ other_xor(b)}\n")
    # for i in range(100):
    #     print(i, xor(i), brute(i))


if __name__ == '__main__':
    solve()
