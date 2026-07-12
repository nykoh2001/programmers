"""https://school.programmers.co.kr/learn/courses/30/lessons/118669

- 출발점 == 도착점
- 산 봉우리는 하나만, 한 번 포함
- 출발점 외 다른 게이트 방문 불가
- 최소 intensity를 갖는 산봉우리 중 가장 작은 숫자 값

- intensity에 대한 daijkstra
- 조건:
  출발점 == 도착점, 출발점 외 다른 게이트 방문 X
  산봉우리는 하나만
- 각 출발점 & 산봉우리 조합에 대한 daijkstra
  => 최대 n^2번 다익스트라

1. Infinite Loop
=> Add = to next value comparison, while keeping the current comparison as it is
~2. Intensity dict does not include summit key - it ends at first-adjacent node level~
- Due to the wrong correction
3. Timeout
=> Use Multi-source Daijkstra, initialize with multiple start points
    -> Still timeout for the last test case
    => `in summits`, `in gates` -> replace lists with sets ( O(N) -> O(1) )
"""

from collections import defaultdict
import heapq as hq


def solution(n, paths, gates: list, summits):
    INF = float('inf')
    graph = defaultdict(list)
    gate_set = set(gates)
    summit_set = set(summits)

    for path in paths:
        i, j, w = path
        graph[i].append([j, w])
        graph[j].append([i, w])

    nodes_to_visit = [[0, gate] for gate in gates]
    intensity = {gate: 0 for gate in gates}

    while nodes_to_visit:
        current_intensity, current_node = hq.heappop(nodes_to_visit)

        # !! Summit should be the end point, not going further !!
        if current_node in summit_set:
            continue

        # 1. Skip when new one is greater than existing one
        if current_intensity > intensity[current_node]:
            continue

        for adjacent_node in graph[current_node]:
            next_node, edge_distance = adjacent_node

            if next_node in gate_set:
                continue

            next_intensity = max(current_intensity, edge_distance)
            # 1. Does not push when the new calc is equal or less effective
            if next_intensity >= intensity.get(next_node, INF):
                continue

            intensity[next_node] = next_intensity
            hq.heappush(nodes_to_visit, [next_intensity, next_node])

    min_summit = INF
    min_intensity = INF
    for summit in summits:
        current_intensity = intensity.get(summit, INF)
        if min_intensity < current_intensity:
            continue

        if min_intensity > current_intensity:
            min_intensity = current_intensity
            min_summit = summit
            continue

        if summit < min_summit:
            min_summit = summit

    return [min_summit, min_intensity]


if __name__ == "__main__":
    result = solution(7, [[1, 4, 4], [1, 6, 1], [1, 7, 3], [
                      2, 5, 2], [3, 7, 4], [5, 6, 6]], [1], [2, 3, 4])
    print(result)
