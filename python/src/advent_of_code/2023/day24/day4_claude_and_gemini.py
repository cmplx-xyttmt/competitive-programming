import re
from z3 import *

# initial solution by gemini 2.0 Flash was wrong for part 1: https://g.co/gemini/share/29c1c19f4c7b
# after code review by claude 3.5 Haiku, it got it correct for part 1: https://claude.ai/chat/76d01aa9-b0f7-4505-85b4-c6b8307dda70
# Claude also solves part 2.


def intersect_xy(hailstone1, hailstone2, min_coord, max_coord):
    x1, y1, _, vx1, vy1, _ = hailstone1
    x2, y2, _, vx2, vy2, _ = hailstone2

    # Handle parallel lines case
    if vx1 * vy2 == vx2 * vy1:  # More robust parallel check
        return False  # Parallel lines never intersect in the future

    # Calculate denominator first to avoid division by zero
    denominator = vx1 * vy2 - vx2 * vy1

    # Calculate intersection time for both hailstones
    t1 = ((x2 - x1) * vy2 - (y2 - y1) * vx2) / denominator
    t2 = ((x2 - x1) * vy1 - (y2 - y1) * vx1) / denominator

    # Check if intersection occurs in the future
    if t1 < 0 or t2 < 0:
        return False

    # Calculate intersection point
    x_intersect = x1 + t1 * vx1
    y_intersect = y1 + t1 * vy1

    # Check if intersection is within bounds
    return (min_coord <= x_intersect <= max_coord and
            min_coord <= y_intersect <= max_coord)


def solve_part1(hailstones, min_coord, max_coord):
    count = 0
    for i in range(len(hailstones)):
        for j in range(i + 1, len(hailstones)):
            if intersect_xy(hailstones[i], hailstones[j], min_coord, max_coord):
                count += 1
    return count


def solve_part2(hailstones):
    # Create Z3 solver
    solver = Solver()

    # Variables for rock's position and velocity
    rx, ry, rz = Real('rx'), Real('ry'), Real('rz')  # Initial position
    vx, vy, vz = Real('vx'), Real('vy'), Real('vz')  # Velocity

    # We only need first 3 hailstones to find unique solution
    for i, (x, y, z, hx, hy, hz) in enumerate(hailstones[:3]):
        # Time variable for this hailstone
        t = Real(f't{i}')

        # At intersection:
        # rock_pos + t * rock_vel = hailstone_pos + t * hailstone_vel
        solver.add(rx + t * vx == x + t * hx)  # x coordinate
        solver.add(ry + t * vy == y + t * hy)  # y coordinate
        solver.add(rz + t * vz == z + t * hz)  # z coordinate

    # Check if solution exists
    if solver.check() == sat:
        m = solver.model()
        # Get initial position coordinates (this is our answer)
        result = m.eval(rx + ry + rz).as_long()
        return result
    else:
        return "No solution found"


def parse_input(filename):
    hailstones = []
    try:
        with open(filename, 'r') as f:
            for line in f:
                line = line.strip()
                match = re.match(r"(-?\d+),\s*(-?\d+),\s*(-?\d+)\s*@\s*(-?\d+),\s*(-?\d+),\s*(-?\d+)", line)
                if match:
                    x, y, z, vx, vy, vz = map(int, match.groups())
                    hailstones.append((x, y, z, vx, vy, vz))
                else:
                    print(f"Error parsing line: {line}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None

    return hailstones


# Example usage (you'll need to parse your input into the 'hailstones' list)
hailstones_ = parse_input("input.txt")
print(hailstones_[:5])
min_coord = 200000000000000  # Example values
max_coord = 400000000000000  # Example values
result = solve_part1(hailstones_, min_coord, max_coord)
print(f"Part 1: {result}")

# Example usage
# hailstones = parse_input("input.txt")
result = solve_part2(hailstones_)
print(f"Part 2: {result}")
