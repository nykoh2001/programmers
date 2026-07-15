"""https://school.programmers.co.kr/learn/courses/30/lessons/150369

- 상태 관리
- 처음 시작할 때 몇 개의 택배를 담을건가?
- 먼 곳을 왔다갔다 해야할 수록 비효율적일 가능성이 커짐, 먼 집들부터 우선적으로 고려
1. 얼마나 담을 것인가?
- 가장 뒷 집에서 필요한 택배 개수들을 세면서 capacity가 될 때까지 계산
- 이 때 가장 먼 집들에 다시 방문할 필요가 없도록, 택배를 준 후 다시 담을 수 있는 capacity도 고려
2. 뒷집들부터 처리
3. 1~2 반복

- Issues
1. current_capacity > capacity인 경우 고려해야 함
2. 부분적 수거도 처리
3. delivery/pickup이 필요 없는 집들 제외

===
Solution:

1. 가장 먼 미처리 주택은 무조건 가야함 -> 배달/수거 물량을 기반으로 왕복 횟수 계산
2. 가장 먼 주택 처리 후 남는 용적량으로 할 수 있는 처리를 더 가까운 주택들의 상태로 반영
- 그리디를 떠올렸지만 수학적으로 최적화할 수 있는 방법 존재
"""

from math import ceil

def solution(capacity: int, num_house: int, deliveries: list[int], pickups: list[int]):
    remain_delivery = 0
    remain_pickup = 0

    total_distance = 0

    for house_idx in range(num_house - 1, -1, -1):
        remain_delivery += deliveries[house_idx]
        remain_pickup += pickups[house_idx]

        max_remain = max(remain_delivery, remain_pickup)
        if max_remain <= 0:
            continue

        trip_count = ceil(max_remain / capacity)
        remain_delivery -= capacity * trip_count
        remain_pickup -= capacity * trip_count
        total_distance += 2 * (trip_count * (house_idx + 1))

    return total_distance
