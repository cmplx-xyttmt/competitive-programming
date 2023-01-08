from math import gcd


def mul():
    a = int(x)
    b = int(y)
    return (a * b) % n


def add():
    a = int(x)
    b = int(y)
    return (a + b) % n


def sub():
    a = int(x)
    b = int(y)
    return (a + n - b) % n


def extended_gcd(a, b):
    if b == 0:
        return 1, 0, a
    else:
        p, q, g = extended_gcd(b, a % b)
        return q, p - (a // b) * q, g


def mod_inverse(x, m):
    return extended_gcd(x, m)[0]


def div():
    a = int(x)
    b = int(y)
    if gcd(b, n) != 1 or b == 0:
        return -1
    return (a * mod_inverse(b, n)) % n


if __name__ == '__main__':
    line = input()
    while line:
        n, t = map(int, line.split())
        if n == 0:
            break
        for _ in range(t):
            x, op, y = input().split()
            if op == '+':
                print(add())
            elif op == '*':
                print(mul())
            elif op == '-':
                print(sub())
            else:
                print(div())
        line = input()
