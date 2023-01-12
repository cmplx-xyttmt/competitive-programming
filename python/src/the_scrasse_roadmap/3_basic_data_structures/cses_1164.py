from collections import defaultdict
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


def solve():
    n = read_int()
    rooms = [0] * n
    times = []
    events = defaultdict(list)
    for i in range(n):
        arrival, departure = read_ints()
        if arrival not in events:
            times.append(arrival)
        events[arrival].append(('a', i))
        if departure not in events:
            times.append(departure)
        events[departure].append(('d', i))

    for time_events in events.values():
        time_events.sort()

    times.sort()
    nxt_room = 1
    available_rooms = []
    for time in times:
        for (event_type, id_) in events[time]:
            if event_type == 'a':
                if available_rooms:
                    rooms[id_] = available_rooms.pop()
                else:
                    rooms[id_] = nxt_room
                    nxt_room += 1
            else:
                available_rooms.append(rooms[id_])

    print_(f"{nxt_room - 1}\n")
    print_(f"{' '.join(map(str, rooms))}\n")


if __name__ == '__main__':
    solve()
