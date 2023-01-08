from typing import List
import sys
import heapq

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


def convert_time_to_minutes(time):
    hours, minutes = map(int, time.split(":"))
    return hours * 60 + minutes


def solve():
    t = read_int()

    for case in range(1, t + 1):
        cooldown = read_int()
        na, nb = read_ints()
        trips = []  # (start, end, from_a)
        for _ in range(na):
            start, end = map(convert_time_to_minutes, read_strings())
            trips.append((start, end, True))
        for _ in range(nb):
            start, end = map(convert_time_to_minutes, read_strings())
            trips.append((start, end, False))

        trips.sort()
        a_trains = []
        b_trains = []

        def assign_train(fro, to, _start, _end, _cooldown):
            if len(fro) == 0 or fro[0] > _start:
                heapq.heappush(to, _end + _cooldown)
                return 1
            else:
                heapq.heappop(fro)
                heapq.heappush(to, _end + _cooldown)
                return 0
        ans_a, ans_b = 0, 0
        for start, end, from_a in trips:
            if from_a:
                ans_a += assign_train(a_trains, b_trains, start, end, cooldown)
            else:
                ans_b += assign_train(b_trains, a_trains, start, end, cooldown)
        print_(f"Case #{case}: {ans_a} {ans_b}\n")


if __name__ == '__main__':
    solve()
