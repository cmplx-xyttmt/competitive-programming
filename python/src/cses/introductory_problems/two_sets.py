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
    need = n * (n + 1)
    if need % 4 != 0:
        print_("NO\n")
        return

    need //= 4
    st = set()
    num = n
    while need > 0:
        take = min(num, need)
        st.add(take)
        num -= 1
        need -= take
    other = set(range(1, n + 1)).difference(st)
    print_("YES\n")
    print_(f"{len(st)}\n")
    print_(f"{' '.join(map(str, st))}\n")
    print_(f"{len(other)}\n")
    print_(f"{' '.join(map(str, other))}\n")


if __name__ == '__main__':
    solve()
