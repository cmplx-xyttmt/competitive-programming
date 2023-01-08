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
    a = []
    for _ in range(n):
        a.append(read_int())
    print('second' if all(a[i] % 2 == 0 for i in range(n)) else 'first')  # correct answer

    # Below is a wrong answer, but it passed the test cases due to weak tests.
    # Fails for this case:
    # 3 3 6 9
    a.sort()
    heaps = []
    for i in range(n):
        apples = a[i]
        if i > 0:
            apples -= a[i - 1]
        heaps.append(n - i if apples % 2 == 1 else 0)

    ans = 0
    for heap in heaps:
        ans ^= heap

    print('first' if ans > 0 else 'second')


if __name__ == '__main__':
    solve()
