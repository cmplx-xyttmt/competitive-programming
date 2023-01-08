from collections import defaultdict, deque
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


MOD = 998244353


def mod_pow(x, n):
    if n == 0:
        return 1
    u = mod_pow(x, n // 2)
    u = (u * u) % MOD
    if n % 2 == 1:
        u = (u * (x % MOD)) % MOD

    return u


def max_product(x):
    occ = defaultdict(int)
    q = deque()
    occ[x] = 1
    q.append(x)
    final_nums = []
    while q:
        num = q.popleft()
        if num <= 4:
            final_nums.append(num)
            continue
        if num % 2 == 1:
            floor = (num - 1) // 2
            if occ[floor] == 0:
                q.append(floor)
            occ[floor] += occ[num]
            ceil = (num + 1) // 2
            if occ[ceil] == 0:
                q.append(ceil)
            occ[ceil] += occ[num]
        else:
            half = num // 2
            if occ[half] == 0:
                q.append(half)
            occ[num // 2] += 2 * occ[num]

    ans = 1
    for num in final_nums:
        ans = (ans * mod_pow(num, occ[num])) % MOD
    return ans


def solve():
    x = read_int()
    print(max_product(x))


if __name__ == '__main__':
    solve()
