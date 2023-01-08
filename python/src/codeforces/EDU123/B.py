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


def has_fib(perm):
    for i in range(2, len(perm)):
        if perm[i - 2] + perm[i - 1] == perm[i]:
            return True

    return False


def solve():
    t = read_int()

    for _ in range(t):
        n = read_int()
        curr_perm = [n - i for i in range(0, n)]
        perms = [' '.join(map(str, curr_perm))]
        int_perms = [curr_perm]
        while len(perms) < n:
            if curr_perm[-1] > curr_perm[-2]:
                curr_perm[-1], curr_perm[-2] = curr_perm[-2], curr_perm[-1]
                curr_perm = [curr_perm[-1]] + curr_perm[0:-1]
            else:
                curr_perm[-1], curr_perm[-2] = curr_perm[-2], curr_perm[-1]

            perms.append(' '.join(map(str, curr_perm)))
            int_perms.append(curr_perm)

        print('\n'.join(perms))
        # print(has_fib([1, 2, 3]))
        # print(len(set(perms)))
        # print(any([has_fib(perm) for perm in int_perms]))


if __name__ == '__main__':
    solve()
