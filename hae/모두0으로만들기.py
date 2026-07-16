"""https://school.programmers.co.kr/learn/courses/30/lessons/76503"""

from collections import defaultdict


def solution(node_weights: list[int], edges: list[int, int]) -> int:
    edges_per_node = defaultdict(set)
    for edge_idx, edge in enumerate(edges):
        node1, node2 = edge
        edges_per_node[node1].add(edge_idx)
        edges_per_node[node2].add(edge_idx)

    nodes_by_edge_count = defaultdict(set)
    for node, edge_idx_set in edges_per_node.items():
        nodes_by_edge_count[len(edge_idx_set)].add(node)

    total_count = 0
    edge_used = [False] * len(edges)

    while not all(edge_used):
        node = list(nodes_by_edge_count[1])[0]
        edge_idx_set = edges_per_node[node]
        node_weight = node_weights[node]

        edge_idx = list(edge_idx_set)[0]
        for n in edges[edge_idx]:
            if n == node:
                node_weights[n] -= node_weight
            else:
                node_weights[n] += node_weight

            edge_count = len(edges_per_node[n])
            edges_per_node[n].remove(edge_idx)
            nodes_by_edge_count[edge_count].remove(n)
            nodes_by_edge_count[edge_count - 1].add(n)

        total_count += abs(node_weight)
        edge_used[edge_idx] = True

    if sum(node_weights) != 0:
        return -1

    return total_count
