# https://school.programmers.co.kr/learn/courses/30/lessons/118669
# 2:14 ~ 2:38 (24/25, timeout)
# ~ 2:45 - pause

from collections import defaultdict
import heapq as hq


def solution(n: int, paths: list[list[int]], gates: list[int], summits: list[int]) -> list[int]:
    INF = 10**9

    graph = defaultdict(list)
    gate_set = set(gates)
    summit_set = set(summits)

    for node1, node2, intensity in paths:
        if node2 not in gate_set:
            graph[node1].append((intensity, node2))
        if node1 not in gate_set:
            graph[node2].append((intensity, node1))

    intensities = [INF] * (n + 1)
    nodes_to_visit = [(0, gate) for gate in gates]

    min_intensities = []
    while nodes_to_visit:
        curr_intensity, curr_node = hq.heappop(nodes_to_visit)
        if intensities[curr_node] < curr_intensity:
            continue

        if curr_node in summit_set:
            hq.heappush(min_intensities, (curr_intensity, curr_node))
            continue

        for next_intensity, next_node in graph[curr_node]:
            new_intensity = max(curr_intensity, next_intensity)
            if new_intensity >= intensities[next_node]:
                continue
            hq.heappush(nodes_to_visit, (new_intensity, next_node))
            intensities[next_node] = new_intensity

    min_intensity = hq.heappop(min_intensities)
    return [min_intensity[1], min_intensity[0]]
