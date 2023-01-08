import sys

input_ = sys.stdin.readline
print_ = sys.stdout.write
flush = sys.stdout.flush


def solve():
    t = int(input_().strip())

    for _ in range(t):
        r, c = map(int, input_().strip().split())
        prod = r * ((c * (c - 1)) // 2)
        if (c != 1 and (r * c) % 2 == 1) or prod % c != 0:
            print_("NO\n")
        else:
            print_("YES\n")
            ans = []
            for i in range(1, r + 1):
                ans.append([])
                for j in range(i, r * c + 1, r):
                    ans[i - 1].append(j)

            print_("\n".join(map(lambda row: " ".join(map(str, row)), ans)))
            print_("\n")


if __name__ == '__main__':
    solve()
