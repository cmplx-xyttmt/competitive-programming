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
    n, m, k, s, t, x = read_ints()
    adj = [[] for _ in range(n + 1)]
    mod = 998244353
    for _ in range(m):
        u, v = read_ints()
        adj[u].append(v)
        adj[v].append(u)

    ways_t = [[[0, 0] for _ in range(n + 1)] for _ in range(k + 1)]

    ways_t[0][t][0] = 1
    for length in range(1, k + 1):
        for u in range(1, n + 1):
            for v in adj[u]:
                if v == x:
                    ways_t[length][u][0] = (ways_t[length][u][0] + ways_t[length - 1][v][1]) % mod
                    ways_t[length][u][1] = (ways_t[length][u][1] + ways_t[length - 1][v][0]) % mod
                else:
                    ways_t[length][u][0] = (ways_t[length][u][0] + ways_t[length - 1][v][0]) % mod
                    ways_t[length][u][1] = (ways_t[length][u][1] + ways_t[length - 1][v][1]) % mod
    print_(f"{ways_t[k][s][0]}\n")


if __name__ == '__main__':
    solve()
