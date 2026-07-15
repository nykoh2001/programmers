"""https://school.programmers.co.kr/learn/courses/30/lessons/72415

- BFS but with dynamic condition
"""

from collections import deque


def solution(board, r, c):
    cell_to_visit = deque([(r, c, 0, board[r][c])])
    remaining_pairs = set()
    visited = set()
    for row in board:
        remaining_pairs.update(row)

    while cell_to_visit:
        row, col, dist, card = cell_to_visit.popleft()
        print(f"row: {row}, col: {col}, dist: {dist}, card: {card}")

        if board[row][col] and board[row][col] == card:
            if card in remaining_pairs:
                remaining_pairs.remove(card)
                card = 0

            if not remaining_pairs:
                return dist

        if card == 0 and board[row][col] > 0:
            current_card = board[row][col]
        else:
            current_card = card

        for move in (-1, 1):
            row_move_count, col_move_count = 0, 0

            # Move in the same row
            new_col = col + move
            col_move_count += 1
            # print(f"col: {col}, new_col: {new_col}")
            while new_col >= 0 and new_col <= 3:
                if col_move_count == 1:
                    if (row, new_col) not in visited:
                        cell_to_visit.append(
                            (row, new_col, dist + 1, current_card))
                        visited.add((row, new_col))

                elif board[row][new_col] > 0 or new_col in [0, 3]:
                    if (row, new_col) not in visited:
                        cell_to_visit.append(
                            (row, new_col, dist + 1, current_card))
                        visited.add((row, new_col))
                    break

                new_col += move
                col_move_count += 1
                # print(f"col: {col}, new_col: {new_col}")

            # Move in the same column
            new_row = row + move
            row_move_count += 1
            # print(f"row: {row}, new_row: {new_row}")
            while new_row >= 0 and new_row <= 3:
                if row_move_count == 1:
                    if (new_row, col) not in visited:
                        cell_to_visit.append(
                            (new_row, col, dist + 1, current_card))
                        visited.add((new_row, col))

                elif board[new_row][col] > 0 or new_row in [0, 3]:
                    if (new_row, col) not in visited:
                        cell_to_visit.append(
                            (new_row, col, dist + 1, current_card))
                        visited.add((new_row, col))
                    break

                new_row += move
                row_move_count += 1
                # print(f"row: {row}, new_row: {new_row}")
