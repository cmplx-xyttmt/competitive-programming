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
        n = read_int()
        a = read_ints()
        if n % 2 == 1:
            print_(f"Mike\n")
            continue
        least = min(a)
        winner = None
        for i in range(n):
            if i % 2 == 0:
                if a[i] == least:
                    winner = 'Joe'
                    break
            else:
                if a[i] == least:
                    winner = 'Mike'
                    break

        print_(f"{winner}\n")


if __name__ == '__main__':
    solve()
