from typing import List
import sys

sys.stdin = open("day9.in", "r")
sys.stdout = open("day9.out", "w")

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


def draw_grid(positions):
    size = 30
    grid = [['.'] * size for _ in range(size)]
    for i in reversed(range(len(positions))):
        x, y = positions[i]
        grid[x + size//2][y + size // 2] = str(i)

    grid_str = '\n'.join(map(lambda row: ''.join(row), grid))
    sys.stderr.write(f"{grid_str}\n")
    sys.stderr.write(f"====================================================\n")


def solve():
    line = read_line()
    delta = {
        'U': (-1, 0),
        'D': (1, 0),
        'L': (0, -1),
        'R': (0, 1)
    }
    ropes = 10
    positions = [(0, 0) for _ in range(ropes)]
    draw_grid(positions)
    seen1 = set()
    seen1.add((0, 0))
    seen2 = set()
    seen2.add((0, 0))
    while line:
        d, steps = line.split()
        steps = int(steps)
        dx, dy = delta[d]
        for _ in range(steps):
            hx, hy = positions[0]
            hx, hy = hx + dx, hy + dy
            positions[0] = hx, hy
            for rope in range(1, ropes):
                hx, hy = positions[rope - 1]
                tx, ty = positions[rope]

                # sys.stderr.write(f"Rope {rope}: prev: {hx} {hy} from: {tx} {ty}")
                if hx == tx or hy == ty:
                    if abs(hx - tx) + abs(hy - ty) > 1:
                        if hx > tx:
                            tx = hx - 1
                        elif hx < tx:
                            tx = hx + 1
                        if hy > ty:
                            ty = hy - 1
                        elif hy < ty:
                            ty = hy + 1
                elif abs(hx - tx) + abs(hy - ty) > 2:
                    # tx, ty = prev_hx, prev_hy
                    x, y = hx - tx, hy - ty
                    x = 1 if x > 0 else -1
                    y = 1 if y > 0 else -1
                    tx, ty = tx + x, ty + y
                positions[rope] = tx, ty
                if rope == ropes - 1:
                    seen2.add((tx, ty))
                    # sys.stderr.write(f"{d} {steps}: {(hx, hy)} {(tx, ty)}\n")
                if rope == 1:
                    seen1.add((tx, ty))
            #     sys.stderr.write(f" to: {tx} {ty}\n")
            # sys.stderr.write(f"{d} {steps}:\n")
            # draw_grid(positions)
            # sys.stderr.write(f"{str((tx, ty))}\n")
        line = read_line()

    print(f"Part 1: {len(seen1)}")
    print(f"Part 2: {len(seen2)}")


if __name__ == '__main__':
    solve()
