if __name__ == '__main__':
    n = int(input())
    ways = [0 for _ in range(n + 1)]
    ways[0] = 1
    MOD = int(1e9) + 7
    for num in range(1, n + 1):
        for r in range(1, 7):
            if num - r >= 0:
                ways[num] = (ways[num] + ways[num - r]) % MOD

    print(ways[n])
