class State:
    pass


if __name__ == '__main__':
    t = int(input())

    for case in range(1, t + 1):
        s, ra, pa, rb, pb, c = map(int, input().split())
        under_construction = []
        for _ in range(c):
            ri, pi = map(int, input().split())
            under_construction.append((ri, pi))
