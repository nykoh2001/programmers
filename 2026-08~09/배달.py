import heapq as hq
from collections import defaultdict

# 3:18 ~ 3:35


def solution(N, road, K):
    INF = float('inf')
    distances = [INF] * (N + 1)
    distances[1] = 0

    graph = defaultdict(list)
    for v1, v2, dist in road:
        graph[v1].append((dist, v2))
        graph[v2].append((dist, v1))

    nodes_to_visit = [(0, 1)]
    while nodes_to_visit:
        dist, node = hq.heappop(nodes_to_visit)
        if dist > distances[node]:
            continue

        for edge_cost, next_node in graph[node]:
            new_dist = dist + edge_cost
            if distances[next_node] <= new_dist:
                continue

            distances[next_node] = new_dist
            hq.heappush(nodes_to_visit, (new_dist, next_node))

    return sum([1 for d in distances[1:] if d <= K])
