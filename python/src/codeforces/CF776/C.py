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

    for _ in range(t):
        read_line()
        n, m = read_ints()
        points = []
        for i in range(m):
            coord, weight = read_ints()
            points.append((coord, weight, i + 1))

        points.sort(key=lambda x: x[1])
        points_to_take = points[:2 * n]
        points_to_take.sort(key=lambda x: x[0])

        segments = []
        total = 0
        for i in range(len(points_to_take)):
            # print(i, 2 * n - i - 1)
            if i >= 2 * n - i - 1:
                break
            left = points_to_take[i]
            right = points_to_take[2 * n - i - 1]
            segments.append(f"{left[2]} {right[2]}")
            total += left[1] + right[1]

        print_(f"{total}\n")
        segs = '\n'.join(segments)
        print_(f"{segs}\n\n")


if __name__ == '__main__':
    solve()
