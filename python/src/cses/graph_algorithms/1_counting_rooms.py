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


def bfs(node_r, node_c, building, room_no, n, m):
    diffs = [(0, -1), (0, 1), (1, 0), (-1, 0)]
    queue = [(node_r, node_c)]
    while queue:
        node_r, node_c = queue.pop()
        for dx, dy in diffs:
            nr, nc = node_r + dx, node_c + dy
            if 0 <= nr < n and 0 <= nc < m and building[nr][nc] == '.' and room_no[nr][nc] == -1:
                room_no[nr][nc] = room_no[node_r][node_c]
                queue.append((nr, nc))


def solve():
    n, m = read_ints()
    building = []
    for _ in range(n):
        building.append(read_line())
    room_no = [[-1 for _ in range(m)] for _ in range(n)]
    rooms = 0
    for r in range(n):
        for c in range(m):
            if building[r][c] == '.' and room_no[r][c] == -1:
                rooms += 1
                room_no[r][c] = rooms
                bfs(r, c, building, room_no, n, m)
    print(rooms)


if __name__ == '__main__':
    solve()
