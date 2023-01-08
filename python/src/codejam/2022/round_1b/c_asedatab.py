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


def rotations(num):
    s = bin(num)[2:].zfill(8)
    group = set()
    for i in range(8):
        group.add(int(s[i:] + s[0:i], 2))
    return group


def ones(num):
    return bin(num)[2:].count('1')


def solve():
    groups = dict()
    seen = set()
    parent = [i for i in range(256)]
    for i in range(256):
        if i not in seen:
            groups[i] = rotations(i)
            seen.update(groups[i])
            for num in groups[i]:
                parent[num] = i

    print(len(groups), groups)


if __name__ == '__main__':
    solve()
