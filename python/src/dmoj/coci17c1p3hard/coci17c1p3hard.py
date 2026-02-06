import resource
from collections import defaultdict
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
    q = read_int()
    passwords = defaultdict(int)
    for i in range(q):
        type_, pw = read_strings()
        seen = set()
        if type_ == "1":
            for start in range(len(pw)):
                substr_int = 0
                for end in range(start, len(pw)):
                    substr_int = (substr_int * 27) + (ord(pw[end]) - ord('a') + 1)
                    if substr_int not in seen:
                        passwords[substr_int] += 1
                    seen.add(substr_int)
        else:
            pw_int = 0
            for j in range(len(pw)):
                pw_int = (pw_int * 27) + (ord(pw[j]) - ord('a') + 1)
            print_(f"{passwords[pw_int]}\n")
            pass
        # if i % 1000 == 0:
        #     print_memory()
    # print(len(passwords))


def print_memory():
    # Returns memory usage in kilobytes
    usage = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    # On macOS, ru_maxrss is in bytes; on Linux, it's in kilobytes
    print(f"Memory usage: {usage / 1024:.2f} MB", file=sys.stderr)


if __name__ == '__main__':
    solve()
