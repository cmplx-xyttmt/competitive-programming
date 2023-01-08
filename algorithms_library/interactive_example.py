import sys

input_ = sys.stdin.readline
print_ = sys.stdout.write
flush = sys.stdout.flush


def ask(guess):
    print_(f"{guess}\n")
    flush()
    return input_().strip()  # need strip here because the input comes with a new line appended


def solve():
    low = 0
    high = int(1e6)

    while high - low > 1:
        mid = (low + high) // 2
        sign = ask(mid)
        if sign == "<":
            low = mid
        else:
            high = mid
        flush()

    print_(f"! {high}\n")
    flush()


if __name__ == '__main__':
    solve()
