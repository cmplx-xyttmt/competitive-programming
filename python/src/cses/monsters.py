from typing import List
from collections import deque


if __name__ == '__main__':
    n, m = map(int, input().split())
    lab: List[List[str]] = []
    for _ in range(n):
        lab.append(list(input()))

    x, y = -1, -1
    q = deque()
    for i in range(n):
        for j in range(m):
            if lab[i][j] == 'A':
                x, y = i, j
            elif lab[i][j] == 'M':
                q.append((i, j, False))

    q.append((x, y, True))
    start_x, start_y = -1, -1
    while q:
        i, j, is_me = q.popleft()
        if (i == 0 or j == 0 or i == n - 1 or j == m - 1) and is_me:
            start_x, start_y = i, j
            break
        for dx, dy, d in [(0, 1, 'R'), (0, -1, 'L'), (1, 0, 'D'), (-1, 0, 'U')]:
            nx, ny = i + dx, j + dy
            if 0 <= nx < n and 0 <= ny < m and lab[nx][ny] == '.':
                if is_me:
                    lab[nx][ny] = d
                else:
                    lab[nx][ny] = '#'
                q.append((nx, ny, is_me))

    if start_x == -1:
        print("NO")
    else:
        x, y = start_x, start_y
        ans = []
        while lab[x][y] != 'A':
            c = lab[x][y]
            ans.append(c)
            if c == 'L':
                y += 1
            elif c == 'R':
                y -= 1
            elif c == 'U':
                x += 1
            else:
                x -= 1
        print("YES")
        print(len(ans))
        print("".join(reversed(ans)))
