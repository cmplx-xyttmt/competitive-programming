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
    # first idea:
    # 010 -> change the ends to 0, then change all the middles to 1.  0100110010
    # 01 -> change first ones to 0, then starting at the next 1, change all after that to 1.
    # 10 -> change first zeros to 1, then starting at the next 0, change all after that to 0. e.g 01001010
    # 0 -> change all 1s to 0
    # 1 -> change all zeros to 1
    # second idea:
    # for 01 and 10, just choose the best pivot i where s[<i] = 0 or 1 and s[>=i] = 1
    # for each i, keep track of how many 1s are to the left
    # 0100110010
    # ones ->            0  1 1 1 2  3 3 3 4 4
    # j - 2 * ones[j] -> 0 -1 0 1 0 -1 0 1 0 1
    # 0100110010
    # for 010: for each index, calculate how many it will take to get the left to zero.
    # then calculate the index that minimizes future changes (how?)
    # we can generalize the whole thing by choosing the index where 1 will start:
    #       -> left of i has to be 0, easy to calculate changes needed: ones[i - 1]
    #       -> how far right to take the 1s?
    #       -> say we reach j, then ops = ones[n - 1] - ones[j] + j - i + 1 - ones[j] + ones[i - 1] = ones[n - 1] + ones[i - 1] - i + 1 - 2 * ones[j] + j
    #       -> we can precalculate j - 2 * ones[j] for each index, and then for each i, choose the minimum j.

    t = read_int()
    for _ in range(t):
        n = read_int()
        s = read_line()
        ones = [0 for _ in range(n)]
        for i in range(n):
            ones[i] = int(s[i] == '1')
            if i - 1 >= 0:
                ones[i] += ones[i - 1]

        # precalculate j - 2 * ones[j] because the minimum value determines where we'll stop the 1s.
        precalc = [j - 2 * one_count for j, one_count in enumerate(ones)]
        # minimum of precalc from the end of the array
        min_precalc = [0 for i in range(n)]
        curr_min = precalc[-1]
        for i in reversed(range(n)):
            curr_min = min(precalc[i], curr_min)
            min_precalc[i] = curr_min
        # print("ones: ", ones)
        # print("precalc: ", precalc)
        # print("min-precalc: ", min_precalc)

        all_zero_ops = ones[-1]
        all_one_ops = n - ones[-1]
        curr_best = min(all_one_ops, all_zero_ops)
        for i in range(n):
            prev_ones = 0 if i - 1 < 0 else ones[i - 1]
            ops = prev_ones
            ops += ones[n - 1] + prev_ones - i + 1 + min_precalc[i]
            # print(i, ops)
            curr_best = min(curr_best, ops)

        print(curr_best)


if __name__ == '__main__':
    solve()
