from collections import defaultdict
from typing import List
import sys
import bisect

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
    a = read_ints()
    indices = defaultdict(list)
    for i, num in enumerate(a):
        indices[num].append(i + 1)
    # print(indices)
    q = read_int()
    ans = []
    for _ in range(q):
        l, r, x = read_ints()
        if x not in indices:
            ans.append(0)
        else:
            i = bisect.bisect_left(indices[x], l)
            j = bisect.bisect_right(indices[x], r)
            ans.append(j - i)
    ans = '\n'.join(map(str, ans))
    print_(ans)


if __name__ == '__main__':
    solve()
