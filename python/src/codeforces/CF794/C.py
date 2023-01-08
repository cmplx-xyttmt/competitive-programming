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
        a = read_ints()
        if n % 2 == 1:
            print_("NO\n")
            continue
        a.sort()
        ans = [0 for _ in range(n)]
        j = 0
        half = n // 2
        for i in range(half):
            ans[j] = a[i]
            ans[j + 1] = a[half]
            half += 1
            j += 2
        # print(ans)
        correct = True
        for i in range(n):
            left = ans[(n + i - 1) % n]
            right = ans[(i + 1) % n]
            if (left > ans[i] and ans[i] < right) or (left < ans[i] and ans[i] > right):
                continue
            else:
                correct = False
                break

        if not correct:
            print_("NO\n")
            continue
        print_("YES\n")
        print_(f"{' '.join(map(str, ans))}\n")


if __name__ == '__main__':
    solve()
