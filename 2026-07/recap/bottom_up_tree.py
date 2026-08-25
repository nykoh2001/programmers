"""엣지가 하나인 Leaf 노드부터 처리 -> Bottom-up Tree traverse"""

from collections import defaultdict, deque


def solution(weights: list[int], edges: list[list[int]]) -> int:
    if sum(weights) != 0:
        return -1

    graph = defaultdict(set)
    for node1, node2 in edges:
        graph[node1].add(node2)
        graph[node2].add(node1)

    visited = [False] * len(weights)
    visited[0] = True

    visit_ordering = [0]
    nodes_to_visit = deque([0])
    while nodes_to_visit:
        current_node = nodes_to_visit.popleft()

        for next_node in graph[current_node]:
            if visited[next_node]:
                continue

            visited[next_node] = True
            nodes_to_visit.append(next_node)
            visit_ordering.append(next_node)

    edge_selected_count = 0
    reversed_ordering = reversed(visit_ordering[1:])
    for node in reversed_ordering:
        node_weight = weights[node]

        edge_selected_count += abs(node_weight)
        weights[node] -= node_weight
        current_edges = graph[node]

        if len(current_edges) > 1 or not current_edges:
            raise Exception(
                f"0개 또는 2개 이상의 엣지가 존재합니다. - node={node}, current_edges={current_edges}"
            )

        another_node = list(current_edges)[0]
        weights[another_node] += node_weight

        graph[node].remove(another_node)
        graph[another_node].remove(node)

    return edge_selected_count
