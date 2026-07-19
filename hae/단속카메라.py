"""https://school.programmers.co.kr/learn/courses/30/lessons/42884

- 1st: Permutation -> timeout
- 2nd: Sort + Greedy
"""


def solution(routes: list[list[int]]) -> int:
    len_route = len(routes)
    sorted_routes = sorted(routes)
    route_visited = [False] * len_route

    required_camera = 0

    for i in range(len_route):
        if route_visited[i]:
            continue

        route_visited[i] == True
        required_camera += 1
        _, current_end = sorted_routes[i]

        overlapped_area = (None, current_end)

        for j in range(i + 1, len_route):
            next_start, next_end = sorted_routes[j]
            if next_start > overlapped_area[1]:
                break

            route_visited[j] = True
            overlapped_area = (next_start, min(overlapped_area[1], next_end))

    return required_camera
