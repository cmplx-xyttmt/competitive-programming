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


def get_parent(a, parents):
    if a not in parents:
        parents[a] = a
        return a
    path = []
    while a != parents[a]:
        path.append(a)
        a = parents[a]

    for node in path:
        parents[node] = a
    return a


def union(a, b, parents):
    a, b = get_parent(a, parents), get_parent(b, parents)
    if a == b:
        return

    parents[a] = b


def cell_to_int(r, c, num_cols):
    return r * num_cols + c


def int_to_cell(num, num_cols):
    return num // num_cols, num % num_cols


def solve():
    t = read_int()
    for test in range(t):
        n, num_rows, num_cols, r, c = read_ints()
        r -= 1
        c -= 1
        instructions = read_line()
        directions = {'N': 0, 'E': 1, 'S': 2, 'W': 3}
        deltas = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        parents = [dict() for _ in range(4)]  # 0 -> north, 1 -> east, 2 -> south, 3 -> west

        for d in instructions:
            curr_cell = cell_to_int(r, c, num_cols)
            new_row, new_col = 0, 0
            for direction in range(4):
                nr, nc = r + deltas[direction][0], c + deltas[direction][1]
                if 0 <= nr < num_rows and 0 <= nc < num_cols:
                    next_cell = cell_to_int(nr, nc, num_cols)
                    union(curr_cell, next_cell, parents[direction])
                    if direction == directions[d]:
                        parent = get_parent(next_cell, parents[direction])
                        new_row, new_col = int_to_cell(parent, num_cols)

            r, c = new_row, new_col
        print_(f"Case #{test + 1}: {r + 1} {c + 1}\n")


if __name__ == '__main__':
    solve()
