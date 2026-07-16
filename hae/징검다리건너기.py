"""https://school.programmers.co.kr/learn/courses/30/lessons/64062

- 2개 test case에 대해 시간초과
- 최적화 방안 -
  - Binary search에서 비효율적인 부분이 있을 것이라고 생각했지만, 
    더 간단하게 건널 수 있는지 확인하는 방법이 있었음
    - 마찬가지로 시뮬레이션을 수학적으로 최적화
"""

from math import ceil


def solution(stones: list[int], jump: int):
    def _check_if_pass(friends: int) -> bool:
        broken = 0
        for stone in stones:
            if stone < friends:
                broken += 1

                if broken >= jump:
                    return False

                continue

            broken = 0

        return True

    start, end = min(stones), max(stones)

    while start < end:
        friends = ceil((start + end) / 2)
        if _check_if_pass(friends):
            start = friends
            continue

        end = friends - 1

    return start
