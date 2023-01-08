from typing import List
import sys
from collections import  deque

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


def get_nxt_strings(string, nxt_ch):
    nxt_strings = []
    for i in range(len(string)):
        if string[i] == '':
            string[i] = nxt_ch
            break

    q = deque()
    q.append((1, string))
    while q:
        idx, string = q.popleft()
        if idx == len(string):
            nxt_strings.append(string)
            continue
        if string[idx] == '':
            q.append((idx + 1, string))
            copy = list(string)
            copy[idx] = nxt_ch
            q.append((idx + 1, copy))
        else:
            q.append((idx + 1, string))

    return nxt_strings


def next_strings(curr_strings, nxt_ch):
    nxt = []
    for string in curr_strings:
        nxt.extend(get_nxt_strings(string, nxt_ch))
    return nxt


def solve():
    n = read_int()
    curr = [['' for _ in range(n)]]
    for i in range(n):
        curr = next_strings(curr, chr(ord('a') + i))
    curr = [''.join(string) for string in curr]
    curr.sort()
    ans = '\n'.join(curr)
    print_(f"{ans}\n")


def solve2():
    n = read_int()

    def dfs(curr):
        mx = -1
        for c in curr:
            if ord(c) - ord('a') > mx:
                mx = ord(c) - ord('a')
        if len(curr) == n:
            print_(f"{curr}\n")
        else:
            for i in range(0, mx + 2):
                dfs(curr + chr(ord('a') + i))

    dfs('')


if __name__ == '__main__':
    solve2()
