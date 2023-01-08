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
    n, k = read_ints()
    bin_seq = read_line()
    zeros_pref = [0]
    ones_ps = [0]
    i = 0
    while i < n:
        zero = 0
        one = 0
        while i < n and bin_seq[i] == '0':
            zero += 1
            i += 1
        zeros_pref.append(zeros_pref[-1] + zero)
        while i < n and bin_seq[i] == '1':
            one += 1
            i += 1
        ones_ps.append(ones_ps[-1] + one)

    ans = 0

    def get_value(array, index):
        return 0 if index < 0 else array[index]
    for i in range(1, len(zeros_pref)):
        ans = max(ans, zeros_pref[i] - get_value(zeros_pref, i - k) + ones_ps[i] - get_value(ones_ps, i - k - 1))

    print_(f"{ans}\n")


if __name__ == '__main__':
    solve()
