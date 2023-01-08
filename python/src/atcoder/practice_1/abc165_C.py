from typing import List
import sys

input_ = sys.stdin.readline
print_ = sys.stdout.write
flush = sys.stdout.flush


def readline() -> str:
    return input_().strip()


def read_int() -> int:
    return int(readline())


def read_strings() -> List[str]:
    return list(readline().split())


def read_ints():
    return list(map(int, readline().split()))


def sequences(n, m, curr_perm):
    if len(curr_perm) == n:
        return [curr_perm]
    sequence_list = []
    for nxt in range(curr_perm[-1], m + 1):
        sequence_list.extend(sequences(n, m, curr_perm + [nxt]))
    return sequence_list


def sequence_score(sequence, scores):
    score = 0
    for (a, b, c, d) in scores:
        if sequence[b - 1] - sequence[a - 1] == c:
            score += d

    return score


def solve():
    n, m, q = read_ints()
    scores = []
    for _ in range(q):
        a, b, c, d = read_ints()
        scores.append((a, b, c, d))

    print_(f"{max([sequence_score(sequence, scores) for sequence in sequences(n, m, [1])])}\n")


if __name__ == '__main__':
    solve()
