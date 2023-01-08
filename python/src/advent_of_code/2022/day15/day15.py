from collections import deque
from typing import List
import sys

sys.stdin = open("day15.in", "r")
sys.stdout = open("day15.out", "w")

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


def cant_row(distance, sensor, row):
    q = deque()
    q.append((sensor, 0))
    coords = set()
    d = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    seen = set()
    seen.add(sensor)
    while q:
        (r, c), dist = q.popleft()
        if dist > distance:
            break
        if r == row:
            coords.add(c)
        for dr, dc in d:
            nr, nc = r + dr, c + dc
            if (nr, nc) not in seen:
                q.append(((nr, nc), dist + 1))
                seen.add((nr, nc))

    return coords


def find_gap(ranges, min_col, max_col, debug=False):
    l, r = min_col, min_col
    for nl, nr in ranges:
        if debug:
            sys.stderr.write(f"{l} -> {r}\n")
        if nl > r:
            return r + 1
        r = max(r, nr)
        if r > max_col:
            break
    return None


def cant_row_efficient(sensors, beacons, row):
    beacons_set = set(beacons)
    sensors_set = set(sensors)
    all_set = beacons_set.union(sensors_set)
    filled_cols = [c for r, c in all_set if r == row]
    # sys.stderr.write(f"{[c for r, c in all_set if r == row]}\n")
    ranges = []
    for i in range(len(sensors)):
        sr, sc = sensors[i]
        br, bc = beacons[i]
        distance = abs(sr - br) + abs(sc - bc)
        high = distance + sc - abs(sr - row)
        low = sc - distance + abs(sr - row)
        # if high == 25:
        #     sys.stderr.write(f"{(sr, sc)} -> {(br, bc)}: {distance}\n")
        if low <= high:
            # if row == 11:
            #     sys.stderr.write(f"{(sr, sc)} -> {(br, bc)}: {distance} {(low, high)}\n")
            ranges.append((low, high))

    ranges.sort()
    # sys.stderr.write(f"{ranges}\n")
    min_col = min([left for left, _ in ranges])
    max_col = max([right for _, right in ranges])
    return max_col - min_col + 1 - len(filled_cols), ranges


def solve():
    line = read_line()

    sensors = []
    beacons = []
    max_col = 0
    min_col = 0
    while line:
        split = line.replace('x=', '').replace('y=', '').replace(':', '').replace(',', '').split(" ")
        sensor_c, sensor_r, beacon_c, beacon_r = map(int, [split[2], split[3], split[8], split[9]])
        sensors.append((sensor_r, sensor_c))
        beacons.append((beacon_r, beacon_c))
        max_col = max(max(sensor_c, beacon_c), max_col)
        min_col = min(min(sensor_c, beacon_c), min_col)
        # sys.stderr.write(f"{split}\n")
        line = read_line()

    sys.stderr.write(f"{min_col} {max_col}\n")

    row = 10
    coords_at_row = set()
    # for i in range(len(sensors)):
    #     distance = abs(sensors[i][0] - beacons[i][0]) + abs(sensors[i][1] - beacons[i][1])
    #     coords_at_row = coords_at_row.union(cant_row(distance, sensors[i], row))

    print(f"Part 1: {cant_row_efficient(sensors, beacons, row)[0]}")
    # sys.stderr.write(f"{coords_at_row}\n")

    min_, max_ = 0, 4_000_000
    for row in range(min_, max_ + 1):
        size, ranges = cant_row_efficient(sensors, beacons, row)
        gap = find_gap(ranges, min_, max_, row == 11)
        if gap is not None:
            print(f"Part 2: {(gap * max_ + row)}")
            break


if __name__ == '__main__':
    solve()
