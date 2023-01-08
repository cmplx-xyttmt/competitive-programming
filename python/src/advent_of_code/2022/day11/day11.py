from typing import List
import sys

sys.stdin = open("day11.in", "r")
sys.stdout = open("day11.out", "w")

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


divisors = [2, 3, 5, 7, 11, 13, 17, 19, 23]


def get_mod_rep(item):
    mod_rep = dict()
    for divisor in divisors:
        mod_rep[divisor] = item % divisor
    return mod_rep


def add(item1, item2):
    ans = dict()
    for divisor in divisors:
        ans[divisor] = (item1[divisor] + item2[divisor]) % divisor
    return ans


def mul(item1, item2):
    ans = dict()
    for divisor in divisors:
        ans[divisor] = (item1[divisor] * item2[divisor]) % divisor
    return ans


class Monkey:

    def __init__(self, id_, op, test, items):
        self.id = id_
        self.op = op
        self.test = test
        self.items = items
        self.inspected_items = 0

    def get_new_worry(self, old):
        left = old if self.op[0] == 'old' else get_mod_rep(int(self.op[0]))
        right = old if self.op[2] == 'old' else get_mod_rep(int(self.op[2]))
        if self.op[1] == '+':
            return add(left, right)
        return mul(left, right)

    def inspect(self, monkeys):
        my_items = self.items
        monkeys[self.id].items = []
        for item in my_items:
            new_w = self.get_new_worry(item)
            div, t, f = self.test
            if new_w[div] == 0:
                monkeys[t].items.append(new_w)
            else:
                monkeys[f].items.append(new_w)
            self.inspected_items += 1


def solve():
    lines = sys.stdin.readlines()
    lines = [line.strip() for line in lines]
    print_lines = '\n'.join(lines)
    # sys.stderr.write(f"{print_lines}\n")

    monkeys = []
    for i in range(0, len(lines), 7):
        items = list(map(int, lines[i + 1].replace(',', '').split()[2:]))
        dict_items = []
        for item in items:
            dict_items.append(get_mod_rep(item))

        operation = lines[i + 2].split()[3:]
        divisor = lines[i + 3].split()[3]
        true_case = lines[i + 4].split()[5]
        false_case = lines[i + 5].split()[5]

        monkey = Monkey(i // 7, operation, (int(divisor), int(true_case), int(false_case)), dict_items)
        monkeys.append(monkey)
        # sys.stderr.write(f"{items}\n")
        # sys.stderr.write(f"{operation} {divisor} {true_case} {false_case}\n")
        # sys.stderr.write(f"\n")

    for round_ in range(10000):
        for monkey in monkeys:
            monkey.inspect(monkeys)
        if round_ == 0 or (round_ + 1) % 20 == 0:
            sys.stderr.write(f"Round {round_ + 1}:\n")
            sys.stderr.write(f"{[monkey.inspected_items for monkey in monkeys]}\n")

    inspected_items = [monkey.inspected_items for monkey in monkeys]
    inspected_items.sort(reverse=True)
    sys.stderr.write(f"{inspected_items}\n")

    print(f"Part 2: {inspected_items[0] * inspected_items[1]}")
    # sys.stderr.write(f"{[monkey.items for monkey in monkeys]}")


if __name__ == '__main__':
    solve()
