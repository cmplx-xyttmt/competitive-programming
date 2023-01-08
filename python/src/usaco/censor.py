from typing import List
import sys

sys.stdin = open("censor.in", "r")
sys.stdout = open("censor.out", "w")

input_ = sys.stdin.readline
print_ = sys.stdout.write
flush = sys.stdout.flush


def readline() -> str:
    return input_().strip()


def read_int() -> int:
    return int(readline())


def read_strings() -> List[str]:
    return list(readline().split())


def read_ints():
    return list(map(int, readline().split()))


def solve():
    s = readline()
    t = readline()
    new_s = ""
    for c in s:
        new_s += c
        if c == t[-1] and len(new_s) > len(t) and new_s[-len(t):] == t:
            new_s = new_s[0:-len(t)]

    print_(f"{new_s}\n")


if __name__ == '__main__':
    solve()
