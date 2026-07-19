"""https://school.programmers.co.kr/learn/courses/30/lessons/42883

1. DFS, Greedy: 3 runtime error, 1 timeout
"""

def solution(number: str, k: int):
    numbers_to_select = len(number) - k
    selected_idx = set()

    def select_first_max_idx(start: int, end: int) -> int | None:
        nonlocal selected_idx, number

        if start >= end or len(selected_idx) == numbers_to_select:
            return

        max_number, max_idx = 0, start

        for idx in range(start, end):
            if int(number[idx]) > max_number:
                max_number = int(number[idx])
                max_idx = idx

        selected_idx.add(max_idx)

        select_first_max_idx(max_idx + 1, end)
        select_first_max_idx(start, max_idx)

    select_first_max_idx(0, len(number))

    selected_number = ""
    for idx in sorted(list(selected_idx)):
        selected_number += number[idx]

    return selected_number
