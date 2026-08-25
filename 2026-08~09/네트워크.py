# https://school.programmers.co.kr/learn/courses/30/lessons/43162?language=python3
# 3:46 ~ 3:55

from collections import defaultdict, deque

def solution(n: int, computers: list[list[int]]) -> int:
    visited_list = [False] * n
    graph = defaultdict(list)
    
    network_count = 0
    for computer, visited in enumerate(visited_list):
        if visited:
            continue
        
        computer_to_visit = deque([computer])
        visited_list[computer] = True

        while computer_to_visit:
            curr_computer = computer_to_visit.popleft()
            for adjacent_computer, connected in enumerate(computers[curr_computer]):
                if not connected or visited_list[adjacent_computer]:
                    continue
                
                visited_list[adjacent_computer] = True
                computer_to_visit.append(adjacent_computer)
        
        
        network_count += 1
    
    return network_count