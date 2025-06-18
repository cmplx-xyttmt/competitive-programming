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
    n, s = read_ints()
    times = read_ints()
    time_to_sleep = times[0]
    slept = False
    for t in times:
        # print(t, time_to_sleep)
        if time_to_sleep < t:
            slept = True
            break
        time_to_sleep = t + s
    print(f"{'No' if slept else 'Yes'}")


if __name__ == '__main__':
    solve()
