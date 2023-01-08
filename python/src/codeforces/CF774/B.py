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
    t = read_int()

    for _ in range(t):
        n = read_int()
        a = read_ints()
        a.sort()
        prefix = [a[0]]
        for i in range(1, n):
            # print(i, prefix)
            prefix.append(prefix[i - 1] + a[i])

        can = False
        for red in range(1, n):
            red_sum = prefix[n - 1] - prefix[n - red - 1]
            blue_sum = prefix[red]
            if n - red - 1 < red:
                break
            if red_sum > blue_sum:
                can = True
                break
        print("YES" if can else "NO")


if __name__ == '__main__':
    solve()
