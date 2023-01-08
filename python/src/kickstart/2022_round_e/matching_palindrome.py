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


def char_to_int(char):
    return ord(char) - ord('a') + 1


def mod_pow(x, n, m):
    res = 1
    while n > 0:
        if n % 2 == 1:
            res = (res * x) % m
        x = (x * x) % m
        n //= 2
    return res % m


def mod_inverse(x, m):
    return mod_pow(x, m - 2, m)


def solve():
    t = read_int()
    p = 31
    mod = int(1e9) + 7
    p_mod_inverse_m = mod_inverse(p, mod)
    p_mod_inverse_builtin = pow(p, -1, mod)
    print(p_mod_inverse_m, p_mod_inverse_builtin)
    for test in range(t):
        n = read_int()
        s = read_line()
        rev_s = ''.join(reversed(s))
        p_pow = [1]
        hash_s = 0
        hash_rev_s = 0
        for i in range(n):
            hash_s = (hash_s * p + char_to_int(s[i])) % mod
            hash_rev_s = (hash_rev_s * p + char_to_int(rev_s[i])) % mod
            if i != n - 1:
                p_pow.append((p * p_pow[-1]) % mod)

        # print(p_pow, hash_s, hash_rev_s)
        ans_index = n - 1
        hash_prefix = 0
        hash_prefix_rev = 0
        for i in range(0, n):
            hash_s = (hash_s + mod - (p_pow[-(i + 1)] * char_to_int(s[i])) % mod) % mod
            hash_rev_s = (hash_rev_s + mod - char_to_int(s[i])) % mod
            hash_rev_s = (hash_rev_s * p_mod_inverse_m) % mod
            # print(hash_s, hash_rev_s)

            hash_prefix = (hash_prefix * p + char_to_int(s[i])) % mod
            hash_prefix_rev = (hash_prefix_rev + (p_pow[i] * char_to_int(s[i])) % mod) % mod

            if hash_prefix == hash_prefix_rev and hash_s == hash_rev_s:
                ans_index = i
                break
        print_(f"Case #{test + 1}: {''.join(reversed(s[:ans_index + 1]))}\n")


if __name__ == '__main__':
    solve()
