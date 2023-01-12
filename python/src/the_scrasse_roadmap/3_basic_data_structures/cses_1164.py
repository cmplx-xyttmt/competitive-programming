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
    events = []
    m = int(1e6)
    for i in range(n):
        arrival, departure = read_ints()
        events.append(m * (2 * arrival) + i)
        events.append(m * (2 * departure + 1) + i)
    events.sort()
    available_rooms = []
    nxt_room = 1
    for num in events:
        time, id_ = divmod(num, m)
        event_type = time % 2
        if event_type == 0:
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