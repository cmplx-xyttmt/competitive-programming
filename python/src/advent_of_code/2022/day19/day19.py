import functools
from typing import List
import sys

sys.stdin = open("day19.in", "r")
sys.stdout = open("day19.out", "w")

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


class Robot:

    def __init__(self, cost_info: str):
        cost_info = cost_info.split(" ")
        self.type = cost_info[1]
        self.costs = [int(cost_info[4]), 0, 0, 0]
        if self.type == 'obsidian':
            self.costs[1] = int(cost_info[7])
        if self.type == 'geode':
            self.costs[2] = int(cost_info[7])
        self.ore_cost, self.clay_cost, self.obsidian_cost, self.geode_cost = self.costs

    def can_get(self, resources):
        return all([r >= c for r, c in zip(resources, self.costs)])

    def __repr__(self):
        return f"Robot({self.type}, {self.costs})"


class Blueprint:

    def __init__(self, id_, ore_robot_info, clay_robot_info, obsidian_robot_info, geode_robot_info):
        self.id = id_
        self.robots: List[Robot] = [
            Robot(ore_robot_info.strip()),
            Robot(clay_robot_info.strip()),
            Robot(obsidian_robot_info.strip()),
            Robot(geode_robot_info.strip())
        ]
        self.maxes = [4, 4, 10, 24]
        self.ore_robot = Robot(ore_robot_info.strip())
        self.clay_robot = Robot(clay_robot_info.strip())
        self.obsidian_robot = Robot(obsidian_robot_info.strip())
        self.geode_robot = Robot(geode_robot_info.strip())

    def __hash__(self):
        return self.id

    def __repr__(self):
        robots = ','.join(map(str, self.robots))
        return f"Blueprint({self.id}, {robots})"


reps = [0]
max_resources = [0]


def get_next_robot(robot: Robot, resources: List[int]):
    need = [max(c - r, 0) for r, c in zip(resources, robot.costs)]
    max_ = max(need)
    for i in range(4):
        if need[i] == max_:
            return i
    return -1


def next_state(idx_to_build, robots, resources, blueprint, minute, time):
    max_robots = [
        max([blueprint.robots[i].ore_cost for i in range(4)]),
        max([blueprint.robots[i].clay_cost for i in range(4)]),
        max([blueprint.robots[i].obsidian_cost for i in range(4)]),
        time
    ]
    # sys.stderr.write(f"{max_robots}\n")
    resources_limits = [(time + 1 - minute) * max_robots[i] for i in range(4)]
    # sys.stderr.write(f"Robs: {max_robots} Res: {resources_limits}\n")

    new_resources = [min(resources_limits[i], resources[i] + robots[i]) for i in range(4)]
    if idx_to_build == -1:
        new_robots = [rbs for rbs in robots]
    else:
        new_resources = [r - c for r, c in zip(new_resources, blueprint.robots[idx_to_build].costs)]
        new_robots = list(robots)
        new_robots[idx_to_build] = min(max_robots[idx_to_build], new_robots[idx_to_build] + 1)
    return tuple(new_robots), tuple(new_resources)


@functools.lru_cache(maxsize=None)
def simulate(minute, robots, resources, blueprint: Blueprint, time):
    reps[0] += 1
    max_resources[0] = max(resources)
    # if blueprint.id == 1:
    #     sys.stderr.write(f"Minute {minute}: {robots} {resources} (Blueprint: {blueprint.id})\n")
    if minute == time:
        # sys.stderr.write(f"{reps} -> {minute} -> ({robots}, {resources}) (blueprint: {blueprint.id})\n")
        return resources[3] + robots[3]

    best = 0
    for idx_to_build in range(-1, 4):
        if idx_to_build == -1 or blueprint.robots[idx_to_build].can_get(resources):
            new_robots, new_resources = next_state(idx_to_build, robots, resources, blueprint, minute, time)
            best = max(best, simulate(minute + 1, new_robots, new_resources, blueprint, time))

    return best


def solve():
    line = read_line()
    blueprints = []
    while line:
        blueprint_id, costs = line.split(':')
        blueprint_id = int(blueprint_id.strip().split(" ")[1])
        blueprints.append(Blueprint(blueprint_id, *costs.split('.')[:-1]))

        line = read_line()

    bps = '\n'.join(map(str, blueprints))
    sys.stderr.write(f"{bps}\n")

    geodes = []
    for blueprint in blueprints:
        robots = (1, 0, 0, 0)  # ore, clay, obsidian, geode
        resources = (0, 0, 0, 0)
        geode = (blueprint.id, simulate(1, robots, resources, blueprint, 24))
        sys.stderr.write(f"Cache info: {simulate.cache_info()}\n")
        sys.stderr.write(f"{geode}\n")
        geodes.append(geode)
    sys.stderr.write(f"Max: {max(geodes, key=lambda g: g[1])} \n{geodes}\n")

    print(f"Part 1: {sum([id_ * g for id_, g in geodes])}")

    geodes = []
    for blueprint in blueprints[:3]:
        robots = (1, 0, 0, 0)  # ore, clay, obsidian, geode
        resources = (0, 0, 0, 0)
        geode = simulate(1, robots, resources, blueprint, 32)
        sys.stderr.write(f"{geode}\n")
        geodes.append(geode)
    print(f"Part 2: {geodes[0] * geodes[1] * geodes[2]}")


if __name__ == '__main__':
    solve()
