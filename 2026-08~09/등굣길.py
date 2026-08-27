# 2:45 ~ 3:12 (9/10), (0/10) -> manhatton == min dist

from sys import maxsize
import heapq as hq
from collections import defaultdict


def solution(m: int, n: int, puddles: list[list[int]]) -> int:
    MOD = 1_000_000_007
    INF = maxsize
    DX_DY = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def _get_adjacent_cells(x: int, y: int) -> list[list[int]]:
        adjacent_cells = []
        for dx, dy in DX_DY:
            new_x, new_y = x + dx, y + dy
            if new_x not in range(1, m + 1):
                continue
            if new_y not in range(1, n + 1):
                continue
            if [new_x, new_y] in puddles:
                continue

            adjacent_cells.append([new_x, new_y])

        return adjacent_cells

    manhatton = (m - 1) + (n - 1)
    min_distances = [[(INF, 0)] * (n + 1) for _ in range(m + 1)]

    # distance, path count
    min_distances[1][1] = (0, 1)
    cells_to_visit = [(0, 1, 1)]
    while cells_to_visit:
        dist, x, y = hq.heappop(cells_to_visit)

        # if min_distances[x][y][0] < dist:
        #     continue

        next_cells = _get_adjacent_cells(x, y)
        for next_x, next_y in next_cells:
            if dist + 1 > manhatton or min_distances[next_x][next_y][0] < dist + 1:
                continue

            if min_distances[next_x][next_y][0] == dist + 1:
                min_distances[next_x][next_y] = (dist + 1,
                                                 (min_distances[next_x]
                                                  [next_y][1] + 1) % MOD
                                                 )

            else:
                min_distances[next_x][next_y] = (dist + 1, 1)

            cells_to_visit.append((dist + 1, next_x, next_y))

    return min_distances[m][n][1] % MOD
