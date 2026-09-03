# 3:05 ~ 3:17 (22.2/100) => pop이 아닌 popleft

from collections import deque, defaultdict


def solution(n: int, vertex: list[list[int]]):
    INF = float('inf')
    distances = [INF] * (n + 1)
    distances[1] = 0
    vertex_to_visit = deque([1])

    graph = defaultdict(list)
    for v1, v2 in vertex:
        graph[v1].append(v2)
        graph[v2].append(v1)

    max_distance = 0

    while vertex_to_visit:
        curr_vertex = vertex_to_visit.popleft()
        for next_vertex in graph[curr_vertex]:
            if distances[next_vertex] != INF:
                continue

            new_distance = distances[curr_vertex] + 1
            distances[next_vertex] = new_distance
            max_distance = max(max_distance, new_distance)
            vertex_to_visit.append(next_vertex)

    return distances.count(max_distance)
