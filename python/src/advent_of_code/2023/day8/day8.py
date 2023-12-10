from typing import List, Dict
import sys
from math import gcd

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


def find_zs(graph, instructions, sources):
    curr = list(filter(lambda source_: source_[-1] == 'A', sources))
    cycle_lengths = []
    for source in curr:
        cycle_start, cycle_length, found_z = find_zs_and_cycle_length(source, graph, instructions)
        cycle_lengths.append(cycle_length)
        # the zs found are all equal to the length of the cycle, so we just need to find the lcm of the lengths.

    lcm = cycle_lengths[0]
    for i in range(1, len(cycle_lengths)):
        cycle_length = cycle_lengths[i]
        product = cycle_length * lcm
        gcd_ = gcd(cycle_length, lcm)
        lcm = product // gcd_
    return lcm


def find_zs_and_cycle_length(start, graph, instructions):
    seen = dict()
    zs = []
    steps = 0
    curr = start
    index = 0
    seen[(start, index)] = 0
    while True:
        curr = graph[curr][instructions[index]]
        steps += 1
        if curr[-1] == 'Z':
            zs.append(steps)
        if (curr, index) in seen:
            cycle_start = seen[(curr, index)]
            cycle_length = steps - cycle_start
            return cycle_start, cycle_length, zs
        seen[(curr, index)] = steps
        index = (index + 1) % len(instructions)


def find_zzz(graph, instructions):
    index = 0
    curr = "AAA"
    if curr not in graph:
        return 0
    steps = 0
    while True:
        curr = graph[curr][instructions[index]]
        steps += 1
        if curr == "ZZZ":
            break
        index = (index + 1) % len(instructions)
    return steps


def solve():

    # {AAA -> {L -> BBB, R -> CCC}, ...}
    graph: Dict[str, Dict[str, str]] = dict()
    instructions = read_line()
    read_line()
    mapping_str = read_line()
    sources = []
    while mapping_str:
        source, left_right = mapping_str.split(" = ")
        left, right = left_right.replace('(', '').replace(')', '').split(", ")
        graph[source] = {
            'L': left,
            'R': right
        }
        mapping_str = read_line()
        sources.append(source)
    print(f"Part 1: {find_zzz(graph, instructions)}")
    print(f"Part 2: {find_zs(graph, instructions, sources)}")


if __name__ == '__main__':
    solve()
