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


def solve():
    n, m = read_ints()
    adj = defaultdict(list)
    for _ in range(m):
        a, b = read_ints()
        adj[a].append(b)
        adj[b].append(a)
    impossible = False
    team = [0 for _ in range(n + 1)]
    for pupil in range(1, n + 1):
        if team[pupil]:
            continue
        stack = [pupil]
        team[pupil] = 1
        while stack:
            node = stack.pop()
            for nxt in adj[node]:
                if not team[nxt]:
                    team[nxt] = 1 if team[node] == 2 else 2
                    stack.append(nxt)
                elif team[nxt] == team[node]:
                    impossible = True
                    break
            if impossible:
                break
        if impossible:
            break
    if impossible:
        print("IMPOSSIBLE")
    else:
        print(f"{' '.join(map(str, team[1:]))}")


if __name__ == '__main__':
    solve()
