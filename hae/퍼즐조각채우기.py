from itertools import permutations
from collections import deque


def get_cell_groups(
    board: list[list[int]], group_flag: int
) -> list[list[int]]:
    dr_dc = [(dr, 0) for dr in (-1, 1)] + [(0, dc) for dc in (-1, 1)]
    cell_groups = []

    len_board = len(board)
    for row in range(len_board):
        for col in range(len_board):
            if board[row][col] == group_flag:
                cell_to_visit = deque([(row, col)])
                board[row][col] = 1 - group_flag  # group flag: 0 or 1
                adjacent_cells = [(row, col)]

                while cell_to_visit:
                    current_r, current_c = cell_to_visit.popleft()
                    for dr, dc in dr_dc:
                        next_r, next_c = current_r + dr, current_c + dc
                        if next_r not in range(len_board) or next_c not in range(len_board):
                            continue
                        if board[next_r][next_c] == 1 - group_flag:
                            continue

                        adjacent_cells.append((next_r, next_c))
                        cell_to_visit.append((next_r, next_c))
                        board[next_r][next_c] = 1 - group_flag

                cell_groups.append(sorted(adjacent_cells))
    return cell_groups


def match(puzzle_cells: list, empty_cells: list) -> int:
    puzzle_delta = (
        puzzle_cells[0][0] -
        empty_cells[0][0], puzzle_cells[0][1] - empty_cells[0][1]
    )

    for puzzle_cell, empty_cell in zip(puzzle_cells, empty_cells):
        if empty_cell != (
            puzzle_cell[0] - puzzle_delta[0], puzzle_cell[1] - puzzle_delta[1]
        ):
            return 0
    return len(puzzle_cells)


def solution(game_board: list[list[int]], table: list[list[int]]) -> int:
    INF = 10 ** 9

    board_empty_group = get_cell_groups(game_board, 0)
    table_puzzle_group = get_cell_groups(table, 1)

    for puzzle_idx, puzzle in enumerate(table_puzzle_group):
        puzzle_min_row = INF
        puzzle_min_col = INF
        max_delta = 0
        for row, col in puzzle:
            puzzle_min_row = min(puzzle_min_row, row)
            puzzle_min_col = min(puzzle_min_col, col)

        current_puzzle = []
        max_delta = 0
        for row, col in puzzle:
            current_puzzle.append((row - puzzle_min_row, col - puzzle_min_col))
            max_delta = max(max_delta, row - puzzle_min_row,
                            col - puzzle_min_col)

        # Rotate Puzzle
        puzzle_rotations = [current_puzzle]
        for _ in range(0, 3):
            current_puzzle = sorted([(col, max_delta - row)
                                    for row, col in current_puzzle])
            puzzle_rotations.append(current_puzzle)

        table_puzzle_group[puzzle_idx] = puzzle_rotations

    empty_filled = [False] * len(board_empty_group)
    puzzle_used = [False] * len(table_puzzle_group)
    fulfilled_cell = 0
    for empty_idx, empty_cells in enumerate(board_empty_group):
        len_empty_cells = len(empty_cells)
        for puzzle_idx, puzzle_rotations in enumerate(table_puzzle_group):
            if puzzle_used[puzzle_idx] or empty_filled[empty_idx]:
                continue

            for puzzle in puzzle_rotations:
                len_puzzle = len(puzzle)
                if len_empty_cells != len_puzzle:
                    continue

                matched_cells = match(puzzle, empty_cells)
                if not matched_cells:
                    continue

                puzzle_used[puzzle_idx] = True
                empty_filled[empty_idx] = True
                fulfilled_cell += matched_cells
                break

    return fulfilled_cell
