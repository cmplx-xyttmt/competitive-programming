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
    s = list(sorted(read_line()))
    all_on = (1 << len(s)) - 1
    ans = []

    def perms(curr_string, taken):
        if taken == all_on:
            ans.append(''.join(curr_string))
            return
        seen_chars = set()
        for i in range(len(s)):
            if not (taken & (1 << i)) and s[i] not in seen_chars:
                seen_chars.add(s[i])
                curr_string.append(s[i])
                perms(curr_string, taken | (1 << i))
                curr_string.pop()

    perms([], 0)
    print_(f"{len(ans)}\n")
    ans = '\n'.join(ans)
    print_(f"{ans}\n")


if __name__ == '__main__':
    solve()
