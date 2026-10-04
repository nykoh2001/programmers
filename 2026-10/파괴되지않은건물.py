# 4:33 ~ 4:43 -> passed all test cases, pure simulation
# 5:00 - skills 순회 => (r1, c1, r2, c2, durability) 기록
# { row_idx: heapq([(c1, count, durability), ...]), ...}
# 5:07 - GPT opti.
# 5:23 - 차분배열, difference array, imos


def solution(board, skill):
    N, M = len(board), len(board[0])
    difference_array = [[0] * (M + 1) for _ in range(N + 1)]

    for skill_type, r1, c1, r2, c2, degree in skill:
        signed_degree = -1 * degree if skill_type == 1 else degree
        difference_array[r1][c1] += signed_degree
        difference_array[r2 + 1][c1] -= signed_degree
        difference_array[r1][c2 + 1] -= signed_degree
        difference_array[r2 + 1][c2 + 1] += signed_degree

    buildings = 0
    for row_idx in range(N):
        for col_idx in range(M):
            if row_idx > 0:
                difference_array[row_idx][col_idx] += difference_array[row_idx - 1][col_idx]
            if col_idx > 0:
                difference_array[row_idx][col_idx] += difference_array[row_idx][col_idx - 1]
            if row_idx > 0 and col_idx > 0:
                difference_array[row_idx][col_idx] -= difference_array[row_idx - 1][col_idx - 1]

            if board[row_idx][col_idx] + difference_array[row_idx][col_idx] > 0:
                buildings += 1

    return buildings
