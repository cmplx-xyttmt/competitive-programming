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
    n, k = read_ints()

    mod = int(1e9) + 7

    partition = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    total = [0 for _ in range(n + 1)]

    for num in range(n + 1):
        new_total = [0 for _ in range(n + 1)]
        for i in range(n + 1):
            if num == 0:
                partition[num][i] = 1 if i == 0 else 0
            else:
                partition[num][i] = 0 if (i == 0 or i > num) else (total[i - 1]) % mod
            new_total[i] = total[i] + partition[num][i]
        total = new_total
    # print(partition)
    ans = []
    for i in range(1, k + 1):
        bi = partition[k][i]
        ri1m, ri, ri1a = partition[n - k][i - 1], partition[n - k][i], 0 if i + 1 > n else partition[n - k][i + 1]
        res = (bi * ri1m) % mod
        res = (res + (2 * bi * ri) % mod) % mod
        res = (res + (bi * ri1a) % mod) % mod
        # print(bi, ri1m, ri, ri1a)
        # print(bi * ri1m, bi * ri, bi * ri1a)
        ans.append(res)
    print('\n'.join(map(str, ans)))


if __name__ == '__main__':
    solve()
