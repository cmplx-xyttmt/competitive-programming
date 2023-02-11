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
    n, m = read_ints()
    pairs = set()

    for _ in range(m):
        line = read_ints()
        for i in range(1, len(line)):
            for j in range(i + 1, len(line)):
                a, b = min(line[i], line[j]), max(line[i], line[j])
                pairs.add((a, b))

    all_pairs = True

    for i in range(1, n + 1):
        if not all_pairs:
            break
        for j in range(i + 1, n + 1):
            if (i, j) not in pairs:
                all_pairs = False
                break

    print(f"{'Yes' if all_pairs else 'No'}\n")


if __name__ == '__main__':
    solve()
