import sys

sys.stdin = open('input.in', 'r')

input = sys.stdin.readline


if __name__ == '__main__':
    bin_numbers = []
    num = input()
    while num:
        bin_numbers.append(num)
        num = input()

    gamma_rate = 0
    epsilon_rate = 0
    for pos in range(0, len(bin_numbers[0])):
        zeros = 0
        ones = 0
        for num in bin_numbers:
            if num[pos] == '0':
                zeros += 1
            else:
                ones += 1
        if zeros > ones:
            gamma_rate *= 2
            epsilon_rate = (epsilon_rate * 2) + 1
        else:
            gamma_rate = (gamma_rate * 2) + 1
            epsilon_rate *= 2
    gamma_rate //= 2
    epsilon_rate //= 2
    print(f"Part 1: {gamma_rate * epsilon_rate}")
