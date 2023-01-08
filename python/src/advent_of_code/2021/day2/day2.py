import sys

sys.stdin = open('input.in', 'r')

input = sys.stdin.readline

if __name__ == '__main__':
    horizontal, depth = 0, 0

    instructions = []
    instruction = input()
    while instruction:
        direction, distance = instruction.split(" ")
        distance = int(distance)
        instructions.append((direction, distance))
        if direction == "forward":
            horizontal += distance
        elif direction == "up":
            depth -= distance
        else:
            depth += distance
        instruction = input()

    print(f"Part 1: {horizontal * depth}")

    horizontal, depth, aim = 0, 0, 0
    for (direction, distance) in instructions:
        if direction == "forward":
            horizontal += distance
            depth += (aim * distance)
        elif direction == "up":
            aim -= distance
        else:
            aim += distance

    print(f"Part 2: {horizontal * depth}")
