if __name__ == '__main__':
    n = int(input())
    x = list(map(int, input().split(" ")))
    x.sort()
    d = 0
    prev = 0
    for num in x:
        if num != prev:
            d += 1
            prev = num
    print(d)
