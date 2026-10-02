# 6:25 ~ 6:35
# 정렬 - 시작시간 기준
# 호텔 방 확인 후 생성 - 종료시간 기준으로 정렬
# 10분 청소시간


import heapq as hq


def _hh_mm_to_minutes(hh_mm: str) -> int:
    hh, mm = map(int, hh_mm.split(":"))
    return 60 * hh + mm


def solution(book_time):
    book_time.sort()
    rooms = []
    max_room_count = 0

    for start_time, end_time in book_time:
        earliest_end_time = rooms[0] if rooms else 0
        if earliest_end_time <= _hh_mm_to_minutes(start_time):
            if rooms:
                hq.heappop(rooms)

            hq.heappush(rooms, _hh_mm_to_minutes(end_time) + 10)
            max_room_count = max(max_room_count, len(rooms))
            continue

        hq.heappush(rooms, _hh_mm_to_minutes(end_time) + 10)
        max_room_count = max(max_room_count, len(rooms))

    return max_room_count
