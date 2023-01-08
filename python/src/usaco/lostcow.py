import sys

sys.stdin = open("lostcow.in", "r")
sys.stdout = open("lostcow.out", "w")

input_ = sys.stdin.readline
print_ = sys.stdout.write
flush = sys.stdout.flush


def solve():
    x, y = map(int, input_().strip().split())
    jump = 1
    distance = 0
    curr = x
    forward = True
    while curr != y:
        prev = curr
        if forward:
            curr = x + jump
            if prev < y <= curr:
                curr = y
        else:
            curr = x - jump
            if curr <= y < prev:
                curr = y
        sys.stderr.write(f"{prev} {curr} {jump}\n")
        jump *= 2
        distance += abs(curr - prev)
        forward = not forward

    print_(f"{distance}\n")


if __name__ == '__main__':
    solve()
