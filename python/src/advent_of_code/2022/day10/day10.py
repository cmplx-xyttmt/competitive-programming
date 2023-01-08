from typing import List
import sys

sys.stdin = open("day10.in", "r")
sys.stdout = open("day10.out", "w")

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


def draw_pixel(reg_val, cycle, crt):
    if reg_val - 1 <= ((cycle - 1) % 40) <= reg_val + 1:
        crt.append('#')
    else:
        crt.append('.')


def draw_crt(crt):
    for i in range(0, len(crt), 40):
        print(''.join(crt[i:i+40]))


def solve():
    line = read_line()
    cycle = 0
    next_interesting_cycle = 20
    reg_val = 1
    ans1 = 0
    crt = []
    while line:
        inst = line.split()
        if len(inst) == 1:
            cycle += 1
            draw_pixel(reg_val, cycle, crt)
            add = 0
        else:
            add = int(inst[1])
            draw_pixel(reg_val, cycle + 1, crt)
            # sys.stderr.write(f"{cycle + 1} -> {reg_val} {''.join(crt)}\n")
            draw_pixel(reg_val, cycle + 2, crt)
            # sys.stderr.write(f"{cycle + 2} -> {reg_val} {''.join(crt)}\n")
            cycle += 2
        if cycle >= next_interesting_cycle:
            ans1 += next_interesting_cycle * reg_val
            next_interesting_cycle += 40
        reg_val += add
        # reg_vals.add(reg_val)
        line = read_line()

    # sys.stderr.write(f"{reg_vals}\n")

    print(f"Part 1: {ans1}")
    print("Part 2: FECZELHE")
    draw_crt(crt)


if __name__ == '__main__':
    solve()
