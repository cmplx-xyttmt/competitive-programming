from collections import defaultdict
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



def can_remove(max_num, removed, numbers: List[int]):
    if len(numbers) == 1:
        return []
    num_map = defaultdict(int)
    for num in numbers:
        num_map[num] += 1
    num_map[removed] -= 1

    ans = []
    for num in numbers:
        if num_map[num] == 0:
            continue
        num_map[num] -= 1
        need = max_num - num
        if num_map[need]:
            ans.append((num, need))
            num_map[need] -= 1
            max_num = num
        else:
            return None
    return ans


def solve():
    t = read_int()

    for _ in range(t):
        n = read_int()
        a = read_ints()
        a.sort()
        max_num = a.pop()
        a.reverse()
        res = None
        for i in range(2 * n - 1):
            res = can_remove(max_num, a[i], a)
            if res is not None:
                res = [(max_num, a[i])] + res
                break

        if res:
            print_(f"YES\n")
            print_(f"{sum(res[0])}\n")
            ans = '\n'.join(map(lambda tup: f'{tup[0]} {tup[1]}', res))
            print_(f"{ans}\n")
        else:
            print_(f"NO\n")


if __name__ == '__main__':
    solve()
