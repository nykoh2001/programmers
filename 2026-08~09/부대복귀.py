from collections import deque, defaultdict

# 2:54 ~ 3:02
# destination -> sources로 BFS => distances 업데이트


def solution(n, roads, sources, destination):
    INF = float('inf')
    distances = [INF] * (n + 1)
    distances[destination] = 0

    graph = defaultdict(list)
    for node1, node2 in roads:
        graph[node1].append(node2)
        graph[node2].append(node1)

    nodes_to_visit = deque([destination])
    while nodes_to_visit:
        curr_node = nodes_to_visit.popleft()

        for next_node in graph[curr_node]:
            if distances[next_node] != INF:
                continue

            new_distance = distances[curr_node] + 1
            distances[next_node] = new_distance
            nodes_to_visit.append(next_node)

    return [distances[node] if distances[node] != INF else -1 for node in sources]
