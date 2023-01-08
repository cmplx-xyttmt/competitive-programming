from typing import List


def bfs(city):
    q = [(city, city)]

    while q:
        city, fro = q.pop()
        prev[city] = fro
        for neighbor in adj[city]:
            if prev[neighbor] != 0 and neighbor != fro:
                # print(city, neighbor, prev[neighbor], prev[city])
                prev[neighbor] = city
                return city
            elif neighbor != fro:
                q.append((neighbor, city))

    return 0


if __name__ == '__main__':
    n, m = map(int, input().split())
    adj: List[List[int]] = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)

    prev = [0 for _ in range(n + 1)]
    start = 0
    for i in range(n + 1):
        if prev[i] == 0:
            cy = bfs(i)
            if cy != 0:
                start = cy
                break

    if start == 0:
        print("IMPOSSIBLE")
    else:
        ans = []
        seen = set()
        # print(prev)
        while start not in seen:
            seen.add(start)
            ans.append(start)
            start = prev[start]
        ans.append(start)
        print(len(ans))
        print(" ".join(map(str, ans)))
