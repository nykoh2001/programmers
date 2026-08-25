from collections import deque


def solution(board: list[list[int]]):
    len_board = len(board)
    board.insert(0, [1] * len_board)
    board = [[1] + board[row_idx] for row_idx in range(len_board + 1)]

    delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    visited = set()
    visited.add(((1, 1), (1, 2)))

    cells_to_visit = deque([(0, (1, 1), (1, 2))])
    while cells_to_visit:
        time, first_cell, last_cell = cells_to_visit.popleft()

        dr = last_cell[0] - first_cell[0]
        dc = last_cell[1] - first_cell[1]

        # 상태를 유지한 채 상,하,좌,우 이동
        available_moves = []
        for move_r, move_c in delta:
            move_valid = True
            next_cells = tuple((cell[0] + move_r, cell[1] + move_c)
                               for cell in (first_cell, last_cell))
            for cell in next_cells:
                new_r, new_c = cell
                if (
                    new_r not in range(1, len_board + 1)
                    or new_c not in range(1, len_board + 1)
                    or board[new_r][new_c] == 1
                ):
                    move_valid = False
                    break
            if next_cells in visited or not move_valid:
                continue
            if (len_board, len_board) in next_cells:
                return time + 1
            available_moves.append(next_cells)

        # 가로로 놓여진 경우 로봇 회전
        if dr == 0 and dc == 1:
            for target_r in [last_cell[0] + 1, last_cell[0] - 1]:
                if target_r not in range(1, len_board + 1):
                    continue
                for fixed_cell, rotate_cell in [
                    (last_cell, first_cell), (first_cell, last_cell)
                ]:
                    check_r = target_r
                    check_c = rotate_cell[1]
                    fixed_r, fixed_c = fixed_cell
                    if board[check_r][check_c] == 1 or board[target_r][fixed_c] == 1:
                        break

                    next_loc = ((target_r, fixed_c), (fixed_r, fixed_c))
                    if next_loc in visited:
                        break
                    if (len_board, len_board) in next_loc:
                        return time + 1

                    available_moves.append(next_loc)

        # 세로로 놓여진 경우 로봇 회전
        if dr == 1 and dc == 0:
            for target_c in [last_cell[1] + 1, last_cell[1] - 1]:
                if target_c not in range(1, len_board + 1):
                    continue
                for fixed_cell, rotate_cell in [
                    (last_cell, first_cell), (first_cell, last_cell)
                ]:
                    check_c = target_c
                    check_r = rotate_cell[0]
                    fixed_r, fixed_c = fixed_cell
                    if board[check_r][check_c] == 1 or board[fixed_r][target_c] == 1:
                        break

                    next_loc = ((fixed_r, target_c), (fixed_r, fixed_c))
                    if next_loc in visited:
                        break
                    if (len_board, len_board) in next_loc:
                        return time + 1
                    available_moves.append(next_loc)

        for move in available_moves:
            sorted_move = sorted(move)
            next_time_loc = [time + 1] + sorted_move
            if tuple(sorted_move) in visited:
                continue

            cells_to_visit.append(next_time_loc)
            visited.add(tuple(sorted_move))
