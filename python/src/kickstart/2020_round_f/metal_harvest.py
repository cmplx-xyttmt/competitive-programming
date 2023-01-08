from math import ceil

if __name__ == '__main__':
    t = int(input())
    for case in range(1, t + 1):
        n, k = map(int, input().split())
        intervals = []
        for _ in range(n):
            s, e = map(int, input().split())
            intervals.append((s, e))
        intervals.sort()
        endtime = intervals[0][0] + k
        deployments = 1
        for (s, e) in intervals:
            if e > endtime:
                dep_time = max(s, endtime)  # dep_time + a * k >= e  --> a = ceil((e - dep_time) / k)
                deps = ceil((e - dep_time) / k)
                deployments += deps
                endtime = dep_time + deps * k

        print(f"Case #{case}:", deployments)
