from math import factorial


def p_occurs(p, num):
    occ = 0
    power = p
    while num // power > 0:
        occ += num // power
        power *= p
    return occ


def prime_factorise(num):
    factors = dict()
    p = 2
    while p * p <= num:
        if num % p == 0:
            factors[p] = 0
            while num % p == 0:
                factors[p] += 1
                num //= p
        p += 1
    if num > 1:
        factors[num] = 1
    return factors


def divides_brute(a, b):
    if b == 0:
        return False
    return factorial(a) % b == 0


def divides_sol(a, b):
    primes = prime_factorise(b)
    # print(primes, p_occurs(2, a))
    divides = True and b != 0
    for prime, occur in primes.items():
        if p_occurs(prime, a) < occur:
            divides = False
            break
    return divides


def stress():
    found = False
    for a in range(1001):
        for b in range(1001):
            if divides_brute(a, b) != divides_sol(a, b):
                print(a, b)
                found = True
                break
        if found:
            break


if __name__ == '__main__':
    # stress()
    line = input()
    while line:
        n, m = map(int, line.split())
        divs = divides_sol(n, m)
        print(f"{m} {'divides' if divs else 'does not divide'} {n}!")
        try:
            line = input()
        except Exception as e:
            break
