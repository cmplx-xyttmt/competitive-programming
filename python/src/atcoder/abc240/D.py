from typing import List
import sys

input_ = sys.stdin.readline
print_ = sys.stdout.write
flush = sys.stdout.flush


def readline() -> str:
    return input_().strip()


def read_int() -> int:
    return int(readline())


def read_strings() -> List[str]:
    return list(readline().split())


def read_ints():
    return list(map(int, readline().split()))


def solve():
    n = read_int()
    a = read_ints()
    ans = []
    stack = [(0, 0)]
    items = 0
    for num in a:
        top_num, top_occ = stack[-1]
        items += 1
        if top_num == num:
            stack.pop()
            top_occ += 1
            if top_occ < num:
                stack.append((num, top_occ))
            else:
                items -= top_occ
        else:
            stack.append((num, 1))
        ans.append(items)

    ans = '\n'.join(map(str, ans))
    print_(f"{ans}\n")


if __name__ == '__main__':
    solve()
