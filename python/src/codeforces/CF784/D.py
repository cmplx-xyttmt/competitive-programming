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
        read_int()
        final = read_line()
        sections = [s for s in final.split('W') if len(s) > 0]
        can = True
        for s in sections:
            colors = set(list(s))
            if len(s) == 1 or len(colors) == 1:
                can = False
                break

        print_(f"{'YES' if can else 'NO'}\n")


if __name__ == '__main__':
    solve()
