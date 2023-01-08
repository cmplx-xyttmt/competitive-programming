import sys
from operator import itemgetter

sys.stdin = open("cowqueue.in", "r")
sys.stdout = open("cowqueue.out", "w")

if __name__ == '__main__':
    n = int(input())
    cows = []
    for _ in range(n):
        t, q = map(int, input().split(" "))
        cows.append((t, q))

    cows.sort(key=itemgetter(0))

    time = 0
    for (t, q) in cows:
        time = max(time, t) + q
    print(time)
