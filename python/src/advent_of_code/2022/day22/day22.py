from typing import List
import sys

sys.stdin = open("day22.in", "r")
sys.stdout = open("day22.out", "w")

input_ = sys.stdin.readline
print_ = sys.stdout.write
flush = sys.stdout.flush


def read_line() -> str:
    return input_().strip('\n')


def read_int() -> int:
    return int(read_line())


def read_strings() -> List[str]:
    return list(read_line().split())


def read_ints():
    return list(map(int, read_line().split()))


directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
dir_list = ['R', 'D', 'L', 'U']

wrap = dict()
grid = []
draw_grid = []


def move(row, col, direction):
    nr, nc = row + directions[direction][0], col + directions[direction][1]
    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] != ' ':
        return (row, col, direction) if grid[nr][nc] == '#' else (nr, nc, direction)

    # sys.stderr.write(f"{(row, col, dir_list[direction])} {(nr, nc)} {grid[row][col]}\n")
    nr, nc, nd = wrap[(row, col, direction)]

    return (row, col, direction) if grid[nr][nc] == '#' else (nr, nc, nd)


def part2_wrap():
    faces = {

    }
    for row in range(50):
        wrap[(row, 50, 2)] = wrap[(100 + row, 0, 0)]


def simulate(s_row, s_col, instructions):
    direction = 0
    row, col = s_row, s_col
    for inst in instructions:
        # sys.stderr.write(f"{inst}\n")
        if inst == 'L':
            direction = (4 + direction - 1) % 4
        elif inst == 'R':
            direction = (direction + 1) % 4
        else:
            draw_grid[row][col] = ['>', 'V', '<', '^'][direction]
            # sys.stderr.write(f"{inst} {dir_list[direction]}\n")
            for _ in range(inst):
                nr, nc, nd = move(row, col, direction)
                if (nr, nc) == (row, col):
                    break
                row, col, direction = nr, nc, direction
                draw_grid[row][col] = ['>', 'V', '<', '^'][direction]
    return row, col, direction


def solve():
    line = read_line()
    while line:
        grid.append(line)
        line = read_line()

    instructions_str = read_line()
    grid_str = '\n'.join(grid)
    # sys.stderr.write(f"{grid_str}\n{instructions_str}\n")
    max_rows = max([len(row) for row in grid])

    for i in range(len(grid)):
        if len(grid[i]) < max_rows:
            grid[i] += ' ' * (max_rows - len(grid[i]))

    for row in grid:
        draw_grid.append(list(row))

    start_row, start_col = 0, 0
    for c in range(len(grid[0])):
        if grid[start_row][c] == '.':
            start_col = c
            break

    dist = 0
    instructions = []
    for c in instructions_str:
        if c in ['L', 'R']:
            instructions.append(dist)
            instructions.append(c)
            dist = 0
        else:
            dist = dist * 10 + int(c)
    instructions.append(dist)

    sys.stderr.write(f"{instructions}\n{(start_row, start_col)}\n")

    for row in range(len(grid)):
        s, e = -1, -1
        for col in range(len(grid[0])):
            if grid[row][col] in ['.', '#']:
                e = col
                if s == -1:
                    s = col
            if row == 0:
                sr, er = -1, -1
                for n_row in range(len(grid)):
                    if col < len(grid[n_row]) and grid[n_row][col] in ['.', '#']:
                        er = n_row
                        if sr == -1:
                            sr = n_row
                wrap[(sr, col, 3)] = (er, col, 3)
                wrap[(er, col, 1)] = (sr, col, 1)
        # if row == 126:
        #     sys.stderr.write(f"{(row, s)} {(row, e)}")
        wrap[(row, s, 2)] = (row, e, 2)
        wrap[(row, e, 0)] = (row, s, 0)

    r, c, d = simulate(start_row, start_col, instructions)
    sys.stderr.write(f"{r} {c} {dir_list[d]} {grid[r][c]}\n")
    # grid_str = '\n'.join([''.join(row) for row in draw_grid])
    # sys.stderr.write(f"{grid_str}\n")
    print(f"Part 1: {(r + 1) * 1000 + 4 * (c + 1) + d}")


if __name__ == '__main__':
    solve()
