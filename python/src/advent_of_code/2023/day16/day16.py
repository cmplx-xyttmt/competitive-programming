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


def move_straight(r, c, direction):
    if direction == "right":
        return r, c + 1
    elif direction == "left":
        return r, c - 1
    elif direction == "up":
        return r - 1, c
    else:
        return r + 1, c


def move_90(r, c, direction, symbol):
    new_direction_forward_slash = {
        "right": "up",
        "left": "down",
        "up": "right",
        "down": "left"
    }

    # \
    new__direction_back_slash = {
        "right": "down",
        "left": "up",
        "up": "left",
        "down": "right"
    }
    if symbol == "/":
        new_direction = new_direction_forward_slash[direction]
        return move_straight(r, c, new_direction), new_direction
    else:
        new_direction = new__direction_back_slash[direction]
        return move_straight(r, c, new_direction), new_direction



def add_if_legal(beam, beam_list, num_rows, num_cols):
    nr, nc = beam.position
    if 0 <= nr < num_rows and 0 <= nc < num_cols:
        beam_list.append(beam)


class Beam:

    def __init__(self, position: Tuple[int, int], direction: str):
        self.direction = direction
        self.position = position

    def next_step(self, grid):
        r, c = self.position
        num_rows, num_cols = len(grid), len(grid[0])
        symbol = grid[r][c]
        new_beams = []
        if symbol == "." or (symbol == "|" and self.direction in ["up", "down"]) or (symbol == "-" and self.direction in ["left", "right"]):
            nr, nc = move_straight(r, c, self.direction)
            add_if_legal(Beam((nr, nc), self.direction), new_beams, num_rows, num_cols)
        elif symbol == "|":
            nr_up, nc_up = move_straight(r, c, "up")
            add_if_legal(Beam((nr_up, nc_up), "up"), new_beams, num_rows, num_cols)

            nr_down, nc_down = move_straight(r, c, "down")
            add_if_legal(Beam((nr_down, nc_down), "down"), new_beams, num_rows, num_cols)
        elif symbol == "-":
            nr_right, nc_right = move_straight(r, c, "right")
            add_if_legal(Beam((nr_right, nc_right), "right"), new_beams, num_rows, num_cols)

            nr_left, nc_left = move_straight(r, c, "left")
            add_if_legal(Beam((nr_left, nc_left), "left"), new_beams, num_rows, num_cols)
        else:
            (nr, nc), new_direction = move_90(r, c, self.direction, symbol)
            add_if_legal(Beam((nr, nc), new_direction), new_beams, num_rows, num_cols)
        return new_beams

    def __hash__(self):
        return hash((self.position, self.direction))
    def __eq__(self, other):
        return self.position == other.position and self.direction == other.direction
    
    def __repr__(self):
        return f"{self.position}->{self.direction}"


def find_energized(grid: List[str], start: Beam):
    beams = [start]
    seen = set()
    seen.add(beams[0])
    energized = set()
    energized.add(beams[0].position)
    while beams:
        new_beams = []
        for beam in beams:
            next_beams = beam.next_step(grid)
            for new_beam in next_beams:
                if new_beam not in seen:
                    new_beams.append(new_beam)
                    seen.add(new_beam)
                    energized.add(new_beam.position)
                    # print(new_beam)
        beams = new_beams
    return len(energized)


def solve():
    grid = []
    line = read_line()
    while line:
        grid.append(line)
        line = read_line()


        # print(beams)

    energized1 = find_energized(grid, Beam((0, 0), "right"))
    print(f"Part 1: {energized1}")

    best_energized = 0
    for r in range(len(grid)):
        energized = find_energized(grid, Beam((r, 0), "right"))
        best_energized = max(best_energized, energized)

        energized = find_energized(grid, Beam((r, len(grid[0]) - 1), "left"))
        best_energized = max(best_energized, energized)

    for c in range(len(grid[0])):
        energized = find_energized(grid, Beam((0, c), "down"))
        best_energized = max(best_energized, energized)

        energized = find_energized(grid, Beam((0, len(grid) - 1), "up"))
        best_energized = max(best_energized, energized)

    print(f"Part 2: {best_energized}")


if __name__ == '__main__':
    solve()
