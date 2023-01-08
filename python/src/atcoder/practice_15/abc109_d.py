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
    h, w = read_ints()
    a = []
    for _ in range(h):
        a.append(read_ints())

    ops = []
    x, y = 0, 0
    while x < h and y < w:
        diff = -1 if x % 2 else 1
        if x % 2 == 0 and y == w - 1:
            nxt_x, nxt_y = x + 1, y
        elif x % 2 == 1 and y == 0:
            nxt_x, nxt_y = x + 1, 0
        else:
            nxt_x, nxt_y = x, y + diff
        if a[x][y] % 2 == 1 and 0 <= nxt_x < h and 0 <= nxt_y < w:
            a[nxt_x][nxt_y] += 1
            ops.append((x + 1, y + 1, nxt_x + 1, nxt_y + 1))

        x, y = nxt_x, nxt_y
    print_(f"{len(ops)}\n")
    ans = "\n".join(map(lambda op: f"{op[0]} {op[1]} {op[2]} {op[3]}", ops))
    print_(f"{ans}\n")


if __name__ == '__main__':
    solve()
