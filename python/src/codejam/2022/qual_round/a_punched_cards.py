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
        r, c = read_ints()

        def row(index, row_type):
            if row_type == 'top':
                return ('..' if index < 2 else '+-') + '+-' * (c - 1) + '+'
            else:
                return ('..' if index < 2 else '|.') + '|.' * (c - 1) + '|'

        grid = [row(0, 'top'), row(1, '')]

        for i in range(2, 2 * r + 1):
            grid.append(row(i, '' if i % 2 == 1 else 'top'))
        ans = '\n'.join(grid)
        print_(f"Case #{case + 1}:\n")
        print_(f"{ans}\n")


if __name__ == '__main__':
    solve()
