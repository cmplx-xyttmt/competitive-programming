import sys

sys.stdin = open("whereami.in", "r")
sys.stdout = open("whereami.out", "w")


if __name__ == '__main__':
    n, m = map(int, input().split(" "))
    cows = list(map(int, input().split(" ")))
