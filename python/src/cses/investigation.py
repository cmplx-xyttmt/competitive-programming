from typing import List, Tuple
import heapq
MOD = int(1e9) + 7
if __name__ == '__main__':
    n, m = map(int, input().split())
    adj: List[List[Tuple[int, int]]] = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        adj[a].append((b, c))

    dists = [0 for _ in range(n + 1)]
    seen = [False for _ in range(n + 1)]
    total_routes = [0 for _ in range(n + 1)]
    total_routes[1] = 1
    min_flights = [m + 1 for _ in range(n + 1)]
    min_flights[1] = 0
    max_flights = [0 for _ in range(n + 1)]
    pq = []
    heapq.heappush(pq, (0, 1))  # dist, city
    edges = 0
    while pq:
        dist, city = heapq.heappop(pq)
        if seen[city]:
            continue
        seen[city] = True
        if city == n:
            break
        for next_city, length in adj[city]:
            edges += 1
            # print(next_city, length, dists[next_city])
            if not dists[next_city] or dist + length <= dists[next_city]:
                if dists[next_city] == 0 or dist + length < dists[next_city]:
                    total_routes[next_city] = total_routes[city]
                    min_flights[next_city] = 1 + min_flights[city]
                    max_flights[next_city] = max_flights[city] + 1
                else:
                    total_routes[next_city] = (total_routes[next_city] + total_routes[city]) % MOD
                    min_flights[next_city] = min(min_flights[next_city], min_flights[city] + 1)
                    max_flights[next_city] = max(max_flights[next_city], max_flights[city] + 1)
                heapq.heappush(pq, (dist + length, next_city))
                dists[next_city] = dist + length

    d, r, min_f, max_f = dists[n], total_routes[n], min_flights[n], max_flights[n]
    print(d, r, min_f, max_f)
