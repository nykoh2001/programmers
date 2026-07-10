"""https://school.programmers.co.kr/learn/courses/30/lessons/72413?language=python3

- 경로에 가중치가 있는 그래프
- 시작점에서 A, B가 있는 위치를 모두 거친 경로만 고려: X
    => 임의의 지점 X에서 a, b, s까지 가는 비용 합산
- Daijkstra using prioritized queue

===
Daijstra: BFS with weighted edges
1. Initialize graph, distance dictionary
2. Iterate every nodes, update adjacent nodes' distances
    - Only when the new distance is less than existing distance
    - The next node should be the next closest from the start node
3. Distance dictionary stores shortest distances from the start node

** Caution:
edge case - A와 B 가 N까지 합승 -> 이후 따로 택시 승차
"""

import heapq as hq
from collections import defaultdict

INF = 999_999_999


def get_cheapest_path(s: int, graph: dict[list]) -> dict:
    """Complexity Estimation

    Time complexity:
        1. heap push & pop up to E times: O(E log E)
        2. 인접 리스트 순회: 모든 인접 리스트 순회 횟수 <= 2E, O(E)
        => Total Time complexity: O(E log E) + O(E) = O(E log E)
        ==> 엣지의 수는 최대 V(V-1) 이므로, O(E log V)로 나타내기도 함.
    
    Space Complexity:
        1. graph: 정점과 엣지 저장, O(V + E)
        2. distance: 정점들에 대한 최소 거리만 저장, O(V)
        3. nodes_to_visit: 최대 E개까지 저장, O(E)
        4. get_cheapest_path: nodes_to_visit + distances, O(V + E)
    """
    nodes_to_visit = [[0, s]]
    distances = {s: 0}

    while nodes_to_visit:
        # Time: O(log E), Space: O(1)
        current_distance, current_node = hq.heappop(nodes_to_visit)

        adjacent_nodes = graph.get(current_node)
        # When the current node is an island
        # Or current node visit is less effective than previous visit
        if not adjacent_nodes or current_distance > distances[current_node]:
            continue

        for next_node, distance in adjacent_nodes:
            new_distance = distance + distances.get(current_node)

            if distances.get(next_node, INF) <= new_distance:
                continue

            distances[next_node] = new_distance

            hq.heappush(nodes_to_visit, [distances[next_node], next_node])

    return distances


def solution(n, s, a, b, fares):
    """Complexity Estimation
    
    Time: O(E log E) or O(E log V)
    Space: O(V + E)
    """
    graph = defaultdict(list)

    # Initialize Graph
    # Time: O(E), Space: O(V + E)
    for f in fares:
        node1, node2, fare = f

        graph[node1].append([node2, fare])
        graph[node2].append([node1, fare])

    # Time: 3 O(E log E), O(E log E) - or O(E log V)
    # Space: O(V) + O(E)
    distances_from_start = get_cheapest_path(s, graph)
    distances_from_a = get_cheapest_path(a, graph)
    distances_from_b = get_cheapest_path(b, graph)

    cheapest_fare = INF

    # Time: O(V)
    # Space: O(1)
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
