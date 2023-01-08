import bisect
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
    # take first as far back as it can go: best, set prev = first, prev_best = best, reduce k
    # for all nxt:
    #     if nxt <= prev_best: binary search for its position
    #     if prev_best < nxt <= prev: set it to prev_best; don't reduce k
    #     if nxt > prev:
    #           if possible to set it to prev, reduce k, set it to prev_best. set prev = nxt
    #           else: set it as far as it can go, k = 0, prev = nxt prev_best = nxt
    t = read_int()
    for _ in range(t):
        n, k = read_ints()
        s = read_line()
        ords = [ord(c) - ord('a') for c in s]
        prev, best = [ords[0]], [max(0, ords[0] - k)]
        k -= (prev[0] - best[0])
        ans = [chr(ord('a') + best[0])]
        for i in range(1, n):
            if ords[i] <= best[-1]:
                # print(s, s[i], prev)
                idx = bisect.bisect_left(prev, ords[i])
                if best[idx] < ords[i]:
                    ans.append(chr(ord('a') + best[idx]))
                else:
                    ans.append(chr(ord('a') + ords[i]))
            elif best[-1] < ords[i] <= prev[-1]:
                ans.append(chr(ord('a') + best[-1]))
            else:
                # print(s, s[i], k)
                n_best = max(prev[-1], ords[i] - k)
                if n_best > prev[-1]:
                    prev.append(ords[i])
                    best.append(n_best)
                    ans.append(chr(ord('a') + best[-1]))
                    k -= (prev[-1] - best[-1])
                else:
                    ans.append(chr(ord('a') + best[-1]))
                    prev.append(ords[i])
                    best.append(best[-1])
                    k -= (ords[i] - n_best)

        print(f"{''.join(ans)}")


if __name__ == '__main__':
    solve()
