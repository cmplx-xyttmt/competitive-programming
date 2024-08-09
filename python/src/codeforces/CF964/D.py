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
    T = read_int()
    for _ in range(T):
        s = read_line()
        s_list = list(s)
        t = read_line()
        t_index = 0
        for i in range(len(s)):
            if t_index < len(t) and (s[i] == t[t_index] or s[i] == '?'):
                s_list[i] = t[t_index]
                t_index += 1
            elif t_index == len(t) and s[i] == '?':
                s_list[i] = 'a'
        if t_index == len(t):
            print_("YES\n")
            print_(f"{''.join(s_list)}\n")
        else:
            print_("NO\n")


if __name__ == '__main__':
    solve()
