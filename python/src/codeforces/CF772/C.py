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
        can = True
        if a[-1] < a[-2]:
            print_("-1\n")
            continue
        ops = []
        for i in range(n - 3, -1, -1):
            if a[i + 1] - a[n - 1] < a[i]:
                a[i] = a[i + 1] - a[n - 1]
                ops.append(f"{i + 1} {i + 2} {n}")
            if a[i] > a[i + 1]:
                can = False
                break

        if not can:
            print_(f"-1\n")
        else:
            ans_string = '\n'.join(ops)
            print_(f"{len(ops)}\n")
            if len(ops) > 0:
                print_(f"{ans_string}\n")


if __name__ == '__main__':
    solve()
