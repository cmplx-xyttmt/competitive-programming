"""
Reference: Codeforces EDU: https://codeforces.com/edu/course/2/lesson/7
DSU is a data structure that supports disjoint sets on n elements and allows two types of queries:
- get(a): return the identifier of the set to which a belongs.
- union(a, b): join two sets that contain a and b
"""


# Use path compression to update the parents of nodes on the path to the root.
# This can also be done recursively.
def get_parent(node, parents):
    path = []
    while node != parents[node]:
        path.append(node)
        node = parents[node]

    new_parent = node
    for node in path:
        parents[node] = new_parent

    return new_parent


# combine first and second into the same set using rank heuristic.
def union(first, second, parents, rank):
    first, second = get_parent(first, parents), get_parent(second, parents)
    if first == second:
        return

    if rank[first] == rank[second]:
        rank[first] += 1

    if rank[first] > rank[second]:
        parents[second] = first
        rank[first] += 1
    else:
        parents[first] = second
        rank[second] += 1
