from typing import List
import sys

sys.stdin = open("day21.in", "r")
sys.stdout = open("day21.out", "w")
sys.setrecursionlimit(int(1e6))

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


numbers = dict()
depends = dict()
opp_ops = {'+': '-', '-': '+', '*': '/', '/': '*'}


def depends_on_humn(monk, instructions):
    if monk == 'humn':
        depends[monk] = True
        return True
    if monk in depends:
        return depends[monk]
    inst = instructions[monk]
    if len(inst) == 1:
        depends[monk] = False
        return depends[monk]

    left, right = inst[0], inst[2]
    # sys.stderr.write(f"{left} {right}\n")
    left_dep = depends_on_humn(left, instructions)
    right_dep = depends_on_humn(right, instructions)
    depends[monk] = left_dep or right_dep
    return depends[monk]


def topo_sort(monk, instructions, need, steps):
    if monk == 'humn':
        sys.stderr.write(f"to humn: {steps}\n")
        if need != 0:
            numbers[monk] = need
    if monk in numbers:
        return numbers[monk]
    inst = instructions[monk]

    if len(inst) == 1:
        numbers[monk] = int(instructions[monk][0])
        return numbers[monk]

    left, op, right = instructions[monk]
    left_dep = depends.get(left, False)
    right_dep = depends.get(right, False)
    # sys.stderr.write(f"{monk} -> {left_dep} {right_dep} {need}\n")
    if left_dep:
        right_val = topo_sort(right, instructions, 0, steps + 1)
        opp_op = opp_ops[op]
        if monk == "root":
            need = right_val
        else:
            need = eval(f"{need} {opp_op} {right_val}")
        left_val = topo_sort(left, instructions, need, steps + 1)
    elif right_dep:
        left_val = topo_sort(left, instructions, 0, steps + 1)
        # x = l / r
        # + -> r = x - l, - => l - x, * -> x / l, / ->  l / x
        opp_op = opp_ops[op]
        if op in ['+', '*']:
            need = eval(f"{need} {opp_op} {left_val}")
        else:
            need = eval(f"{left_val} {op} {need}")
        right_val = topo_sort(right, instructions, need, steps + 1)
    else:
        left_val = topo_sort(left, instructions, 0, steps + 1)
        right_val = topo_sort(right, instructions, 0, steps + 1)
    numbers[monk] = eval(f"{left_val} {op} {right_val}")
    return numbers[monk]


def solve():
    line = read_line()
    instructions = dict()
    while line:
        inst = line.replace(':', '').split()
        instructions[inst[0]] = inst[1:]
        line = read_line()

    # sys.stderr.write(f"{instructions}\n")
    print(f"Part 1: {topo_sort('root', instructions, 0, 0)}")

    depends_on_humn("root", instructions)
    # sys.stderr.write(f"{depends}\n")
    numbers.clear()
    eq = topo_sort('root', instructions, 0, 0)
    sys.stderr.write(f"Root val: {eq}\n")
    print(f"Part 2: {numbers['humn']}")


if __name__ == '__main__':
    solve()
