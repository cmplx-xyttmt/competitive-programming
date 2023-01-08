from collections import deque


if __name__ == '__main__':
    n, m = map(int, input().split())
    row_source, column_source = -1, -1
    x_b, y_b = -1, -1
    lab = []
    for i in range(n):
        lab.append(list(input()))
        for j in range(m):
            if lab[i][j] == 'A':
                row_source, column_source = i, j
            if lab[i][j] == 'B':
                x_b, y_b = i, j

    directions = [(-1, 0, 'U'), (0, 1, 'R'), (1, 0, 'D'), (0, -1, 'L')]
    q = deque()
    q.append((row_source, column_source))
    lab[row_source][column_source] = '#'
    found = False
    while q:
        x, y = q.popleft()
        if x == x_b and y == y_b:
            found = True
            break
        for dx, dy, d in directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < n and 0 <= new_y < m and (lab[new_x][new_y] == '.' or lab[new_x][new_y] == 'B'):
                lab[new_x][new_y] = d
                q.append((new_x, new_y))

    if found:
        ans = []
        while lab[x_b][y_b] != '#':
            c = lab[x_b][y_b]
            ans.append(c)
            if c == 'L':
                y_b += 1
            elif c == 'R':
                y_b -= 1
            elif c == 'U':
                x_b += 1
            else:
                x_b -= 1
        ans = "".join(reversed(ans))
        print("YES")
        print(len(ans))
        print(ans)
    else:
        print("NO")
