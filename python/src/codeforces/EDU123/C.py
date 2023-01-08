from typing import List
import sys

input_ = sys.stdin.readline
print_ = sys.stdout.write
flush = sys.stdout.flush


def readline() -> str:
    return input_().strip()


def read_int() -> int:
    return int(readline())


def read_strings() -> List[str]:
    return list(readline().split())


def read_ints():
    return list(map(int, readline().split()))


def new_sum(ssum, length, x, k):
    return ssum + min(length, k) * x


def solve():
    t = read_int()
    INF = float('inf')

    for _ in range(t):
        n, x = read_ints()
        a = read_ints()
        prefix_sums = []
        for i in range(n):
            if i == 0:
                prefix_sums.append(a[i])
            else:
                prefix_sums.append(prefix_sums[-1] + a[i])
        subarray_sums = [(0, 0)]  # (sum, length)
        for l in range(1, n + 1):
            best = -INF
            for i in range(n):
                if i + l > n:
                    break
                prev_sum = 0 if i == 0 else prefix_sums[i - 1]
                ssum = prefix_sums[i + l - 1] - prev_sum
                best = max(best, ssum)

            subarray_sums.append((best, l))
        # print(subarray_sums)
        ans = []
        for k in range(n + 1):
            new_subarray_sums = [new_sum(ssum, length, x, k) for ssum, length in subarray_sums]
            ans.append(max(new_subarray_sums))

        print_(f"{' '.join(map(str, ans))}\n")


if __name__ == '__main__':
    solve()
