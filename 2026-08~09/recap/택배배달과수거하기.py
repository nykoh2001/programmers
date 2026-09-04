def solution(capacity: int, n: int, deliveries: list[int], pickups: list[int]):
    distance = 0
    delivery, pickup = 0, 0

    for i in range(n - 1, -1, -1):
        delivery += deliveries[i]
        pickup += pickups[i]

        while delivery > 0 or pickup > 0:
            delivery -= capacity
            pickup -= capacity
            distance += (i + 1)

    return 2 * distance
