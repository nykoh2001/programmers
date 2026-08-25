import heapq as hq
from collections import deque

GRAPH = {
    1: [(1, 1), (2, 2), (4, 2), (5, 3)],
    2: [(2, 1), (1, 2), (3, 2), (5, 2), (4, 3), (6, 3)],
    3: [(3, 1), (2, 2), (6, 2), (5, 3)],
    4: [(4, 1), (1, 2), (5, 2), (7, 2), (2, 3), (8, 3)],
    5: [(5, 1), (2, 2), (4, 2), (6, 2), (8, 2), (1, 3), (3, 3), (7, 3), (9, 3)],
    6: [(6, 1), (3, 2), (5, 2), (9, 2), (2, 3), (8, 3)],
    7: [(7, 1), (4, 2), (8, 2), (0, 3), (5, 3)],
    8: [(8, 1), (0, 2), (5, 2), (7, 2), (9, 2), (4, 3), (6, 3)],
    9: [(9, 1), (6, 2), (8, 2), (0, 3), (5, 3)],
    0: [(0, 1), (7, 3), (8, 2), (9, 3)]
}

INF = 10 ** 9


def get_distances(number: int) -> list[int]:
    numbers_to_visit = [(0, number)]
    distances = [INF] * 10
    distances[number] = 0

    while numbers_to_visit:
        curr_dist, curr_number = hq.heappop(numbers_to_visit)
        if distances[curr_number] < curr_dist:
            continue

        for next_number, dist in GRAPH[curr_number]:
            new_dist = curr_dist + dist
            if distances[next_number] <= new_dist:
                continue

            distances[next_number] = new_dist
            hq.heappush(numbers_to_visit, (new_dist, next_number))

    distances[number] = 1
    return distances


def solution(numbers: str) -> int:
    INF = 10 ** 9
    distances_by_number = {number: get_distances(
        number) for number in range(10)}

    # fingers: distance
    distance_dp = {(4, 6): 0}

    for curr_number_str in numbers:
        curr_number = int(curr_number_str)
        new_distance_dp = {}
        for curr_fingers, distance in distance_dp.items():
            if curr_number in curr_fingers:
                new_distance_dp[curr_fingers] = min(
                    distance_dp[curr_fingers] + 1,
                    new_distance_dp.get(curr_fingers, INF)
                )
                continue

            for finger_idx, finger in enumerate(curr_fingers):
                finger_to_number = distances_by_number[finger][curr_number]
                new_distance = distance_dp[curr_fingers] + finger_to_number

                new_fingers = tuple([
                    f if f_idx != finger_idx
                    else curr_number
                    for f_idx, f in enumerate(curr_fingers)
                ])

                if new_distance >= new_distance_dp.get(new_fingers, INF):
                    continue

                new_distance_dp[new_fingers] = new_distance
        distance_dp = new_distance_dp

    return min(distance_dp.values())
