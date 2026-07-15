"""https://school.programmers.co.kr/learn/courses/30/lessons/72415

- 어떤 카드를 먼저 제거하느냐에 따라 최소 비용이 달라질 수 있음
    => 모든 카드 제거 순서에 대해 탐색
- 카드1 -> 카드2 최소 거리 계산 반복
"""

from itertools import permutations
from collections import deque

DR_DC = [[-1, 0], [1, 0], [0, -1], [0, 1]]


def get_distance_to_target_card(board, start_row, start_col, target_card, skip=None):
    cell_to_visit = deque([[start_row, start_col]])
    visited = set((start_row, start_col))
    distance = [[0 for _ in range(4)] for _ in range(4)]

    def find_adjacent_cells(r, c) -> list:
        def is_in_boundary(r, c):
            if r >= 0 and r < 4 and c >= 0 and c < 4:
                return True
            return False

        adjacent_cells = set()
        for dr, dc in DR_DC:
            new_row = r + dr
            new_col = c + dc

            if is_in_boundary(new_row, new_col):
                adjacent_cells.add((new_row, new_col))

        new_row = r + 1
        while is_in_boundary(new_row, c):
            if board[new_row][c] > 0:
                adjacent_cells.add((new_row, c))
                break
            new_row += 1

        new_row = r - 1
        while is_in_boundary(new_row, c):
            if board[new_row][c] > 0:
                adjacent_cells.add((new_row, c))
                break
            new_row -= 1

        new_col = c + 1
        while is_in_boundary(r, new_col):
            if board[r][new_col] > 0:
                adjacent_cells.add((r, new_col))
                break
            new_col += 1

        new_col = c - 1
        while is_in_boundary(r, new_col):
            if board[r][new_col] > 0:
                adjacent_cells.add((r, new_col))
                break
            new_col -= 1

        return list(adjacent_cells)

    while cell_to_visit:
        row, col = cell_to_visit.popleft()

        adjacent_cells = find_adjacent_cells(row, col)
        for ac in adjacent_cells:
            if ac in visited:
                continue

            cell_to_visit.append(ac)
            visited.add(ac)
            new_distance = distance[row][col] + 1
            next_row, next_col = ac
            if board[next_row][next_col] == target_card and (next_row, next_col) != skip:
                return [next_row, next_col, new_distance]

            distance[next_row][next_col] = new_distance


def solution(board, r, c):
    min_distance = 10**9
    all_cards = set()

    for row in board:
        all_cards.update(row)
    all_cards.remove(0)

    card_ordering = list(permutations(list(all_cards)))

    for co in card_ordering:
        current_row, current_col = r, c
        current_board = [row[:] for row in board]
        distance = 0

        for target_card in co:
            # Empty cell to card -
            if current_board[current_row][current_col] != target_card:
                # Start with closest card 
                # ^ The case when start with farther one can be more effective way 
                new_row, new_col, distance_to_card = get_distance_to_target_card(
                    current_board, current_row, current_col, target_card)

                distance += distance_to_card
                current_row, current_col = new_row, new_col

            # Move from Card to Card
            card_row, card_col, distance_to_card = get_distance_to_target_card(
                current_board, current_row, current_col, target_card)

            distance += distance_to_card
            current_board[current_row][current_col] = 0
            current_board[card_row][card_col] = 0
            current_row, current_col = card_row, card_col
            continue

        min_distance = min(distance, min_distance)

    return min_distance
