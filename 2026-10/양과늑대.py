# 1:04 ~ 1:42 - DFS, Find, topological sort
# ~ : 1:57 - DFS

from collections import defaultdict

def solution(info, edges):
    graph = defaultdict(list)
    
    for parent, child in edges:
        graph[parent].append(child)
    
    max_sheep_count = 0
    def _traverse(sheep_count: int, wolf_count: int, candidates: list[int]):
        nonlocal max_sheep_count
        for candidate in candidates:
            is_wolf = info[candidate]
            
            new_wolf_count, new_sheep_count = wolf_count, sheep_count
            if is_wolf:
                new_wolf_count += 1
            else:
                new_sheep_count += 1
            
            if new_wolf_count >= new_sheep_count:
                continue
            
            max_sheep_count = max(max_sheep_count, new_sheep_count)
            
            new_candidates = [_candidate for _candidate in candidates if _candidate != candidate]
            _traverse(new_sheep_count, new_wolf_count, new_candidates + graph[candidate])
        
        max_sheep_count = max(max_sheep_count, sheep_count)
        
    _traverse(0, 0, [0])
    return max_sheep_count