from typing import List
import sys

sys.stdin = open("day17.in", "r")
sys.stdout = open("day17.out", "w")

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


def move(dx, dy, rock, filled_coordinates):
    new_pos = set()
    for x, y in rock:
        nx, ny = x + dx, y + dy
        if (0 <= nx < 7) and ny > 0 and (nx, ny) not in filled_coordinates:
            new_pos.add((nx, ny))
        else:
            return None
    return new_pos


def get_next_rock(time, y):
    rem = time % 5
    if rem == 1:
        return set([(x, y + 4) for x in range(2, 6)])
    elif rem == 2:
        return set([(x, y + 5) for x in range(2, 5)] + [(3, y + i) for i in range(4, 7)])
    elif rem == 3:
        return set([(x, y + 4) for x in range(2, 5)] + [(4, y + i) for i in range(4, 7)])
    elif rem == 4:
        return set([(2, y + i) for i in range(4, 8)])
    else:
        return set([(2, y + 4), (3, y + 4)] + [(2, y + 5), (3, (y + 5))])


def simulate(turns, pattern, start):
    filled_coordinates = set()
    y = 0
    idx = 0
    state = (1, idx, tuple([0] * 7))
    states = set()
    states.add(state)
    state_to_turn = dict()
    state_to_turn[state] = (1, 0)  # turn, height of leftmost column
    turn_to_state = dict()
    turn_to_state[0] = state
    rep_turn = 0
    rep_state = None
    height_diff = 0
    for turn in range(start, turns + start):
        rock = get_next_rock(turn, y)
        last_rock = rock
        alt = True
        while rock:
            if alt:
                rock = move(-1 if pattern[idx] == '<' else 1, 0, rock, filled_coordinates)
                if not rock:
                    rock = last_rock
                idx = (idx + 1) % len(pattern)
            else:
                rock = move(0, -1, rock, filled_coordinates)
                if not rock:
                    break
            last_rock = rock
            alt = not alt
        filled_coordinates = filled_coordinates.union(last_rock)

        y = max([ny for _, ny in filled_coordinates])

        highest = [0] * 7
        for x in range(len(highest)):
            highest[x] = max([0] + [ny for nx, ny in filled_coordinates if nx == x])
        # if turn >= 98:
        #     sys.stderr.write(f"Yello: {highest}\n")
        state = (turn % 5, idx, tuple([h - highest[0] for h in highest]))
        if 28 <= turn <= 36 or 63 <= turn <= 71:
            sys.stderr.write(f"{turn} -> {state} height={highest[0]}\n")
        if state in states and height_diff == 0:
            rep_turn = turn
            rep_state = state
            height_diff = highest[0] - state_to_turn[state][1]
            sys.stderr.write(f"{turn} -> {state} Repeats: {state_to_turn[state][0]}, height={highest[0]}\n")
            # after 64 turns, everything from the 29th rock repeats
            if state in states:
                break
            # if state_to_turn[state] == 34:
            #     break
        if height_diff == 0:
            states.add(state)
            state_to_turn[state] = (turn, highest[0])
            turn_to_state[turn] = state
    start_rep, left_y = state_to_turn[rep_state]
    period = rep_turn - start_rep

    reps, mod = divmod(turns - start_rep, period)
    turns_state = turn_to_state[mod + start_rep]
    _, state_y = state_to_turn[turns_state]
    height_growth = state_y - left_y + height_diff
    sys.stderr.write(f"Period: {period}; {start_rep} -> {mod + start_rep} : {left_y} -> {state_y}\n")
    final_y = max(turns_state[2]) + state_y + height_diff * reps
    sys.stderr.write(f"Num of states: {len(states)}\n")
    sys.stderr.write(f"{reps} {mod} {height_diff} {height_growth} {turns_state}; Ans: {final_y}\n")
    return filled_coordinates, final_y, idx


def solve():
    pattern = read_line()
    # filled, y = simulate(1, pattern, 2)
    # grid = [list('.' * 7) for _ in range(20)]
    # for x, y in filled:
    #     grid[20 - y][x] = '#'
    # draw = '\n'.join([''.join(row) for row in grid])
    # sys.stderr.write(f"{draw}\n")
    print(f"Part 1: {simulate(2022, pattern, 1)[1]}")
    print(f"Part 2: {simulate(1000000000000, pattern, 1)[1]}")

    # highest = []
    # count_with_turns = []
    # max_count_turns = -1
    # for turns in range(1000):
    #     filled, y, idx = simulate(turns, pattern, 1)
    #     count = len([x for x, ny in filled if ny == y])
    #     if count == 7:
    #         max_count_turns = turns
    #         break
    #     if turns % 100 == 0:
    #         sys.stderr.write(f"{turns}: {max_count_turns} -> {y} idx = {idx}\n")
    #         # after 566 turns/rocks, the max row is filled
    #         # filled again after 565 turns
    #
    #     highest.append(y)
    # sys.stderr.write(f"{max_count_turns}\n")

    # turns = 566 + 565
    # for t in range(turns - 6, turns + 6):
    #     filled, y = simulate(t, pattern, 1)
    #     count = len([x for x, ny in filled if ny == y])
    #     sys.stderr.write(f"{t} {count}\n")


if __name__ == '__main__':
    solve()
