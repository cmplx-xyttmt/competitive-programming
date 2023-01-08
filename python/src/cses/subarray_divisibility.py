from collections import defaultdict

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split(" ")))

    occur = defaultdict(lambda: 0)
    rem = 0
    occur[0] = 1
    ans = 0
    for num in a:
        rem = (rem + num) % n
        ans += occur[rem]
        occur[rem] += 1

    print(ans)
