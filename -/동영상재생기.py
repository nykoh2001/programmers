"""https://school.programmers.co.kr/learn/courses/30/lessons/340213

1. 계산 상의 편의를 위해 주어진 모든 시간을 초 단위로 변환
2. next, prev 입력에 대한 분기 구현, 현재 시점과 오프닝 구간을 비교하여 건너뛰기 구현
3. mm:ss 형태로 변환하여 return
"""

START_SECOND = 0
MINUTE_TO_SECONDS = 60


def min_to_sec(min_sec: str) -> int:
    minutes, seconds = map(int, min_sec.split(":"))

    return MINUTE_TO_SECONDS * minutes + seconds


def sec_to_min(sec: int) -> str:
    minutes = sec // MINUTE_TO_SECONDS
    seconds = sec % MINUTE_TO_SECONDS
    return f"{minutes:0>2}:{seconds:0>2}"


def execute_command(command: str, video_len_sec: int, pos_sec: int) -> int:
    if command == "next":
        return min(pos_sec + 10, video_len_sec)

    elif command == "prev":
        return max(pos_sec - 10, START_SECOND)

    msg = "Invalid Command"
    raise ValueError(msg)


def solution(video_len, pos, op_start, op_end, commands):
    video_len_sec = min_to_sec(video_len)
    pos_sec = min_to_sec(pos)

    op_start_sec, op_end_sec = map(min_to_sec, [op_start, op_end])

    for command in commands:
        if pos_sec >= op_start_sec and pos_sec <= op_end_sec:
            pos_sec = op_end_sec
        pos_sec = execute_command(command, video_len_sec, pos_sec)

    if pos_sec >= op_start_sec and pos_sec <= op_end_sec:
        pos_sec = op_end_sec
    return sec_to_min(pos_sec)
