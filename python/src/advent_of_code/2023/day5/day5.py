import dataclasses
from collections import defaultdict
from typing import List, Dict
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


@dataclasses.dataclass
class Range:
    destination_start: int
    source_start: int
    length: int


def find_next(source_object: int, ranges: List[Range]) -> int:
    for range_ in ranges:
        if range_.source_start <= source_object < range_.source_start + range_.length:
            return range_.destination_start + (source_object - range_.source_start)
    return source_object


def find_location(seed: int, pipeline: Dict[str, List[Range]]) -> int:
    soil = find_next(seed, pipeline["seed-to-soil"])
    fertilizer = find_next(soil, pipeline["soil-to-fertilizer"])
    water = find_next(fertilizer, pipeline["fertilizer-to-water"])
    light = find_next(water, pipeline["water-to-light"])
    temperature = find_next(light, pipeline["light-to-temperature"])
    humidity = find_next(temperature, pipeline["temperature-to-humidity"])
    location = find_next(humidity, pipeline["humidity-to-location"])
    return location


def solve():
    pipeline = defaultdict(list)
    _, seeds_str = read_line().split(": ")
    seeds = map(int, seeds_str.strip().split())

    read_line()
    while True:
        map_type, _ = read_line().split()
        range_str = read_line()
        ranges = []
        while range_str:
            dest_start, src_start, length = map(int, range_str.split())
            ranges.append(Range(dest_start, src_start, length))
            range_str = read_line()

        pipeline[map_type] = ranges
        if map_type == "humidity-to-location":
            break

    locations = list(map(lambda seed: find_location(seed, pipeline), seeds))
    print(locations)
    print(f"Part 1: {min(locations)}")


if __name__ == '__main__':
    solve()
