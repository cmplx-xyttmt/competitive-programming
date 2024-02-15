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
    sub = read_line()
    sub_no_a = "".join([char for char in sub if char != 'A'])
    if sub_no_a != "KIHBR":
        print_("NO\n")
        return

    word = "AKIHABARA"
    sub_idx, word_idx = 0, 0
    while word_idx < len(word):
        if sub_idx < len(sub) and sub[sub_idx] == word[word_idx]:
            sub_idx += 1
            word_idx += 1
        elif word[word_idx] == "A":
            word_idx += 1
        else:
            break

    ans = "YES" if sub_idx == len(sub) else "NO"

    print_(f"{ans}\n")


if __name__ == '__main__':
    solve()
