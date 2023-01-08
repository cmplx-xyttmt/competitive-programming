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
    for _ in range(t):
        n = read_int()
        bigrams = read_strings()
        word = [bigrams[0]]
        found_gap = False
        for i in range(1, len(bigrams)):
            if bigrams[i][0] != word[-1][-1]:
                word.append(bigrams[i])
                found_gap = True
            else:
                word.append(bigrams[i][1])

        if not found_gap:
            word.append('a')
        print_(f"{''.join(word)}\n")


if __name__ == '__main__':
    solve()
