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


def get_parent(a, parent):
    path = []
    while a != parent[a]:
        path.append(a)
        a = parent[a]

    for p in path:
        parent[p] = a

    return a


def union(a, b, parent, size, children, fall_time, time, initial):
    a, b = get_parent(a, parent), get_parent(b, parent)
    if a == b:
        return

    if a == 1 or size[a] > size[b]:
        a, b = b, a
    if b == 1:
        if not initial:
            seen = set()
            stack = [a]
            # print(f'{a} children -> ', children[a])
            # print('3 children ->', children[3])
            while stack:
                p = stack.pop()
                # print(f'{a} -> ', p)
                seen.add(p)
                fall_time[p] = time
                for c in children[p]:
                    if c not in seen:
                        stack.append(c)
    else:
        children[b].append(a)
    size[b] += size[a]
    parent[a] = b


def solve():
    n, m = read_ints()
    left = [-1 for _ in range(n + 1)]
    right = [-1 for _ in range(n + 1)]
    for i in range(1, n + 1):
        l, r = read_ints()
        left[i], right[i] = l, r

    releases = []
    releases_set = set()
    for _ in range(m):
        monkey, hand = read_ints()
        other_monkey = left[monkey] if hand == 1 else right[monkey]
        releases.append((monkey, other_monkey, hand))
        releases_set.add((monkey, other_monkey, hand))

    parent = [i for i in range(n + 1)]
    size = [0 for _ in range(n + 1)]
    children = [[i] for i in range(n + 1)]
    for i in range(1, n + 1):
        if left[i] != -1:
            u, v = i, left[i]
            if (u, v, 1) not in releases_set:
                union(u, v, parent, size, children, [], -1, True)
        if right[i] != -1:
            u, v = i, right[i]
            if (u, v, 2) not in releases_set:
                union(u, v, parent, size, children, [], -1, True)

    fall_time = [-1 for _ in range(n + 1)]
    for i, (u, v, _) in enumerate(releases[::-1]):
        union(u, v, parent, size, children, fall_time, m - i - 1, False)

    ans = [str(fall_time[i]) for i in range(1, n + 1)]
    ans = '\n'.join(ans)
    print_(f"{ans}\n")


if __name__ == '__main__':
    solve()
