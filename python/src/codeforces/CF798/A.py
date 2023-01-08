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
    for _ in range(t):
        n, m, k = read_ints()
        a = list(read_line())
        b = list(read_line())
        a.sort(reverse=True)
        b.sort(reverse=True)
        a_ops = b_ops = k
        c = []
        while a and b:
            if a_ops > 0 and (a[-1] < b[-1] or b_ops == 0):
                c.append(a.pop())
                a_ops -= 1
                b_ops = k
            else:
                c.append(b.pop())
                b_ops -= 1
                a_ops = k
        print_(f"{''.join(c)}\n")


if __name__ == '__main__':
    solve()
