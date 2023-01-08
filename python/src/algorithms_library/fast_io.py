# renaming the read/write methods
import sys

input = sys.stdin.readline
print = sys.stdout.write

if __name__ == '__main__':
    print(str(list(map(int, input().split(" ")))))
