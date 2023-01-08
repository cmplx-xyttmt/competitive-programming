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


def can_right(rest_time, a, d):
    prev = 0
    used = False
    for i in range(len(a)):
        curr = a[i]
        nxt = d + 1 if i == len(a) - 1 else a[i + 1]
        # print(prev, curr, nxt)
        if curr - prev < rest_time + 1:
            if used:
                return False
            curr = prev + rest_time + 1
            if curr >= nxt:
                return False
            used = True
        prev = curr

    return True


def can_left(rest_time, a):
    prev = a[-1]
    used = False
    for i in range(len(a) - 2, -1, -1):
        curr = a[i]
        nxt = 0 if i == 0 else a[i - 1]
        if prev - curr < rest_time + 1:
            if used:
                return False
            curr = prev - rest_time - 1
            if curr <= nxt or (i == 0 and curr - nxt < rest_time + 1):
                return False
            used = True
        # print(rest_time, f"{prev} {curr} {nxt}")
        prev = curr

    if prev < rest_time + 1:
        return False
    return True


def solve():
    t = read_int()

    for _ in range(t):
        read_line()
        n, d = read_ints()
        a = read_ints()
        left, right = 0, d
        # print(a, can_right(3, a, d))
        # print("=======")
        while right - left > 1:
            mid = (left + right) // 2
            # if can_right(mid, a, d):
            #     print("->", mid)
            if can_left(mid, a) or can_right(mid, a, d):
                left = mid
            else:
                right = mid

        print_(f"{left}\n")


if __name__ == '__main__':
    solve()
