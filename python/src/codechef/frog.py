import math

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        weight = map(int, input().split(" "))
        length = map(int, input().split(" "))
        distance = range(1, n + 1)
        frogs = sorted(list(zip(weight, length, distance)), key=lambda x: x[0])
        ans = 0
        curr_position = frogs[0][2]
        for i in range(1, n):
            if frogs[i][2] > curr_position:
                curr_position = frogs[i][2]
            else:
                jumps = int(math.ceil((curr_position + 1 - frogs[i][2])/frogs[i][1]))
                ans += jumps
                curr_position = frogs[i][2] + jumps * frogs[i][1]
        print(ans)
