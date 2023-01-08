def get_factorials():
    factorials = [1 for _ in range(10 ** 6 + 1)]
    for i in range(1, len(factorials)):
        factorials[i] = (factorials[i - 1] * i) % mod
    return factorials


def mod_pow(x, n, m):
    if n == 0:
        return 1
    u = mod_pow(x, n // 2, m)
    u = (u * u) % m
    if n % 2 == 1:
        u = (u * x) % m
    return u


def mod_inverse(x, m):
    return mod_pow(x, m - 2, m)


def n_choose_k(n, k):
    return (_factorials[n] * mod_inverse((_factorials[k] * _factorials[n - k]) % mod, mod)) % mod


if __name__ == '__main__':
    mod = 10 ** 9 + 7
    _factorials = get_factorials()
    _n = int(input())
    output = []
    for _ in range(_n):
        a, b = map(int, input().split())
        output.append(str(n_choose_k(a, b)))
    print("\n".join(output))
