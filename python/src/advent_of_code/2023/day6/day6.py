from typing import List
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



def get_ways(time, charge_time):
    start = charge_time
    end = time - start
    return end - start + 1


def get_distance(time, charge_time):
    return charge_time * (time - charge_time)


def ways_to_beat_record(time, record_distance):
    ways = 0
    for charge in range(time):
        distance = get_distance(time, charge)
        if distance > record_distance:
            return get_ways(time, charge)
    return ways


def ways_to_beat_record_binary_search(time, record_distance):
    # Invariant:
    # left -> doesn't beat the record
    # right -> beats the record
    left_charge_time = 0
    assert get_distance(time, left_charge_time) < record_distance  # ensure that the left invariant is held at the start
    right_charge_time = time // 2
    assert get_distance(time, right_charge_time) > record_distance # ensure that the right invariant is held at the start

    while right_charge_time > left_charge_time + 1:
        mid = (left_charge_time + right_charge_time) // 2
        beats_record = get_distance(time, mid) > record_distance
        if beats_record:
            right_charge_time = mid
        else:
            left_charge_time = mid

    return get_ways(time, right_charge_time)


def solve():
    # t = c + m
    # d = m * c
    times = list(map(int, read_line().split()[1:]))
    distances = list(map(int, read_line().split()[1:]))

    ans1 = 1
    ans1_binary = 1
    for i in range(len(times)):
        ans1 *= ways_to_beat_record(times[i], distances[i])
        ans1_binary *= ways_to_beat_record_binary_search(times[i], distances[i])

    print(f"Part 1: {ans1}")
    print(f"Part 1 binary: {ans1_binary}")

    time = int("".join(map(str, times)))
    distance = int("".join(map(str, distances)))
    print(f"Part 2: {ways_to_beat_record_binary_search(time, distance)}")


if __name__ == '__main__':
    solve()
