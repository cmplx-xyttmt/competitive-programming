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


def num_of_emotes(messages, k):
    if messages > k:
        total_emotes = (k * (k + 1) ) // 2 + (k * (k - 1)) // 2
        remainder = 2 * k - 1 - messages
        remainder_emotes = (remainder * (remainder + 1)) // 2
        return total_emotes - remainder_emotes
    else:
        return (messages * (messages + 1)) // 2


def solve():
    # emotes >= x -> banned
    # emotes < x -> not yet banned
    tests = read_int()
    ans = []
    for _ in range(tests):
        k, x = read_ints()
        # messages -> 0..2k - 1
        lo = 0
        hi = 2 * k - 1
        if num_of_emotes(hi, k) < x:
            ans.append(hi)
            continue
        while hi - lo > 1:
            mid = (lo + hi) // 2
            if num_of_emotes(mid, k) < x:
                lo = mid
            else:
                hi = mid
        ans.append(hi)
    ans = '\n'.join(map(str, ans))
    print_(ans)


if __name__ == '__main__':
    solve()
