from typing import List, Set
import time


def sieve(n: int):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for prime in range(2, n + 1):
        if is_prime[prime]:
            for num in range(prime * 2, n + 1, prime):
                is_prime[num] = False

    return [prime for prime in range(n + 1) if is_prime[prime]]


def get_prime_squares(primes: List[int]):
    return [prime ** 2 for prime in primes]


def is_reversible(num: int, prime_squares: Set[int]):
    rev = int(''.join(list(reversed(str(num)))))
    # print(rev)
    return rev != num and rev in prime_squares


def solve():
    time_start = time.time()
    primes = sieve(100_000_000)
    print(f"Number of primes: {len(primes)}")
    prime_squares = get_prime_squares(primes)
    prime_square_set = set(prime_squares)
    # print(is_reversible(169, prime_square_set))
    reversible_prime_squares = []
    for prime_sq in prime_squares:
        if is_reversible(prime_sq, prime_square_set):
            # print(prime_sq)
            reversible_prime_squares.append(prime_sq)
    print(len(reversible_prime_squares))
    print(sum(reversible_prime_squares))
    time_end = time.time()
    print(f"Time taken: {int((time_end - time_start) * 1000)}ms")


if __name__ == '__main__':
    solve()
