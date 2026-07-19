"""https://school.programmers.co.kr/learn/courses/30/lessons/42884

- 1st: Permutation -> timeout
"""

from collections import defaultdict, deque
from itertools import combinations


def solution(routes: list[list[int]]):
    spot_routes = defaultdict(set)
    spot_frequency = defaultdict(int)

    for route_idx, route in enumerate(routes):
        start, end = route
        spot_routes[start].add(route_idx)
        spot_routes[end].add(route_idx)
        for spot in range(start + 1, end):
            if spot in spot_routes:
                spot_routes[spot].add(route_idx)

    for spot, route_idxs in spot_routes.items():
        spot_frequency[spot] = len(route_idxs)

    for required_camera in range(1, len(routes) + 1):
        spot_list = list(spot_routes.keys())
        spot_combs = combinations(spot_list, required_camera)
        for spot_comb in spot_combs:
            route_set = set([])
            for spot in spot_comb:
                route_set.update(spot_routes[spot])
            if len(route_set) == len(routes):
                return required_camera
