def get_repeats(amount, x):
    reps, rem = divmod(amount, x)
    if rem == 0:
        reps -= 1
    return reps


if __name__ == '__main__':
    t = int(input())

    for case in range(1, t + 1):
        n, x = map(int, input().split())
        a = map(int, input().split())
        b = [(get_repeats(amount, x), i + 1) for (i, amount) in enumerate(a)]
        b.sort()
        print(f"Case #{case}:", " ".join(map(lambda bi: str(bi[1]), b)))
