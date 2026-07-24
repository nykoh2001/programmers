import heapq as hq
from collections import deque

GRAPH = {
    1: [(1, 1), (2, 2), (4, 2), (5, 3)],
    2: [(2, 1), (1, 2), (3, 2), (5, 2), (4, 3), (6, 3)],
    3: [(3, 1), (2, 2), (6, 2), (5, 3)],
    4: [(4, 1), (1, 2), (5, 2), (7, 2), (2, 3), (8, 3)],
    5: [(5, 1), (2, 2), (4, 2), (6, 2), (8, 2), (1, 3), (3, 3), (7, 3), (9, 3)],
    6: [(6, 1), (3, 2), (5, 2), (9, 2), (2, 3), (8, 3)],
    7: [(7, 1), (4, 2), (8, 2), (0, 3), (5, 3)],
    8: [(8, 1), (0, 2), (5, 2), (7, 2), (9, 2), (4, 3), (6, 3)],
    9: [(9, 1), (6, 2), (8, 2), (0, 3), (5, 3)],
    0: [(0, 1), (7, 3), (8, 2), (9, 3)]
}

INF = 10 ** 9

def get_distances(number: int) -> list[int]:
    numbers_to_visit = [(0, number)]
    distances = [INF] * 10
    distances[number] = 0
    
    while numbers_to_visit:
        curr_dist, curr_number = hq.heappop(numbers_to_visit)
        if distances[curr_number] < curr_dist:
            continue

        for next_number, dist in GRAPH[curr_number]:
            new_dist = curr_dist + dist
            if distances[next_number] <= new_dist:
                continue

            distances[next_number] = new_dist
            hq.heappush(numbers_to_visit, (new_dist, next_number))
    
    distances[number] = 1
    return distances

def solution(numbers: str) -> int:
    min_distance = INF
    number_idx = -1
    fingers = [4, 6]
    distances_by_number = {number: get_distances(number) for number in range(10)}
    
    distance_dp = [[[INF] * 10 for _ in range(10)] for _ in range(len(numbers))]
    
    cells_to_visit = deque([(number_idx, fingers)])
    while cells_to_visit:
        curr_num_idx, curr_fingers = cells_to_visit.popleft()
        curr_number = int(numbers[curr_num_idx])
        
        # print(f"curr_num_idx: {curr_num_idx}, curr_fingers: {curr_fingers}")
        # print(distance_dp[curr_num_idx][curr_fingers[0]])
        # print(distance_dp[curr_num_idx][curr_fingers[0]][curr_fingers[1]])
        
        new_num_idx = curr_num_idx + 1
        if new_num_idx == len(numbers):
            continue
        
        new_number = int(numbers[new_num_idx])
        
        if new_number in curr_fingers:
            new_distance = (
                distance_dp[curr_num_idx][curr_fingers[0]][curr_fingers[1]]
                if curr_num_idx >= 0
                else 0
            ) + 1
            
            if distance_dp[new_num_idx][curr_fingers[0]][curr_fingers[1]] <= new_distance:
                continue
            
            distance_dp[new_num_idx][curr_fingers[0]][curr_fingers[1]] = new_distance
            cells_to_visit.append((new_num_idx, curr_fingers))
            continue
        
        for finger_idx, finger in enumerate(curr_fingers):
            new_distance = distances_by_number[finger][new_number] + (
                distance_dp[curr_num_idx][curr_fingers[0]][curr_fingers[1]]
                if curr_num_idx >= 0
                else 0
            )
            
            new_fingers = curr_fingers[:]
            new_fingers[finger_idx] = new_number
            new_fingers.sort()

            if distance_dp[new_num_idx][new_fingers[0]][new_fingers[1]] <= new_distance:
                continue
            
            distance_dp[new_num_idx][new_fingers[0]][new_fingers[1]] = new_distance
            cells_to_visit.append((new_num_idx, new_fingers))
    
    return min([cell for row in distance_dp[len(numbers) - 1] for cell in row])
            
            
            