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


def solve():
    t = read_int()

    for case in range(t):
        n = read_int()
        f = [0] + read_ints()
        p = [0] + read_ints()
        non_initiators = set(p)
        queue = deque()
        inf = float('inf')
        values = [(0, inf) for _ in range(n + 1)]  # (sum, min)
        seen = set()

        for module in range(1, n + 1):
            if module not in non_initiators:
                queue.append(module)
                seen.add(module)

        ans = 0
        while queue:
            module = queue.popleft()
            # total, minimum = values[module]
            # print(module, total, minimum)
            # ans += total - (0 if minimum == inf else minimum)
            # curr_max = max(f[module], (0 if minimum == inf else minimum))
            nxt = p[module]
            # if nxt == 0 or nxt in seen:
            #     # ans += curr_max
            #     values[module] = (values[module][0] + f[module], min(values[module][1], f[module]))
            if nxt != 0:
                if nxt not in seen:
                    queue.append(nxt)
                    seen.add(nxt)
                values[nxt] = (values[nxt][0] + f[module], min(values[nxt][1], f[module]))

        for module in range(1, n + 1):
            total, minimum = values[module]
            if p[module] == 0:
                total += f[module]
                minimum = min(minimum, f[module])
                ans += minimum
            ans += total - (0 if minimum == inf else minimum)
        print_(f"Case #{case + 1}: {ans}\n")


if __name__ == '__main__':
    solve()
