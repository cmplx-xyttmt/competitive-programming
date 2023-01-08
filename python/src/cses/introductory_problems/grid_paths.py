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
    path = read_line()
    seen = set()
    diff = {'D': (1, 0), 'U': (-1, 0), 'L': (0, -1), 'R': (0, 1)}
    size = 3

    def count_paths(index, r, c, p):
        if index == len(path):
            print(p)
            return int(r == size - 1 and c == 0)
        if r == size - 1 and c == 0:
            return 0
        # if c == size - 1:
        #     for i in range(r):
        #         for j in range(size):
        #             if (i, j) not in seen:
        #                 return 0
        # if r == size - 1:
        #     for i in range(size):
        #         for j in range(c + 1, size):
        #             if (i, j) not in seen:
        #                 return 0
        paths = 0
        if path[index] != '?':
            dr, dc = diff[path[index]]
            nr, nc = r + dr, c + dc
            if (0 <= nr < size and 0 <= nc < size) and (nr, nc) not in seen:
                seen.add((nr, nc))
                paths = count_paths(index + 1, nr, nc, p)
                seen.remove((nr, nc))
                return paths
            else:
                return 0

        for d, (dr, dc) in diff.items():
            nr, nc = r + dr, c + dc
            if (0 <= nr < size and 0 <= nc < size) and (nr, nc) not in seen:
                seen.add((nr, nc))
                p.append(d)
                paths += count_paths(index + 1, nr, nc, p)
                p.pop()
                seen.remove((nr, nc))
        return paths

    seen.add((0, 0))
    print_(f"{count_paths(0, 0, 0, [])}\n")


if __name__ == '__main__':
    solve()
