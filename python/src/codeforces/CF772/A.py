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
        read_int()
        a = read_ints()
        ans = 0
        pow2 = 1
        while sum(a) > 0:
            add = any([num % 2 == 1 for num in a])
            if add:
                ans += pow2
            a = [num // 2 for num in a]
            pow2 *= 2
        print(ans)


if __name__ == '__main__':
    solve()
