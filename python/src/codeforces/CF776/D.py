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
        can = True
        ans = []
        for num in range(n, 1, -1):
            idx = a.index(num)
            if idx >= num:
                can = False
                break
            if idx + 1 == num:
                ans.append(f"0")
            else:
                a[:num] = a[idx + 1:num] + a[0:idx + 1]
                ans.append(f"{idx + 1}")
            # print(a)

        ans.append("0")

        for i in range(n):
            if a[i] != i + 1:
                can = False
                break

        if not can:
            print_(f"-1\n")
        else:
            ans = ans[::-1]
            print_(f"{' '.join(ans)}\n")


if __name__ == '__main__':
    solve()
