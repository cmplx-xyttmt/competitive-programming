from collections import deque


if __name__ == '__main__':
    n, m = map(int, input().split())

    building = []
    for _ in range(n):
        building.append(list(input()))
    rooms = 0
    for i in range(n):
        for j in range(m):
            if building[i][j] == '.':
                rooms += 1
                q = deque()
                q.append((i, j))
                building[i][j] = '#'
                while q:
                    x, y = q.popleft()
                    for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                        new_x, new_y = x + dx, y + dy
                        if 0 <= new_x < n and 0 <= new_y < m and building[new_x][new_y] == '.':
                            building[new_x][new_y] = '#'
                            q.append((new_x, new_y))

    print(rooms)
