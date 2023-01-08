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
    t = read_int()
    for case in range(1, t + 1):
        read_int()
        s = read_strings()
        ch_to_strs = defaultdict(list)
        nodes = []
        for si in s:
            if si[0] * len(si) == si:
                ch_to_strs[si[0]].append(si)
            else:
                nodes.append(si)

        for words in ch_to_strs.values():
            nodes.append(''.join(words))

        # print(nodes)
        adj = [[] for _ in range(len(nodes))]
        starters = {i for i in range(len(nodes))}
        for i in range(len(nodes)):
            for j in range(len(nodes)):
                if i != j and nodes[i][-1] == nodes[j][0]:
                    adj[i].append(j)
                    if j in starters:
                        starters.remove(j)

        # print(nodes)
        # print(adj)

        topo = []
        seen = set()

        def topo_sort(u):
            seen.add(u)
            for v in adj[u]:
                if v not in seen:
                    topo_sort(v)
            topo.append(u)

        # print(starters)
        for start in starters:
            topo_sort(start)
        for start in range(len(nodes)):
            if start not in seen:
                topo_sort(start)
        ans = ''.join([nodes[i] for i in topo[::-1]])
        prev = ''
        seen = set()
        is_good = True
        for c in ans:
            if prev != c:
                if prev in seen:
                    is_good = False
                    break
                seen.add(prev)
                prev = c
        if prev in seen:
            is_good = False
        # print(ans)
        print_(f"Case #{case}: {ans if is_good else 'IMPOSSIBLE'}\n")


if __name__ == '__main__':
    solve()
