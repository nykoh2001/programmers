"""Daijkstra

5개 테스트케이스에 대해 시간초과
- 무한루프: X
- 시간 최적화:
    - 모든 노드에 대해 다익스트라를 할 필요 없음
    - s, a, b에 대해서만 하면 됨
"""

import heapq as hq
from collections import defaultdict


def solution(n: int, s: int, a: int, b: int, fares: list[list[int]]) -> int:
    INF = 10**9
    fare_graph = defaultdict(list)

    for node1, node2, fare in fares:
        fare_graph[node1].append((fare, node2))
        fare_graph[node2].append((fare, node1))

    def get_cheapest_fares(node: int):
        fares = defaultdict(int)
        nodes_to_visit = [(0, node)]

        while nodes_to_visit:
            fare, current_node = hq.heappop(nodes_to_visit)
            if fare >= fares.get(current_node, INF):
                continue

            fares[current_node] = fare
            for next_fare, next_node in fare_graph[current_node]:
                hq.heappush(nodes_to_visit, (next_fare + fare, next_node))

        return fares

    cheapest_fare = INF
    fares_from_start = get_cheapest_fares(s)
    fares_from_a = get_cheapest_fares(a)
    fares_from_b = get_cheapest_fares(b)

    for node in range(1, n + 1):
        start_to_node = fares_from_start.get(node, INF)
        node_to_a = fares_from_a.get(node, INF)
        node_to_b = fares_from_b.get(node, INF)

        cheapest_fare = min(cheapest_fare, start_to_node +
                            node_to_a + node_to_b)

    return cheapest_fare
