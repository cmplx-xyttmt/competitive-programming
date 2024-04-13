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


def get_power_of_2(l, R):
    two_i = 1
    while l % two_i == 0 and two_i * (l // two_i + 1) <= R:
        two_i *= 2
    return two_i // 2


def solve():
    # Greedy approach: always take the biggest power of 2 that divides l, without exceeding R
    # at the end, get as close as possible to the even number that ends the sequence
    L, R = read_ints()
    two_i = get_power_of_2(L, R)
    l = L
    r = two_i * (l // two_i + 1)
    division = [(l, r)]
    while r < R:
        l = r
        two_i = get_power_of_2(l, R)
        r = two_i * (l // two_i + 1)
        division.append((l, r))
    print_(f"{len(division)}\n")
    ans = '\n'.join(map(lambda tup: f'{tup[0]} {tup[1]}', division))
    print_(f"{ans}\n")


if __name__ == '__main__':
    solve()
