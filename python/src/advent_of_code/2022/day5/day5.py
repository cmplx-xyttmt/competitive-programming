from dataclasses import dataclass
from typing import List
import sys

input_file = "day5.in"
sample_input_file = "day5_sample.in"

sys.stdout = open("day5.out", "w")


input_ = sys.stdin.readline
print_ = sys.stdout.write
flush = sys.stdout.flush


@dataclass
class InputConstants:
    num_stacks: int
    longest_stack: int
    instructions_start: int
    input_file: str


def print_error(*items):
    for item in items:
        sys.stderr.write(f"{str(item)} ")
    sys.stderr.write("\n")


def read_line() -> str:
    return input_().strip()


def read_int() -> int:
    return int(read_line())


def read_strings() -> List[str]:
    return list(read_line().split())


def read_ints():
    return list(map(int, read_line().split()))


def solve():
    input_constants = InputConstants(9, 8, 10, input_file) if sys.argv[1] == 'final' \
        else InputConstants(3, 3, 5, sample_input_file)
    sys.stdin = open(input_constants.input_file, "r")
    lines = sys.stdin.readlines()
    stacks = [[] for _ in range(input_constants.num_stacks)]
    for i in range(input_constants.longest_stack):
        line = lines[i]
        for j in range(0, len(line), 4):
            crate = line[j:j+4].strip().replace('[', '').replace(']', '')
            if crate:
                # print_error(crate, stacks, j, line)
                stacks[j // 4].append(crate)

    for stack in stacks:
        stack.reverse()

    stacks2 = [stack[:] for stack in stacks]

    for i in range(input_constants.instructions_start, len(lines)):
        _, num_items, _, frm, _, to = lines[i].split(" ")
        num_items, frm, to = map(int, [num_items, frm, to])
        for _ in range(num_items):
            stacks[to - 1].append(stacks[frm - 1].pop())
        stacks2[to - 1].extend(stacks2[frm - 1][-num_items:])
        stacks2[frm - 1] = stacks2[frm - 1][:-num_items]

    ans = "".join([stack[-1] for stack in stacks])
    print_error(stacks2)
    ans2 = "".join('' if not stack else stack[-1] for stack in stacks2)
    print(f"Part 1: {ans}")
    print(f"Part 2: {ans2}")


if __name__ == '__main__':
    solve()
