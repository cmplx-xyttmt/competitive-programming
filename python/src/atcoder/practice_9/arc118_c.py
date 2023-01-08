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
    primes = []
    is_prime = [True for _ in range(10000)]
    for i in range(2, len(is_prime)):
        if is_prime[i]:
            primes.append(i)
            for j in range(2 * i, len(is_prime), i):
                is_prime[j] = False

    max_num = int(1e4)
    coprime = {6, 10, 15}
    for prime in primes:
        new = set()
        for c in coprime:
            p = prime
            while c * p <= max_num:
                new.add(c * p)
                p *= prime
        coprime = coprime.union(new)
        if len(coprime) >= 2500:
            break

    coprime = list(coprime)
    coprime.sort()
    n = read_int()
    if n == 3:
        ans = "6 10 15"
    else:
        ans = ' '.join(map(str, coprime[:n]))
    print_(f"{ans}\n")


if __name__ == '__main__':
    solve()
