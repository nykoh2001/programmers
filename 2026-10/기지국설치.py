# 6:35 ~ 6:57

# 예외 검증
# - W가 엄청 클 때
# - 겹치는 구간 없이 딱 맞을 때
# - station 하나로 충족될 때
# - 온 구간이 station일 때

# 효율성 실패

# 기지국 사이의 gap만 계산

from math import ceil


def solution(n, stations, w):
    stations.insert(0, -1 * w)
    stations.append(n + w + 1)

    required_stations = 0
    for i, station in enumerate(stations):
        if i == len(stations) - 1:
            break

        gap = stations[i + 1] - station - (2 * w + 1)

        required_stations += ceil(max(0, gap) / (2 * w + 1))

    return required_stations
