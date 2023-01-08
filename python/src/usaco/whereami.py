import sys

sys.stdin = open("whereami.in", "r")
sys.stdout = open("whereami.out", "w")

if __name__ == '__main__':
    n = int(input())

    string = input()

    for k in range(1, n + 1):
        unique_substrs = set()
        expected = n - k + 1
        for i in range(0, expected):
            unique_substrs.add(string[i:i + k])
        if len(unique_substrs) == expected:
            print(k)
            break
