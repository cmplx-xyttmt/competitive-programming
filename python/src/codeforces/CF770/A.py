import sys

input_ = sys.stdin.readline
print_ = sys.stdout.write
flush = sys.stdout.flush


def solve():
    t = int(input_())

    for _ in range(t):
        n, k = map(int, input_().split())
        s = input_().strip()
        if s == s[::-1]:
            print_(f"1\n")
        else:
            ans = 1 if k == 0 else 2
            print_(f"{ans}\n")


if __name__ == '__main__':
    solve()
