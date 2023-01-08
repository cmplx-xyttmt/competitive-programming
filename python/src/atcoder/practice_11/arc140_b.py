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
    n = read_int()
    s = read_line()
    arcs = []
    for i in range(n):
        if s[i] == 'R':
            arc = 0
            k, j = i - 1, i + 1
            while k >= 0 and j < n and s[k] == 'A' and s[j] == 'C':
                arc += 1
                k -= 1
                j += 1
            if arc > 0:
                arcs.append(arc)

    arcs.sort(reverse=True)
    j = len(arcs) - 1
    ans = 0
    while j >= 0 and arcs[j] < 2:
        j -= 1

    while arcs:
        ans += 1
        if j >= 0:
            arcs[j] -= 1
            if arcs[j] == 1:
                j -= 1
        else:
            arcs.pop()
        if arcs:
            ans += 1
            arcs.pop()
        j = min(j, len(arcs) - 1)
        while j >= 0 and arcs[j] < 2:
            j -= 1

    print_(f"{ans}\n")


if __name__ == '__main__':
    solve()
