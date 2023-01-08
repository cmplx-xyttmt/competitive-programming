if __name__ == '__main__':
    n = int(input())
    INF = float('inf')
    steps = [INF for _ in range(n + 1)]
    steps[0] = 0
    for num in range(n + 1):
        for ch in str(num):
            d = int(ch)
            steps[num] = min(steps[num], 1 + steps[num - d])
    print(steps[n])
