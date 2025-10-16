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
    t = read_int()
    for _ in range(t):
        n, m, k = read_ints()
        s = read_line()
        win_cond = [''] + list(s)
        adj = [[] for _ in range(n + 1)]
        for _ in range(m):
            u, v = read_ints()
            adj[u].append(v)

        # backwards
        for moves in range(2 * k):
            new_win_cond = ['' for _ in range(n + 1)]
            for i in range(1, n + 1):
                if moves % 2 == 0:  # Bob
                    if any(map(lambda node: win_cond[node] == 'B', adj[i])):
                        new_win_cond[i] = 'B'
                    else:
                        new_win_cond[i] = 'A'
                else:  # Alice
                    if any(map(lambda node: win_cond[node] == 'A', adj[i])):
                        new_win_cond[i] = 'A'
                    else:
                        new_win_cond[i] = 'B'
            win_cond = new_win_cond

        print('Alice' if win_cond[1] == 'A' else 'Bob')


if __name__ == '__main__':
    solve()
