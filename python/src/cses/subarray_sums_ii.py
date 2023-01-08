from collections import defaultdict

if __name__ == '__main__':
    n, x = map(int, input().split(" "))
    a = list(map(int, input().split(" ")))

    p_sum = 0
    occur = defaultdict(lambda: 0)
    occur[0] = 1
    ans = 0
    for num in a:
        p_sum += num
        ans += occur[p_sum - x]
        occur[p_sum] += 1
    print(ans)
