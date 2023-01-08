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
    n, w = read_ints()
    cheeses = []
    for _ in range(n):
        a, b = read_ints()
        cheeses.append((a, b))

    cheeses.sort(reverse=True)

    deliciousness = 0
    for a, b in cheeses:
        take = min(w, b)
        deliciousness += a * take
        w -= take

    print(deliciousness)


if __name__ == '__main__':
    solve()
