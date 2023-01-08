import sys

sys.stdin = open('div7.in', 'r')
sys.stdout = open('div7.out', 'w')

input = sys.stdin.readline
print = sys.stdout.write

if __name__ == '__main__':
    n = int(input())
    prefix_sum = [0]
    rems = dict()
    ans = 0
    for i in range(n):
        num = int(input())
        rem = (num + prefix_sum[-1]) % 7
        prefix_sum.append(rem)
        if rem not in rems:
            rems[rem] = (i, i)
        else:
            rems[rem] = (rems[rem][0], i)
        ans = max(ans, rems[rem][1] - rems[rem][0])

    # sys.stderr.write(str(rems))
    print(str(ans if ans > 1 or 0 in rems else 0))
