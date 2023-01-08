import sys
from queue import Queue

sys.stdin = open("angry.in", "r")
sys.stdout = open("angry.out", "w")

if __name__ == '__main__':
    n = int(input())
    hay = []
    for _ in range(n):
        hay.append(int(input()))
    hay.sort()
    ans = 0
    for i in range(n):
        queue = Queue()
        seen = {i}
        queue.put((i, 1))
        while not queue.empty():
            h, r = queue.get()
            for j in range(n):
                if j not in seen and abs(hay[j] - hay[h]) <= r:
                    seen.add(j)
                    queue.put((j, r + 1))
        ans = max(ans, len(seen))

    print(ans)
