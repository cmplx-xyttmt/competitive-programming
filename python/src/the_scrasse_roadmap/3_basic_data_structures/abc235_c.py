from typing import List
import sys
from collections import defaultdict

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
    n, q = read_ints()
    a = read_ints()
    numbers = defaultdict(list)
    for i, num in enumerate(a):
        numbers[num].append(i)

    ans = []
    for _ in range(q):
        x, k = read_ints()
        if x in numbers and k <= len(numbers[x]):
            ans.append(numbers[x][k - 1] + 1)
        else:
            ans.append(-1)

    ans = '\n'.join(map(str, ans))
    print(ans)


if __name__ == '__main__':
    solve()
