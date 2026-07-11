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
3. 
"""

from collections import defaultdict
import heapq as hq


def solution(n, paths, gates: list, summits):
    INF = float('inf')
    graph = defaultdict(list)
    intensity_q = []
    for path in paths:
        i, j, w = path
        graph[i].append([j, w])
        graph[j].append([i, w])

    for gate in gates:
        for summit in summits:
            nodes_to_visit = [[0, gate]]
            intensity = {gate: 0}

            while nodes_to_visit:
                current_intensity, current_node = hq.heappop(nodes_to_visit)

                # 1. Skip when new one is greater than existing one
                if current_intensity > intensity[current_node]:
                    continue

                for adjacent_node in graph[current_node]:
                    next_node, edge_distance = adjacent_node

                    if (
                            # It is gate / other summits
                            (
                                next_node in gates
                                or (next_node in summits and next_node != summit)
                            )
                            # Fix: Comment this out to consider lately updated minimum intensity
                            # Duplicate visits to summit should not matter while updating
                            # or already visited summit
                            # or (next_node == summit and next_node in intensity)
                    ):
                        continue

                    next_intensity = max(current_intensity, edge_distance)
                    # 1. Does not push when the new calc is equal or less effective
                    if next_intensity >= intensity.get(next_node, INF):
                        continue

                    intensity[next_node] = next_intensity
                    hq.heappush(nodes_to_visit, [next_intensity, next_node])

            summit_intensity = intensity.get(summit, INF)

            hq.heappush(intensity_q, [summit_intensity, summit])

    min_intensity, summit = hq.heappop(intensity_q)

    return [summit, min_intensity]


if __name__ == "__main__":
    result = solution(7, [[1, 4, 4], [1, 6, 1], [1, 7, 3], [
                      2, 5, 2], [3, 7, 4], [5, 6, 6]], [1], [2, 3, 4])
    print(result)
