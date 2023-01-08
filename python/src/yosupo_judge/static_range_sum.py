if __name__ == "__main__":
    n, q = map(int, input().split(" "))

    a = list(map(int, input().split(" ")))

    prefix_sum = [0]

    for i in range(n):
        prefix_sum.append(a[i] + prefix_sum[-1])

    for j in range(q):
        l, r = map(int, input().split(" "))
        print(prefix_sum[r] - prefix_sum[l])
