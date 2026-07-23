import heapq as hq

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

    return distances


def solution(numbers: str) -> int:
    min_distance = INF
    number_idx = 0
    fingers = [4, 6]
    distances_by_number = {number: get_distances(
        number) for number in range(10)}

    len_numbers = len(numbers)

    def get_total_distance(number_idx: int, fingers: list[int], total_distance: int) -> int:
        while number_idx < len_numbers:
            number = int(numbers[number_idx])
            if number in fingers:
                total_distance += 1
                number_idx += 1
                continue

            distances = distances_by_number[number]
            # print(f"number: {number}")
            # print(f"fingers: {fingers}")
            # print(f"distances: {distances}")

            first_distance = distances[fingers[0]]
            second_distance = distances[fingers[1]]

            distance_with_first_finger = get_total_distance(
                number_idx + 1, [number, fingers[1]
                                 ], total_distance + first_distance
            )
            distance_with_second_finger = get_total_distance(
                number_idx + 1, [fingers[0],
                                 number], total_distance + second_distance
            )
            # print(f"num_idx: {number_idx}, dist: {distance_with_first_finger, distance_with_second_finger}")
            return min(distance_with_first_finger, distance_with_second_finger)

        return total_distance

    return get_total_distance(number_idx, fingers, 0)
