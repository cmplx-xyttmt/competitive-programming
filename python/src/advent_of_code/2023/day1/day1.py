from typing import List
import sys

sys.stdin = open("day1.in", "r")
sys.stdout = open("day1.out", "w")

input_ = sys.stdin.readline
print_ = sys.stdout.write
flush = sys.stdout.flush


def read_line() -> str:
    return input_().strip()


def read_int() -> int:
    return int(read_line())


def read_strings() -> List[str]:
    return list(read_line().split())


def read_ints():
    return list(map(int, read_line().split()))


def get_digits(string: str) -> List[int]:
    ints = list(map(lambda digit: int(digit), filter(lambda char: char.isdigit(), string)))
    return ints


word_to_digit = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

def extract_digit(substring: str):
    if substring.isdigit():
        return int(substring)
    elif substring in word_to_digit:
        return word_to_digit[substring]
    return None

def get_digits_with_words(string: str):
    digits = []
    for i in range(len(string)):
        for j in range(i, len(string)):
            digit = extract_digit(string[i:j+1])
            if digit:
                digits.append(digit)
    return digits


def solve():
    line = read_line()
    ans1 = 0
    ans2 = 0
    while line:
        digits1 = get_digits(line)
        calibration1 = int(f"{digits1[0]}{digits1[-1]}")
        ans1 += calibration1

        digits2 = get_digits_with_words(line)
        calibration2 = int(f"{digits2[0]}{digits2[-1]}")
        ans2 += calibration2
        line = read_line()
    print(ans1)
    print(ans2)


if __name__ == '__main__':
    solve()
    