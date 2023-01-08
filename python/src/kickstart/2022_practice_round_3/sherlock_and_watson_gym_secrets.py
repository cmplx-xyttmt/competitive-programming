import random
from collections import defaultdict
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


def brute_force(A, B, n, k):
    ans = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                continue
            if (mod_exp(i, A, k) + mod_exp(j, B, k)) % k == 0:
                ans += 1
    return ans


mod = int(1e9) + 7


def solution(A, B, n, k):
    remainders_a = [mod_exp(i, A, k) for i in range(k)]
    remainders_b = [mod_exp(i, B, k) for i in range(k)]
    # print(remainders_a)
    # print(remainders_b)
    b_count = defaultdict(int)
    for j in range(1, k + 1):
        b = remainders_b[j % k]
        if n >= j:
            b_count[b] += (n - j) // k + 1
        # j + u k <= n u = (n - j)/k
    ans = 0
    # ans_naive = 0
    for i in range(1, k + 1):
        a = remainders_a[i % k]
        if n >= i:
            x = (n - i) // k + 1
            y = b_count[(k - a) % k]
            # print(a, k - a, x, y, remainders_a[i % k], remainders_b[(k - a) % k])
            # print(a, k - a, x, y)
            ans = (ans + (x * y) % mod) % mod
            # ans_naive += x * y
            # if i == 4:
            #     print(remainders_b[i % k], (k - a) % k)
            if remainders_b[i % k] == (k - a) % k:
                # print(x)
                ans = (ans + mod - x) % mod
    return ans


def mod_exp(num, power, mod):
    ans = 1
    while power > 0:
        if power % 2 == 1:
            ans = (ans * num) % mod
        num = (num * num) % mod
        power //= 2

    return ans % mod


def test():
    for A in range(10):
        for B in range(10):
            for n in range(1, 30):
                for k in range(1, 30):
                    if brute_force(A, B, n, k) != solution(A, B, n, k):
                        print(A, B, n, k)
                        break


def solve():
    t = read_int()
    for test in range(t):
        A, B, n, k = read_ints()
        # brute_ans = brute_force(A, B, n, k)
        ans = solution(A, B, n, k)
        # print(f"Brute ans: {brute_ans}")
        print_(f"Case #{test + 1}: {ans}\n")


if __name__ == '__main__':
    solve()
    # test()
