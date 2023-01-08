from typing import List
import sys

sys.setrecursionlimit(int(1e6))


def dfs(course):
    status[course] = 1
    for dep in adj[course]:
        if status[dep] == 1:
            return False
        if status[dep] == 0 and not dfs(dep):
            return False

    ans.append(course)
    status[course] = 2
    return True


if __name__ == '__main__':
    n, m = map(int, input().split())
    adj: List[List[int]] = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b = map(int, input().split())
        adj[b].append(a)

    ans = []
    status = [0 for _ in range(n + 1)]  # 0 -> not done, 1 -> doing, 2 -> done
    can = True
    for i in range(1, n + 1):
        if status[i] != 2 and not dfs(i):
            can = False
            break

    if can:
        print(" ".join(map(str, ans)))
    else:
        print("IMPOSSIBLE")
