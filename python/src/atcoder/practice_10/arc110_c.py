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
    n = read_int()
    p = [0] + read_ints()
    curr_index = [0 for _ in range(n + 1)]
    for i, num in enumerate(p):
        curr_index[num] = i

    ops = []
    seen = set()
    can = True
    for num in range(n, 0, -1):
        while curr_index[num] != num:
            prev_idx = curr_index[num]
            if prev_idx in seen:
                can = False
                break
            new_idx = prev_idx + 1
            replaced = p[new_idx]
            p[prev_idx], p[new_idx] = replaced, num
            curr_index[num] = new_idx
            curr_index[replaced] = prev_idx
            ops.append(prev_idx)
            seen.add(prev_idx)
        if not can:
            break

    can = can and len(ops) == n - 1
    ans = '\n'.join(map(str, ops))
    print_(f"{ans if can else -1}\n")


if __name__ == '__main__':
    solve()
