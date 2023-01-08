import functools
import random
from collections import defaultdict
from functools import cache
from typing import List
import sys
import threading
from tqdm import tqdm

sys.stdin = open("day16.in", "r")
sys.stdout = open("day16.out", "w")
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


adj, rates = dict(), dict()
adj_num = dict()
dists = defaultdict(dict)


def calc_dists():
    for valve in adj.keys():
        for valve2 in adj.keys():
            if valve == valve2:
                dists[valve][valve2] = 0
            elif valve2 in adj[valve]:
                dists[valve][valve2] = 1
            else:
                dists[valve][valve2] = float('inf')

    while True:
        improved = False
        for i in adj.keys():
            for j in adj.keys():
                for k in adj.keys():
                    if dists[i][k] + dists[k][j] < dists[i][j]:
                        improved = True
                        dists[i][j] = dists[i][k] + dists[k][j]
        if not improved:
            break


results = [0] * 10


def calc_pressure_2(order, i=0):
    # sys.stderr.write(f"{order}\n")
    time = 1
    total_pressure = 0
    curr_pressure = 0
    curr_valve = 'AA'
    taken_valves = 0
    for valve in order:
        dist = dists[curr_valve][valve]
        # sys.stderr.write(f"{dist}\n")
        if time + dist + 1 > 30:
            # sys.stderr.write(f"{valve} {order}\n")
            break
        total_pressure += curr_pressure * (dist + 1)
        curr_pressure += rates[valve]
        taken_valves += 1
        time += dist + 1
        # sys.stderr.write(f"{time}, {dist} -> {curr_pressure} {total_pressure}\n")
        curr_valve = valve
    total_pressure += (31 - time) * curr_pressure
    results[i] = max(results[i], total_pressure)
    return total_pressure, taken_valves


perms = []


def get_perms(valves, perm):
    if len(valves) == 0:
        calc_pressure_2(list(perm))
        # perms.append(list(perm))
    for i in range(len(valves)):
        perm.append(valves[i])
        get_perms(valves[:i] + valves[i + 1:], perm)
        perm.pop()


def get_order(subset):
    curr_valve = 'AA'
    order = []
    time_to_visit = 0
    while subset:
        nxt = min(subset, key=lambda x: dists[curr_valve][x] / rates[x])
        time_to_visit += dists[curr_valve][nxt] + 1
        order.append(nxt)
        subset.remove(nxt)
        curr_valve = nxt
    return order, time_to_visit


subsets = set()

debug = False


def get_subsets(size, valves, curr_subset, what=''):
    if debug:
        sys.stderr.write(f"{curr_subset} {valves} {what}\n")
    if 0 < len(curr_subset) <= size:
        subsets.add(tuple(curr_subset))
    if len(valves) == 0:
        return
    get_subsets(size, valves[1:], curr_subset.union({valves[0]}), f"{what} -> Take {valves[0]}" if debug else '')
    get_subsets(size, valves[1:], curr_subset.copy(), f"{what} -> Skip {valves[0]}" if debug else '')


def calc_pressure(curr_valve, time, open_valves, curr_pressure, total_pressure):
    if time == 30:
        sys.stderr.write(f"{time} -> {curr_valve} {open_valves} -> {curr_pressure} {total_pressure}\n")
        return total_pressure + curr_pressure
    open_valves = set(open_valves)
    best_pressure = 0

    if curr_valve != 'AA' and curr_valve not in open_valves:
        best_pressure = max(best_pressure, calc_pressure(curr_valve, time + 1,
                                                         tuple(sorted(open_valves.union({curr_valve}))),
                                                         curr_pressure + rates[curr_valve],
                                                         total_pressure + curr_pressure))

    for nxt in adj[curr_valve]:
        if nxt not in open_valves:
            best_pressure = max(best_pressure,
                                calc_pressure(nxt, time + 1, tuple(sorted(open_valves)),
                                              curr_pressure, total_pressure + curr_pressure))
            break

    return best_pressure


@functools.lru_cache(maxsize=None)
def max_flow(cur_me, opened, min_left, other_players):
    if min_left == 0:
        return 0 if other_players == 1 else max_flow(0, opened, 26, other_players - 1)
    best = 0
    if opened & (1 << cur_me) == 0:
        val = (min_left - 1) * rates[cur_me]
        cur_opened = opened | (1 << cur_me)
        if val != 0:
            best = max(best,
                       val + max_flow(cur_me, cur_opened, min_left - 1, other_players))
    for nxt in adj_num[cur_me]:
        best = max(best, max_flow(nxt, opened, min_left - 1, other_players))
        # sys.stderr.write(f"{cur}\n")
    return best


def solve():
    line = read_line()
    valve_to_num = dict()
    num = 0
    while line:
        split = line.replace(',', '').replace(';', '').replace('rate=', '').split()
        # sys.stderr.write(f"{split}\n")
        valve, rate = split[1], split[4]
        rates[num] = int(rate)
        adj[valve] = []
        i = 9
        valve_to_num[valve] = num
        while i < len(split):
            adj[valve].append(split[i])
            i += 1
        line = read_line()
        num += 1

    # sys.stderr.write(f"{adj}\n")
    # for adj_list in adj.values():
    #     adj_list.sort(key=lambda x: rates[x], reverse=True)
    for valve, adj_list in adj.items():
        adj_num[valve_to_num[valve]] = []
        for valve2 in adj_list:
            adj_num[valve_to_num[valve]].append(valve_to_num[valve2])

    calc_dists()
    print(f"Part 1: {max_flow(0, 0, 30, 1)}")
    print(f"Part 2: {max_flow(0, 0, 26, 2)}")
    # sys.stderr.write(f"{dists}\n")
    #
    # valves = list(adj.keys())
    # valves = [valve for valve in valves if valve != 'AA' and dists['AA'][valve] != float('inf') and rates[valve] != 0]
    #
    # sys.stderr.write(f"Non zero valves: {len([valve for valve in valves if rates[valve] != 0])}\n")
    # valves.sort(key=lambda x: rates[x], reverse=True)
    # sys.stderr.write(f"{[(valve, rates[valve]) for valve in valves]}\n")
    # # order = get_order(valves)
    # get_subsets(15, sorted(valves), set(), "start")
    # subsets_list = [list(sub) for sub in subsets]
    # sys.stderr.write(f"{len(subsets)} {sorted(subsets_list[:10])}\n")
    # sys.stderr.write(f"Lengths of subsets: {set([len(sub) for sub in subsets_list])}\n")
    # best_pressure = 0
    # max_taken_valves = 0
    # subs_less_8 = [sub for sub in subsets_list if len(sub) <= 8]
    # subsets_to_visit = [sub for sub in subsets_list if len(sub) == 10]
    # # subsets_to_visit.sort(key=lambda sub: len(sub))
    # sys.stderr.write(f"Subsets that can all be visited: {len(subsets_to_visit)}\n")
    # sys.stderr.write(f"Lengths of subsets to visit: {set([len(sub) for sub in subsets_to_visit])}\n")
    # # for subset in subsets_to_visit:
    # #     order, time_to_visit = get_order(subset)
    # #     pressure, taken_valves = calc_pressure_2(order)
    # #     best_pressure = max(best_pressure, pressure)
    # #     max_taken_valves = max(taken_valves, max_taken_valves)
    # # sys.stderr.write(f"Max taken valves: {max_taken_valves} \nSubsets with length less than 8: {len(subs_less_8)}\n")
    #
    # for k in tqdm(range(len(subsets_to_visit))):
    #     subset = subsets_to_visit[k]
    #     perms.clear()
    #     get_perms(subset, [])
    #     # sys.stderr.write(f"\nLength of perms: {len(perms)}\n")
    #     if k % 100 == 0:
    #         sys.stderr.write(f"\nCurr best: {max(results)}\n")
    #     # for i in range(len(perms)):
    #     #     results[0] = max(results[0], calc_pressure_2(perms[i], 0)[0])
    #     # # for i in range(0, len(perms), 10):
    #     # #     threads = [threading.Thread(target=calc_pressure_2, args=(perms[j], j % 10))
    #     # #                for j in range(i, min(len(perms), i + 10))]
    #     # #     for thread in threads:
    #     # #         thread.start()
    #     # #     # sys.stderr.write(f"What's happening: -> {results}\n")
    #     #     if i % 1000000 == 0:
    #     #         sys.stderr.write(f"\nPerm group: {i} -> Curr best: {max(results)}\n")
    #
    #         # best_pressure = max(best_pressure, calc_pressure_2(perm))
    # print(f"Part 1: {max(results)}")
    # # print(f"Part 1: {calc_pressure_2(['DD', 'BB', 'JJ', 'HH', 'EE', 'CC'])}")
    # # 1635
    # # seen = {'AA'}


if __name__ == '__main__':
    solve()
