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


vowels = {'a', 'e', 'i', 'o', 'u'}


def syllables(word):
    return sum([int(c in vowels) for c in word])


def is_spell(word):
    # i < len(word) - i
    for i in range(1, len(word)):
        if i >= len(word) - i:
            break
        start = word[:i]
        end = word[len(word) - i:]
        mid = word[i:len(word) - i]
        if start == end and syllables(start) >= 2 and syllables(mid) >= 1:
            return True
    return False


def solve():
    t = read_int()
    for test in range(1, t + 1):
        word = read_line()
        found_spell = False
        for length in range(5, len(word) + 1):
            for i in range(len(word)):
                if i + length > len(word):
                    break
                if is_spell(word[i:i + length]):
                    found_spell = True
                    break
            if found_spell:
                break
        print_(f"Case #{test}: {'Spell!' if found_spell else 'Nothing.'}\n")


if __name__ == '__main__':
    solve()
