import heapq as hq
from enum import Enum


class ROAD_TYPE(Enum):
    VERTICAL = "vertical"
    HORIZONTAL = "horizontal"


def _is_corner(road_type: ROAD_TYPE, dr: int, dc: int) -> bool:
    if road_type == ROAD_TYPE.VERTICAL.value and dc != 0:
        return True
    if road_type == ROAD_TYPE.HORIZONTAL.value and dr != 0:
        return True

    return False


def solution(board: list[list[int]]):
    INF = 10 ** 9
    len_board = len(board)

    # 비용, 경주로 유형, row, col
    cell_to_visit = [(0, 0, 0, ROAD_TYPE.HORIZONTAL.value),
                     (0, 0, 0, ROAD_TYPE.VERTICAL.value)]
    costs = [
        [
            {
                ROAD_TYPE.VERTICAL.value: INF,
                ROAD_TYPE.HORIZONTAL.value: INF
            } for _ in range(len_board)
        ] for _ in range(len_board)
    ]
    costs[0][0] = {
        ROAD_TYPE.VERTICAL.value: 0,
        ROAD_TYPE.HORIZONTAL.value: 0
    }

    dr_dc = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while cell_to_visit:
        cost, row, col, road_type = hq.heappop(cell_to_visit)

        if cost > costs[row][col][road_type]:
            continue

        for dr, dc in dr_dc:
            new_row, new_col = row + dr, col + dc
            new_road_type = ROAD_TYPE.VERTICAL.value if dr != 0 else ROAD_TYPE.HORIZONTAL.value

            if (
                any(loc not in range(len_board) for loc in (new_row, new_col))
                or board[new_row][new_col] == 1
            ):
                continue

            d_cost = 100 + (500 if _is_corner(road_type, dr, dc) else 0)
            new_cost = cost + d_cost

            if costs[new_row][new_col][new_road_type] <= new_cost:
                continue

            costs[new_row][new_col][new_road_type] = new_cost
            hq.heappush(cell_to_visit, (new_cost,
                        new_row, new_col, new_road_type))

    return min(costs[len_board - 1][len_board - 1].values())
