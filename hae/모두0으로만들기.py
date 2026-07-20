"""https://school.programmers.co.kr/learn/courses/30/lessons/76503"""

from collections import defaultdict, deque


def solution(node_weights: list[int], edges: list[int, int]) -> int:
    edges_per_node = defaultdict(set)
    for edge_idx, edge in enumerate(edges):
        node1, node2 = edge
        edges_per_node[node1].add(edge_idx)
        edges_per_node[node2].add(edge_idx)

    nodes_with_single_edge = deque()

    for node, edge_idx_set in edges_per_node.items():
        if len(edge_idx_set) == 1:
            nodes_with_single_edge.append(node)

    total_count = 0
    edge_used = [False] * len(edges)

    while nodes_with_single_edge:
        node = nodes_with_single_edge.popleft()
        edge_idx_set = edges_per_node[node]
        node_weight = node_weights[node]

        edge_idx_list = list(edge_idx_set)
        if not edge_idx_list:
            continue

        edge_idx = edge_idx_list[0]
        for n in edges[edge_idx]:
            if n == node:
                node_weights[n] -= node_weight
            else:
                node_weights[n] += node_weight

            edge_count = len(edges_per_node[n])
            edges_per_node[n].remove(edge_idx)
            if len(edges_per_node[n]) == 1:
                nodes_with_single_edge.append(n)

        total_count += abs(node_weight)
        edge_used[edge_idx] = True

    if sum(node_weights) != 0:
        return -1

    return total_count
