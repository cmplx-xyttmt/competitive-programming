from typing import List
import sys
from collections import deque

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


def get_path(b_coord, move_to):
    r, c = b_coord
    path = []
    while move_to[r][c] != '':
        mv = move_to[r][c]
        path.append(mv)
        if mv == 'L':
            c += 1
        elif mv == 'R':
            c -= 1
        elif mv == 'U':
            r += 1
        else:
            r -= 1
    return ''.join(reversed(path))


def bfs(labyrinth, n, m, a_coord, b_coord):
    diff = [(0, -1, 'L'), (0, 1, 'R'), (-1, 0, 'U'), (1, 0, 'D')]
    move = ''
    prev = None
    queue = deque()
    queue.append(a_coord)
    move_to = [['' for _ in range(m)] for _ in range(n)]
    while queue:
        r, c = queue.popleft()
        for dr, dc, mv in diff:
            nr, nc = r + dr, c + dc
            if (nr, nc) == a_coord:
                continue
            if 0 <= nr < n and 0 <= nc < m and labyrinth[nr][nc] != '#' and not move_to[nr][nc]:
                # n_prev = (r, c, mv)
                move_to[nr][nc] = mv
                if (nr, nc) == b_coord:
                    return get_path(b_coord, move_to)
                queue.append((nr, nc))
    return None


def solve():
    n, m = read_ints()
    labyrinth = []
    for _ in range(n):
        labyrinth.append(read_line())

    a_coord = None
    b_coord = None
    for r in range(n):
        for c in range(m):
            if labyrinth[r][c] == 'A':
                a_coord = (r, c)
            if labyrinth[r][c] == 'B':
                b_coord = (r, c)
    path = bfs(labyrinth, n, m, a_coord, b_coord)
    if path:
        print_("YES\n")
        print_(f"{len(path)}\n")
        print_(f"{path}\n")
    else:
        print_("NO\n")


if __name__ == '__main__':
    solve()
