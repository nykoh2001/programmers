import heapq as hq


def solution(
    n: int, m: int, start_r: int, start_c: int, end_r: int, end_c: int, dist: int
) -> str:

    manhatton = abs(end_r - start_r) + abs(end_c - start_c)
    if manhatton > dist or (dist - manhatton) % 2 == 1:
        return "impossible"

    moves = [
        ("d", 1, 0),
        ("l", 0, -1),
        ("r", 0, 1),
        ("u", -1, 0)
    ]

    path_str = ""
    row, col = start_r, start_c
    for step in range(1, dist + 1):
        for move, dr, dc in moves:
            new_r, new_c = row + dr, col + dc
            if new_r not in range(1, n + 1) or new_c not in range(1, m + 1):
                continue

            if abs(end_r - new_r) + abs(end_c - new_c) > dist - step:
                continue

            path_str += move
            row += dr
            col += dc
            break

    return path_str
