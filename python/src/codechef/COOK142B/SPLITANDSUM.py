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


def get_split(arr, bit):
    split = []
    l = 1
    ones = 0
    for i in range(len(arr)):
        if arr[i] & bit:
            ones += 1
            if ones >= 2:
                split.append([l, i])
                l = i + 1
    split.append([l, len(arr)])
    # print(bit, ones, split)
    return split


def solve():
    t = read_int()
    for _ in range(t):
        read_int()
        a = read_ints()
        max_ = max(a)
        bit = 1
        found = False
        while bit <= max_:
            split = get_split(a, bit)
            if len(split) > 1:
                print_(f"YES\n")
                print_(f"{len(split)}\n")
                ans = '\n'.join(map(lambda l: f"{l[0]} {l[1]}", split))
                print_(f"{ans}\n")
                found = True
                break
            bit <<= 1
        if not found:
            print_(f"NO\n")


if __name__ == '__main__':
    solve()
