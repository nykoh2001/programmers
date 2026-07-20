"""Multi-source Daijkstra

- return하는 값에 게이트 정보가 없음 - 최소 인텐시티와 최소 인텐시티를 갖는 목적지만 반환
- 어느 gate에서 시작되서 갱신된 인텐시티인지 기록할 필요 x
"""

import heapq as hq
from collections import defaultdict


def solution(n: int, paths: list[list[int]], gates: list[int], summits: list[int]) -> list[int]:
    nodes_to_visit = [(0, gate) for gate in gates]
    path_graph = defaultdict(list)
    min_intensity_from_gates = defaultdict(int)

    INF = 10 ** 9

    for node1, node2, intensity in paths:
        path_graph[node1].append((intensity, node2))
        path_graph[node2].append((intensity, node1))

    while nodes_to_visit:
        intensity, current_node = hq.heappop(nodes_to_visit)
        if intensity >= min_intensity_from_gates.get(current_node, INF):
            continue

        min_intensity_from_gates[current_node] = intensity
        if current_node in summits:
            continue

        for next_intensity, next_node in path_graph[current_node]:
            hq.heappush(nodes_to_visit,
                        (max(intensity, next_intensity), next_node))

    min_intensity, min_intensity_summit = 10**9, -1
    for summit in summits:
        if min_intensity_from_gates.get(summit, INF) < min_intensity:
            min_intensity = min_intensity_from_gates[summit]
            min_intensity_summit = summit
            continue

        if (
            min_intensity_from_gates.get(summit, INF) == min_intensity
            and summit < min_intensity_summit
        ):
            min_intensity_summit = summit
            continue

    return [min_intensity_summit, min_intensity]
