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
"""


def solution(capacity: int, num_house: int, deliveries: list[int], pickups: list[int]):
    remaining_num_house = num_house
    total_distance = 0

    while remaining_num_house:
        current_capacity, required_box = capacity, 0
        total_distance += remaining_num_house
        for house_idx in range(remaining_num_house - 1, -1, -1):
            # print(f"house_idx: {house_idx}, status: {[(d, p) for d, p in zip(deliveries, pickups)]}")
            delivered_all, picked_all = False, False
            if current_capacity == 0:
                break

            current_required_box = deliveries[house_idx]
            current_required_empty = pickups[house_idx]

            # 더 줄 수 있음
            if capacity - required_box >= 0:
                delivered_box = min(current_required_box,
                                    capacity - required_box)
                current_capacity += delivered_box
                deliveries[house_idx] -= delivered_box
                if deliveries[house_idx] == 0:
                    delivered_all = True
                required_box += delivered_box

            # 더 주울 수 있음
            if current_capacity >= current_required_empty:
                current_capacity -= current_required_empty
                pickups[house_idx] -= current_required_empty
                if pickups[house_idx] == 0:
                    picked_all = True

            # print(f"house_idx2: {house_idx}, status: {[(d, p) for d, p in zip(deliveries, pickups)]}")
            if not (delivered_all and picked_all):
                break

            remaining_num_house -= 1

    return total_distance * 2
