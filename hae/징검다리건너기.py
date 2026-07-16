"""https://school.programmers.co.kr/learn/courses/30/lessons/64062

- 2개 test case에 대해 시간초과
- 최적화 방안 -
"""

from math import ceil


def solution(stones: list[int], jump: int):

    def _check_if_pass(friends: int) -> bool:
        stone_idx = -1
        while stone_idx + 1 < len(stones):
            if stones[stone_idx + 1] >= friends:
                stone_idx += 1
                continue

            if stone_idx + jump >= len(stones):
                return True

            for jump_idx in range(stone_idx + 1, stone_idx + jump + 1):
                if stones[jump_idx] >= friends:
                    stone_idx = jump_idx
                    break

                if jump_idx == stone_idx + jump:
                    return False

        return True

    start, end = min(stones), max(stones)

    while start < end:
        friends = ceil((start + end) / 2)
        if _check_if_pass(friends):
            start = friends
            continue

        end = friends - 1

    return start
