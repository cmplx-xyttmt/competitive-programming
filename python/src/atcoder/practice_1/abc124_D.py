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


def can(ones, zeros, consec, k):
    for i in range(len(ones)):
        if i + consec >= len(ones):
            break
        if ones[i + consec] - ones[i] + 1 <= k or zeros[i + consec] - zeros[i] <= k:
            return True

    return False


def solve():
    n, k = read_ints()
    s = readline()
    # 11101010110011
    ones = [0]
    zeros = [0]
    prev = ''
    for i in range(n):
        c = s[i]
        if c != prev:
            if c == '0':
                ones.append(ones[-1])
                zeros.append(zeros[-1] + 1)
            else:
                ones.append(ones[-1] + 1)
                zeros.append(zeros[-1])
        else:
            ones.append(ones[-1])
            zeros.append(zeros[-1])
        prev = c
    lo, hi = 0, n + 1
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if can(ones, zeros, mid, k):
            lo = mid
        else:
            hi = mid

    print_(f"{lo}\n")


if __name__ == '__main__':
    solve()
