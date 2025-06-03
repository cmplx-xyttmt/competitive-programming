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
    h, w = read_ints()
    grid = []
    for line in range(h):
        grid.append(read_ints())
    covering_options = set()
    covering_options.add(0)
    for i in range(h):
        for j in range(w):
            temp = set()
            temp.update(covering_options)
            curr_cell = i * w + j
            for option in covering_options:
                if not ((1 << curr_cell) & option):
                    right_cell = i * w + j + 1
                    down_cell = (i + 1) * w + j
                    if j + 1 < w and not ((1 << right_cell) & option):
                        new_option = option | (1 << curr_cell)
                        new_option |= (1 << right_cell)
                        temp.add(new_option)
                    if i + 1 < h and not ((1 << down_cell) & option):
                        new_option = option | (1 << curr_cell)
                        new_option |= (1 << down_cell)
                        temp.add(new_option)
            covering_options = temp

    # print(len(covering_options))
    # print({bin(mask) for mask in covering_options})
    best = 0
    for option in covering_options:
        xor = 0
        for i in range(h):
            for j in range(w):
                cell = i * w + j
                if not ((1 << cell) & option):
                    xor ^= grid[i][j]
        best = max(xor, best)

    print(best)


if __name__ == '__main__':
    solve()
