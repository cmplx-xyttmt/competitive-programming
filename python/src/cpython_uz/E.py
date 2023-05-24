a = int(input())
b = int(input())

def get_primes(limit):
    primes = []
    sieve = [True] * (limit + 1)
    for i in range(2, limit + 1):
        if sieve[i]:
            primes.append(i)
            for comp in range(i * 2, limit + 1, i):
                sieve[comp] = False
    return primes

def get_prime_factors(n, primes):
    factors = []
    for p in primes:
        if n % p == 0:
            factors.append(p)
    return tuple(factors)


primes = get_primes(max(a, b))

print('Yes' if get_prime_factors(a, primes) == get_prime_factors(b, primes) else 'No')
