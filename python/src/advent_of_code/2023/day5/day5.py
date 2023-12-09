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
class Mapping:
    destination_start: int
    source_start: int
    length: int

@dataclasses.dataclass
class Range:
    """[start, end) ranges, where start is inclusive and end is exclusive"""
    start: int
    end: int


def find_next_single(source_object: int, mappings: List[Mapping]) -> int:
    for mapping in mappings:
        if mapping.source_start <= source_object < mapping.source_start + mapping.length:
            return mapping.destination_start + (source_object - mapping.source_start)
    return source_object


def find_next_ranges(source_ranges: List[Range], mappings: List[Mapping], debug = False) -> List[Range]:
    new_ranges = []
    for mapping in mappings:
        non_intersecting_ranges = []
        for range_ in source_ranges:
            start, end = range_.start, range_.end
            map_start, map_end = mapping.source_start, mapping.source_start + mapping.length

            before_start, before_end = start, min(end, map_start)
            if before_start < before_end:
                non_intersecting_ranges.append(Range(before_start, before_end))

            intersection_start, intersection_end = max(start, map_start), min(end, map_end)
            if debug:
                print(f"{mapping}, {range_}->", intersection_start, intersection_end)
            if intersection_start < intersection_end:
                new_start = mapping.destination_start + (intersection_start - map_start)
                new_end = mapping.destination_start + (intersection_end - map_start)
                new_ranges.append(Range(new_start, new_end))

            after_start, after_end = max(start, map_end), end
            if after_start < after_end:
                non_intersecting_ranges.append(Range(after_start, after_end))
            if debug:
                print(f"{mapping} -> {new_ranges}")
        source_ranges = non_intersecting_ranges

    new_ranges += source_ranges
    # print(f"{mappings} -> {new_ranges}")
    return new_ranges


def find_single_location(seed: int, pipeline: Dict[str, List[Mapping]]) -> int:
    soil = find_next_single(seed, pipeline["seed-to-soil"])
    fertilizer = find_next_single(soil, pipeline["soil-to-fertilizer"])
    water = find_next_single(fertilizer, pipeline["fertilizer-to-water"])
    light = find_next_single(water, pipeline["water-to-light"])
    temperature = find_next_single(light, pipeline["light-to-temperature"])
    humidity = find_next_single(temperature, pipeline["temperature-to-humidity"])
    location = find_next_single(humidity, pipeline["humidity-to-location"])
    return location


def find_range_location(ranges: List[Range], pipeline: Dict[str, List[Mapping]]) -> int:
    for stage in pipeline.keys():
        # print(ranges)
        mappings = pipeline[stage]
        # debug = True if stage == "seed-to-soil" else False
        ranges = find_next_ranges(ranges, mappings)
    ranges.sort(key=lambda range_: range_.start)
    return ranges[0].start


def solve():
    pipeline = defaultdict(list)
    _, seeds_str = read_line().split(": ")
    seeds = map(int, seeds_str.strip().split())
    ranges = []
    seeds_list = list(seeds)
    for i in range(0, len(seeds_list), 2):
        ranges.append(Range(seeds_list[i], seeds_list[i] + seeds_list[i + 1]))

    read_line()
    while True:
        map_type, _ = read_line().split()
        range_str = read_line()
        mappings = []
        while range_str:
            dest_start, src_start, length = map(int, range_str.split())
            mappings.append(Mapping(dest_start, src_start, length))
            range_str = read_line()

        pipeline[map_type] = mappings
        if map_type == "humidity-to-location":
            break

    locations = list(map(lambda seed: find_single_location(seed, pipeline), seeds_list))
    # print(locations)
    print(f"Part 1: {min(locations)}")
    print(f"Part 2: {find_range_location(ranges, pipeline)}")


if __name__ == '__main__':
    solve()
