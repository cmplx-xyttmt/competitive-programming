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
    s = read_line()
    ans = [''] * len(s)
    chs = [0] * 26
    for c in s:
        chs[ord(c) - ord('A')] += 1
    odds = 0
    odd_index = -1
    for i in range(26):
        if chs[i] % 2 == 1:
            odds += 1
            odd_index = i

    if odds > 1:
        print_("NO SOLUTION\n")
        return

    left, right = 0, len(s) - 1
    for i in range(26):
        if i == odd_index:
            continue
        c = chr(ord('A') + i)
        while chs[i] > 0:
            ans[left] = ans[right] = c
            left += 1
            right -= 1
            chs[i] -= 2

    if odd_index >= 0:
        c = chr(ord('A') + odd_index)
        while chs[odd_index] > 0:
            ans[left] = ans[right] = c
            left += 1
            right -= 1
            chs[odd_index] -= 2

    print_(f"{''.join(ans)}\n")


if __name__ == '__main__':
    solve()
