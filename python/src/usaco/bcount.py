import sys

sys.stdin = open('bcount.in', 'r')
sys.stdout = open('bcount.out', 'w')

input = sys.stdin.readline
print = sys.stdout.write

if __name__ == '__main__':
    n, q = map(int, input().split(" "))
    breeds = [[0], [0], [0]]

    for i in range(n):
        cow = int(input())
        for b in range(3):
            breeds[b].append(breeds[b][-1] + (1 if b == cow - 1 else 0))
    for _ in range(q):
        l, r = map(int, input().split(" "))
        print(" ".join([str(breeds[b][r] - breeds[b][l - 1]) for b in range(3)]))
        print("\n")
