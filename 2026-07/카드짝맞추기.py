"""Permutation + BFS"""

from collections import defaultdict, deque
from itertools import permutations, product


def solution(board: list[list[int]], r: int, c: int) -> int:
    # 카드 위치 정보 정의
    card_deck = defaultdict(list)
    for row in range(0, 4):
        for col in range(0, 4):
            card_num = board[row][col]
            if card_num == 0:
                continue
            card_deck[card_num].append((row, col))

    # 카드를 방문할 경로들 정의
    card_set_ordering = permutations(card_deck, len(card_deck))
    card_pair_ordering = list(product([0, 1], repeat=len(card_deck)))

    card_visit_ordering = []
    for set_ordering in card_set_ordering:
        for pair_ordering in card_pair_ordering:
            ordering = []
            for s, p in zip(set_ordering, pair_ordering):
                ordering.append(card_deck[s][p])
                ordering.append(card_deck[s][abs(p - 1)])
            card_visit_ordering.append(ordering)

    # BFS 탐색 시 필요한 인접한 셀들 구하는 함수
    def get_adjacent_cells(r: int, c: int, board: list[list[int]]):
        adjacent_cells = []
        for move in (-1, 1):
            if r + move in range(0, 4):
                adjacent_cells.append([r + move, c])
            if c + move in range(0, 4):
                adjacent_cells.append([r, c + move])

        for next_r in range(r + 1, 4):
            if board[next_r][c] > 0 or next_r == 3:
                adjacent_cells.append([next_r, c])
                break
        for next_r in range(r - 1, -1, -1):
            if board[next_r][c] > 0 or next_r == 0:
                adjacent_cells.append([next_r, c])
                break

        for next_c in range(c + 1, 4):
            if board[r][next_c] > 0 or next_c == 3:
                adjacent_cells.append([r, next_c])
                break
        for next_c in range(c - 1, -1, -1):
            if board[r][next_c] > 0 or next_c == 0:
                adjacent_cells.append([r, next_c])
                break

        return adjacent_cells

    # 현재 위치 기준으로 다음 탐색할 카드까지의 최단거리 구하기
    INF = 10**9
    min_distance = INF
    for visit_ordering in card_visit_ordering:
        current_board = [row[:] for row in board]
        current_r, current_c = r, c
        distance_for_current_path = 0

        for current_target in visit_ordering:
            distances = [[INF] * 4 for _ in range(4)]
            distances[current_r][current_c] = 0
            cell_to_visit = deque([(current_r, current_c)])

            while cell_to_visit:
                current_cell = cell_to_visit.popleft()
                if distances[current_target[0]][current_target[1]] != INF:
                    distance_for_current_path += distances[current_target[0]
                                                           ][current_target[1]]
                    current_r, current_c = current_target
                    current_board[current_r][current_c] = 0
                    break

                adjacent_cells = get_adjacent_cells(
                    current_cell[0],
                    current_cell[1],
                    current_board
                )
                for next_r, next_c in adjacent_cells:
                    if distances[next_r][next_c] != INF:
                        continue

                    distances[next_r][next_c] = distances[current_cell[0]
                                                          ][current_cell[1]] + 1
                    cell_to_visit.append((next_r, next_c))

        min_distance = min(min_distance, distance_for_current_path)

    return min_distance + len(card_deck) * 2
