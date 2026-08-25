"""https://school.programmers.co.kr/learn/courses/30/lessons/49189"""

from collections import deque, defaultdict

def solution(num_node: int, edges: list[list[int]]):
    INF = float('inf')
    nodes_to_visit = deque([1])
    graph = defaultdict(list)
    distances = [INF] * (num_node + 1)
    distances[1] = 0
    
    max_distance = 0
    nodes_with_max_distance = set()
    
    for node1, node2 in edges:
        graph[node1].append(node2)
        graph[node2].append(node1)
        
    while nodes_to_visit:
        current_node = nodes_to_visit.popleft()
        adjacent_nodes = graph[current_node]
        
        current_node_distance = distances[current_node]
        
        if current_node_distance == max_distance:
            nodes_with_max_distance.add(current_node)
        elif current_node_distance > max_distance:
            max_distance = current_node_distance
            nodes_with_max_distance = set([current_node])
        
        for an in adjacent_nodes:
            if distances[an] <= current_node_distance + 1:
                continue
            
            distances[an] = current_node_distance + 1
            nodes_to_visit.append(an)
        
            
    return len(nodes_with_max_distance) 
        
    