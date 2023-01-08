from typing import List
import sys

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
    n = read_int()
    s = read_ints()
    d = []
    for i in range(1, n):
        d.append(s[i - 1] - s[i])
    # print(d)
    lower = [0, 0, 0]
    sums = [0, 0, 0]
    for i in range(len(d)):
        mod = i % 3
        sums[mod] += d[i]
        lower[mod] = max(lower[mod], sums[mod])

    a = [lower[0]]
    if a[0] > s[0]:
        print_("No\n")
    else:
        rem = s[0] - a[0]
        a.append(lower[1])
        if a[1] > rem:
            print_("No\n")
            return
        rem = rem - a[1]
        a.append(rem)
        if a[2] > rem:
            print_("No\n")
            return
        can = True
        for i in range(3, n + 2):
            a.append(a[i - 3] - d[i - 3])
            if a[-1] < 0:
                can = False
        if not can:
            print_("No\n")
        else:
            print_("Yes\n")
            print_(f"{' '.join(map(str, a))}\n")


if __name__ == '__main__':
    solve()
