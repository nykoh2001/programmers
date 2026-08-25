# https://school.programmers.co.kr/learn/courses/30/lessons/42861
# 4:27 ~ 4:38

import heapq as hq

def solution(n, costs):
    parents = [island for island in range(n)]
    
    def _find(island: int) -> int:
        if parents[island] == island:
            return island
    
        return _find(parents[island])

    def _union(island1: int, island2: int) -> bool:
        root1, root2 = _find(island1), _find(island2)
        if root1 == root2:
            return False
        
        parents[root2] = root1
        return True
    
    costs_heap = []
    for island1, island2, cost in costs:
        hq.heappush(costs_heap, (cost, island1, island2))
    
    total_cost = 0
    while costs_heap:
        cost, island1, island2 = hq.heappop(costs_heap)
        is_unioned = _union(island1, island2)
        if not is_unioned:
            continue
        
        total_cost += cost
    
    return total_cost
        
    