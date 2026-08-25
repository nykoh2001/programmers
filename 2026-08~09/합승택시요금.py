"""
https://school.programmers.co.kr/learn/courses/30/lessons/72413
k 지점까지 합승: (s -> k) + (k -> a) + (k -> b)
4:09 ~ 4:27
"""

from collections import defaultdict
import heapq as hq

INF = 10 ** 9


def solution(n, s, a, b, fares):
    graph = defaultdict(list)
    for node1, node2, cost in fares:
        graph[node1].append((cost, node2))
        graph[node2].append((cost, node1))

    def _get_distances_from_node(node: int) -> list[int]:
        distances = [INF] * (n + 1)
        distances[node] = 0
        nodes_to_visit = [(0, node)]

        while nodes_to_visit:
            curr_cost, curr_node = hq.heappop(nodes_to_visit)
            if distances[curr_node] < curr_cost:
                continue

            for next_cost, next_node in graph[curr_node]:
                new_distance = curr_cost + next_cost
                if distances[next_node] <= new_distance:
                    continue

                distances[next_node] = new_distance
                hq.heappush(nodes_to_visit, (new_distance, next_node))

        return distances

    distances_from_s = _get_distances_from_node(s)
    distances_from_a = _get_distances_from_node(a)
    distances_from_b = _get_distances_from_node(b)

    min_cost = INF
    for node in range(1, n + 1):
        min_cost = min(
            min_cost, distances_from_s[node] + distances_from_a[node] + distances_from_b[node])

    return min_cost
