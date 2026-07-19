"""https://school.programmers.co.kr/learn/courses/30/lessons/42884

- 1st: Permutation -> timeout
- 2nd: Sort + Greedy
- 3rd: Sort + Greedy, Interval Scheduling
"""


def solution(routes: list[list[int]]) -> int:
    sorted_routes = sorted(routes, key=lambda x: x[1])
    last_camera = -float('inf')

    required_camera = 0

    for start, end in sorted_routes:
        if last_camera >= start:
            continue

        required_camera += 1
        last_camera = end

    return required_camera
