from functools import lru_cache
from typing import List, Tuple
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


def get_damage_counts(row: List[str]):
    curr_count = 0
    damages = []
    for c in row:
        if c == "#":
            curr_count += 1
        elif curr_count > 0:
            damages.append(curr_count)
            curr_count = 0

    if curr_count > 0:
        damages.append(curr_count)
    return tuple(damages)


def all_possibilities(row: List[str], expected_counts: Tuple, debug=False):
    if debug:
        print(row, expected_counts)
    unknown = 0
    for c in row:
        if c == "?":
            unknown += 1

    all_masks = 1 << unknown
    poss = 0
    for mask in range(all_masks):
        curr_empty = 0
        new_row = []
        for c in row:
            if c == "?":
                if (1 << curr_empty) & mask:
                    new_row.append("#")
                else:
                    new_row.append(".")
                curr_empty += 1
            else:
                new_row.append(c)
        if debug:
            print(new_row, get_damage_counts(new_row), expected_counts)
        if get_damage_counts(new_row) == expected_counts:
            poss += 1

    return poss

def all_possibilities_dp(row: List[str], expected_counts: Tuple):
    @lru_cache(maxsize=None)
    def dp(i: int, counts: Tuple, prev_char: str):
        # print(row, counts)
        if len(counts) > len(expected_counts):
            return 0
        if i == len(row):
            # print(row, counts)
            return int(len(counts) == len(expected_counts) and counts[-1] == expected_counts[-1])

        ans = 0
        new_counts = list(counts)
        if row[i] == '#' or row[i] == '?':
            if prev_char == '#':
                new_counts[-1] += 1
            else:
                new_counts.append(1)
            if len(expected_counts) >= len(new_counts) and new_counts[-1] <= expected_counts[len(new_counts) - 1]:
                ans += dp(i + 1, tuple(new_counts), '#')

        if row[i] == '.' or row[i] == '?':
            if len(counts) == 0 or counts[-1] == expected_counts[len(counts) - 1]:
                ans += dp(i + 1, counts, '.')

        return ans

    return dp(0, (), ".")


def solve():
    line = read_line()
    rows = []  # row, counts pairs
    while line:
        row, counts = line.split()
        counts = tuple(map(int, counts.split(",")))
        rows.append((list(row), counts))
        line = read_line()

    # print(all_possibilities(rows[0][0], rows[0][1], debug=True))
    # print(f"Part 1: {sum(map(lambda r: all_possibilities(r[0], r[1]), rows))}")  # Kinda slow
    ans1_dp = 0
    for (row, counts) in rows:
        # print(row, "->", dp(0, row, (), ".", counts))
        ans1_dp += all_possibilities_dp(row, counts)

    print(f"Part 1 (dp): {ans1_dp}")

    ans2 = 0
    for (row, counts) in rows:
        row.append('?')
        new_row = row * 5
        new_row.pop()
        new_counts = counts * 5
        ans2 += all_possibilities_dp(new_row, new_counts)

    print(f"Part 2: {ans2}")


if __name__ == '__main__':
    solve()
