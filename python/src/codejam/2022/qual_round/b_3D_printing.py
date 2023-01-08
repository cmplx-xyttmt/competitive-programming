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
    t = read_int()

    for case in range(t):
        p1 = read_ints()
        p2 = read_ints()
        p3 = read_ints()
        needed_paint = int(1e6)
        ans = []
        for i in range(4):
            ans.append(min(needed_paint, min(p1[i], p2[i], p3[i])))
            needed_paint -= ans[-1]

        if needed_paint != 0:
            print_(f"Case #{case + 1}: IMPOSSIBLE\n")
        else:
            print_(f"Case #{case + 1}: {' '.join(map(str, ans))}\n")


if __name__ == '__main__':
    solve()
