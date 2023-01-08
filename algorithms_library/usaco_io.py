import sys

sys.stdin = open('filename.in', 'r')
sys.stdout = open('filename.out', 'w')

input = sys.stdin.readline
print = sys.stdout.write
