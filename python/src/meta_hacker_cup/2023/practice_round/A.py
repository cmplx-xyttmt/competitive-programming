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


def calc_k(s, A, B, C):
    return ((B - 2 * A) * s + 2 * C) / B


def analyze(A, B, C, config="random"):
    print(f"======{config}========")
    max_s = C // A
    for s in range(max_s + 1):
        expected_k = calc_k(s, A, B, C)
        d = (C - s * A) // B
        actual_k = 2 * d - 1 if s == 0 else s + 2 * d
        print(f"s: {s}, d: {d}, expected_k: {expected_k}, actual_k: {actual_k}")


def solve():
    # k-decker burger:
    #  k + 1 buns
    #  k cheese
    #  k pattie
    #  S -> 2 buns, 1 cheese, 1 pattie
    #  D -> 2 buns, 2 cheese, 2 patties
    t = read_int()
    for case in range(1, t + 1):
        s, d, k = read_ints()
        buns_available = 2 * (s + d)
        cheese_available = pattie_available = s + 2 * d

        needed_buns = k + 1
        needed_pattie = needed_cheese = k
        can_make = buns_available >= needed_buns and cheese_available >= needed_cheese and pattie_available >= needed_pattie
        print_(f"Case #{case}: {'YES' if can_make else 'NO'}\n")

        # s * A + d * B <= C
        # d = floor((C - s * A)/B)  s ranges between 0 and floor(C / A)
        # 2s + 2d  k = s + 2d
        # if s == 0: k = 2d - 1
        # else: k = s + 2d
        # 2 3 5
        # s = 0, d = 1, k = 1
        # s = 1, d = 1, k = 1 + 2
        # s = 2, d = 0, k = 2
        # k = s + 2(C - A*s)/B
        # k = (B*s + (C - A*s) ) / B
        # if B < A, set s = 0
        # else:
        # k = ((B - 2A) * s + 2C) / B
        # if B >= 2A, set d = 0
        # if B <= A, set s = 0


if __name__ == '__main__':
    # solve()
    analyze(7, 7, 30, "equal")
    analyze(4, 7, 30, "B = 2 * A - 1")
    analyze(3, 7, 30, "B = 2 * A + 1")
    analyze(2, 7, 30, "B = 3 * A + 1")
    analyze(8, 7, 30, "B = A - 1")
    analyze(5, 10, 30, "B = 2 * A")
    analyze(5, 6, 30, "B = A + 1")
    analyze(5, 7, 30, "B = A + 2")
    analyze(5, 8, 30, "B = A + 3")
    analyze(5, 8, 100, "big number")
