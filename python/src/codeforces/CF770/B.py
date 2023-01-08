import sys

input_ = sys.stdin.readline
print_ = sys.stdout.write
flush = sys.stdout.flush


def solve():
    t = int(input_().strip())

    for _ in range(t):
        n, x, y = map(int, input_().strip().split())
        a = list(map(int, input_().strip().split()))
        alice, bob = x, x + 3


if __name__ == '__main__':
    solve()
