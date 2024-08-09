from typing import List
import sys

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


def solve():
    t = read_int()
    for _ in range(t):
        a1, a2, b1, b2 = read_ints()
        suneet = [a1, a2]
        slavic = [b1, b2]
        ways = 0
        for i in range(2):
            for j in range(2):
                suneet_wins = 0
                slavic_wins = 0
                a = suneet[i]
                b = slavic[j]
                if a > b:
                    suneet_wins += 1
                elif a < b:
                    slavic_wins += 1
                a_other = suneet[(i + 1) % 2]
                b_other = slavic[(j + 1) % 2]
                if a_other > b_other:
                    suneet_wins += 1
                elif a_other < b_other:
                    slavic_wins += 1
                if suneet_wins > slavic_wins:
                    ways += 1
        print_(f"{ways}\n")


if __name__ == '__main__':
    solve()
