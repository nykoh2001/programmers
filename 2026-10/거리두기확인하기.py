# 11:48 ~ 12:08
# 사람 사이의 거리가 2 이하인 경우만 필터링 -> 빈 책상이 사이에 있는 경우 존재 -> 0
# 66.2/100

# places[row][col] -> place[row][col]로 정정
# 사람이 아예 없는 경우 - all_safe가 while문 내부에서만 초기화 => 런타임 에러

from collections import deque


def solution(places):
    result = []
    for place in places:
        people = deque()
        for row_idx, row in enumerate(place):
            for col_idx, loc in enumerate(row):
                if loc == "P":
                    people.append((row_idx, col_idx))
                    continue

        all_safe = True
        while people:
            p_row, p_col = people.popleft()
            for r, c in people:
                manhatton = abs(p_row - r) + abs(p_col - c)
                if manhatton > 2:
                    continue

                if manhatton == 1:
                    all_safe = False
                    break

                # 같은 선상에 있을 때
                if p_row == r:
                    mid_col = (p_col + c) // 2
                    if place[p_row][mid_col] == "O":
                        all_safe = False
                        break

                if p_col == c:
                    mid_row = (p_row + r) // 2
                    if place[mid_row][p_col] == "O":
                        all_safe = False
                        break

                # 대각선상에 있을 때
                min_row, min_col, max_row, max_col = min(p_row, r), min(
                    p_col, c), max(p_row, r), max(p_col, c)
                adjacent_cells = set(
                    [(min_row, min_col), (min_row, max_col), (max_row, min_col), (max_row, max_col)])
                adjacent_cells.remove((p_row, p_col))
                adjacent_cells.remove((r, c))

                for adj_r, adj_c in adjacent_cells:
                    if place[adj_r][adj_c] == "O":
                        all_safe = False
                        break

            if not all_safe:
                break

        result.append(int(all_safe))

    return result
