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


def sol_groups(length, sizes):
    groups = [(0, len(sizes) - 1, length)] # start_idx, end_idx, sum

    cost = 0
    while groups:
        s_i, e_i, s = groups.pop()
        if s_i == e_i:
            continue
        curr_sum = 0
        diff = s
        for i in range(s_i, e_i + 1):
            if abs(s - 2 * (curr_sum + sizes[i])) >= diff:
                cost += s
                groups.append((s_i, i - 1, curr_sum))
                groups.append((i, e_i, s - curr_sum))
                break
            else:
                curr_sum += sizes[i]
                diff = abs(s - 2 * curr_sum)

    return cost


def solve():
    x, n = read_ints()
    d = read_ints()
    d.sort()

    print_(f"{sol_groups(x, d)}\n")

    # TODO: Solve this later...


if __name__ == '__main__':
    solve()
