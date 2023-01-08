from collections import defaultdict, deque
from typing import List
import sys

sys.stdin = open("day18.in", "r")
sys.stdout = open("day18.out", "w")

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


def get_neighbors(cube):
    x, y, z = cube
    neighbors = []
    d = [-1, 1]
    for dz in d:
        neighbors.append((x, y, z + dz))

    for dx in d:
        neighbors.append((x + dx, y, z))

    for dy in d:
        neighbors.append((x, y + dy, z))

    return neighbors


def get_air_neighbors(cube, cubes):
    neighs = get_neighbors(cube)
    air = []
    for neigh in neighs:
        if neigh not in cubes:
            air.append(neigh)
    return air


def is_neighbor_free(neighbor, cube_neighbors, all_neighbors):
    d = [(1, 0, 0), (-1, 0, 0)]
    vals = [set(), set(), set()]
    for x, y, z in neighbor:
        vals[0].add(x)
        vals[1].add(y)
        vals[2].add(z)
    if len(vals[1]) == 1:
        d = [(0, 1, 0), (0, -1, 0)]
    elif len(vals[2]) == 1:
        d = [(0, 0, 1), (0, 0, -1)]
    # sys.stderr.write(f"{d}\n")
    for dx, dy, dz in d:
        for rep in range(1, 100):
            new_neighbor = []
            for x, y, z in neighbor:
                new_neighbor.append((x + rep * dx, y + rep * dy, z + rep * dz))
            new_neighbor = tuple(new_neighbor)
            # if rep <= 10:
            #     sys.stderr.write(f"{new_neighbor}\n")
            if new_neighbor in cube_neighbors:
                break
            if new_neighbor in all_neighbors:
                sys.stderr.write(f"{neighbor} -> {new_neighbor}\n")
                return False
    return True


def goes_outside(neighbor, cubes, limit):
    q = deque()
    q.append(neighbor)
    seen = set()
    seen.add(neighbor)
    while q:
        neighbor = q.popleft()
        neighs = get_air_neighbors(neighbor, cubes)
        # sys.stderr.write(f"{len(neighs)}\n")
        if max(neighbor) >= limit:
            return True
        for neigh in neighs:
            if neigh not in seen:
                q.append(neigh)
                seen.add(neigh)
    return False


def solve():
    # neighbors = get_neighbors(0, 0, 0)
    # neighbors_str = '\n'.join(map(str, neighbors))
    # sys.stderr.write(f"{neighbors_str}\n")
    line = read_line()
    cubes = []
    max_coord = 0
    while line:
        x, y, z = map(int, line.split(','))
        max_coord = max(max_coord, max((x, y, z)))
        cubes.append((x, y, z))
        line = read_line()

    cubes = set(cubes)
    free_faces = []
    for cube in cubes:
        neighbors = get_neighbors(cube)
        for neigh in neighbors:
            if neigh not in cubes:
                free_faces.append(neigh)
    # sys.stderr.write(f"Length of cube neighbors: {len(cubes[0])} {cubes[0][0]} "
    #                  f"{is_neighbor_free(cubes[0][0], set(cubes[0]), neighbor_count.keys())}\n")

    print(f"Part 1: {len(free_faces)}")

    outside = 0
    sys.stderr.write(f"Max coord: {max_coord}\n")
    for neigh in free_faces:
        outside += goes_outside(neigh, cubes, max_coord + 2)

    print(f"Part 2: {outside}")
    #
    # adj = defaultdict(list)
    #
    # def is_line(points):
    #     p1, p2 = points
    #     zeros = 0
    #     for k in range(len(p1)):
    #         if p1[k] - p2[k] > 1:
    #             return False
    #         zeros += (1 if p1[k] - p2[k] == 0 else 0)
    #     return zeros == 2
    #
    # for i in range(len(exposed_neighbors)):
    #     u = exposed_neighbors[i]
    #     for j in range(i + 1, len(exposed_neighbors)):
    #         v = exposed_neighbors[j]
    #         u_x, u_y, u_z = u
    #         v_x, v_y, v_z = v
    #         dx, dy, dz = abs(u_x - v_x), abs(u_y - v_y), abs(u_z - v_z)
    #         diff = abs(u_x - v_x) + abs(u_y - v_y) + abs(u_z - v_z)
    #         diffs = [dx, dy, dz]
    #         if diff == 1 and (sum([d == 1 for d in diffs]) == 1 or sum([d == 0.5 for d in diffs]) == 2):
    #             adj[u].append(v)
    #             adj[v].append(u)
    # pr = '\n'.join(map(str, adj[exposed_neighbors[0]]))
    # sys.stderr.write(f"{exposed_neighbors[0]} -> \n{pr}\n")
    # sys.stderr.write(f"{[len(c) for c in adj.values()]}")
    # q = deque()
    # q.append(exposed_neighbors[0])
    # seen = set()
    # seen.add(exposed_neighbors[0])
    # while q:
    #     neighbor = q.popleft()
    #     for nxt in adj[neighbor]:
    #         if nxt not in seen:
    #             q.append(nxt)
    #             seen.add(nxt)
    #
    # print(f"Part 2: {len(seen)}")


if __name__ == '__main__':
    solve()
