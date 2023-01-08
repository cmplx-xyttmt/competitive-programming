if __name__ == '__main__':
    n, m = map(int, input().split())

    a = list(map(int, input().split()))

    ans = 0
    for ai in a:
        if m >= ai:
            m -= ai
        else:
            ans += 1

    print(ans)
