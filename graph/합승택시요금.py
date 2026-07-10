"""https://school.programmers.co.kr/learn/courses/30/lessons/72413?language=python3

- 경로에 가중치가 있는 그래프
- 시작점에서 A, B가 있는 위치를 모두 거친 경로만 고려: X
    => 임의의 지점 X에서 a, b, s까지 가는 비용 합산
- Daijkstra using prioritized queue
- Result = min(s -> a + s -> b, s -> a -> b, s -> b -> a)

** Caution:
edge case - A와 B 가 N까지 합승 -> 이후 따로 택시 승차
"""

import heapq as hq
from collections import defaultdict

INF = 999_999_999


def get_cheapest_path(s: int, graph: dict[list]) -> dict:
    nodes_to_visit = [[0, s]]
    distances = {s: 0}

    while nodes_to_visit:
        _, current_node = hq.heappop(nodes_to_visit)

        adjacent_nodes = graph.get(current_node)
        if not adjacent_nodes:
            continue

        for next_node, distance in adjacent_nodes:
            new_distance = distance + distances.get(current_node)

            if distances.get(next_node, INF) <= new_distance:
                continue

            distances[next_node] = new_distance
            hq.heappush(nodes_to_visit, [distances[next_node], next_node])

    return distances


def solution(n, s, a, b, fares):
    graph = defaultdict(list)

    # Initialize Graph
    for f in fares:
        node1, node2, fare = f

        graph[node1].append([node2, fare])
        graph[node2].append([node1, fare])

    distances_from_start = get_cheapest_path(s, graph)
    distances_from_a = get_cheapest_path(a, graph)
    distances_from_b = get_cheapest_path(b, graph)

    cheapest_fare = INF

    for split_node in range(1, n+1):
        new_fare = (distances_from_start.get(split_node, INF)
                    + distances_from_a.get(split_node, INF)
                    + distances_from_b.get(split_node, INF))

        cheapest_fare = min(cheapest_fare, new_fare)

    return cheapest_fare


if __name__ == "__main__":
    result = solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [
                      5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]])
    print(result)
