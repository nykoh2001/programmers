import heapq as hq

def solution(
    n: int, m: int, start_r: int, start_c: int, end_r: int, end_c: int, dist: int
) -> str:
    delta_r, delta_c = end_r - start_r, end_c - start_c
    additional_dist = dist - (abs(delta_r) + abs(delta_c))
    if additional_dist < 0 or additional_dist % 2 == 1:
        return "impossible"
    
    moves = [("d", 1, 0), ("l", 0, -1), ("r", 0, 1), ("u", -1, 0)]
    
    cell_to_visit = [("", start_r, start_c)]
    while cell_to_visit:
        path_str, row, col = hq.heappop(cell_to_visit)
        
        for move_idx, move in enumerate(moves):
            path_char, d_r, d_c = move
            new_path_str = path_str + path_char
            
            new_row, new_col = row + d_r, col + d_c
            if new_row not in range(1, n + 1) or new_col not in range(1, m + 1):
                continue
                
            manhatton = abs(end_r - new_row) + abs(end_c - new_col)
            if manhatton > dist - len(new_path_str):
                continue
                
            if len(new_path_str) == dist:
                if new_row == end_r and new_col == end_c:
                    return new_path_str
                continue
            
            hq.heappush(cell_to_visit, (new_path_str, new_row, new_col))
            
            
            
            