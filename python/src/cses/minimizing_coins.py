if __name__ == '__main__':
    n, x = map(int, input().split())
    c = list(map(int, input().split()))
    INF = float('inf')
    needed = [INF for _ in range(x + 1)]
    needed[0] = 0
    for num in range(x + 1):
        if needed[num] == INF:
            continue
        # print(num)
        for coin in c:
            if num + coin <= x:
                needed[num + coin] = min(needed[num + coin], 1 + needed[num])

    if needed[x] == INF:
        print(-1)
    else:
        print(needed[x])
