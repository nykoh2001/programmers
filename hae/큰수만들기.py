"""https://school.programmers.co.kr/learn/courses/30/lessons/42883

1. DFS, Greedy: 3 runtime error, 1 timeout
2. Stack, Greedy: Fail for last test case
"""

from collections import deque


def solution(number: str, k: int):
    INF = 1_000_001
    number_stack = deque()
    last_idx = len(number)

    for i, n in enumerate(number):
        int_num = int(n)
        if not number_stack:
            number_stack.append(int_num)
            continue

        top_element = number_stack[-1] if number_stack else INF
        while number_stack and top_element < int_num and k > 0:
            number_stack.pop()
            top_element = number_stack[-1] if number_stack else INF
            k -= 1
        number_stack.append(int_num)

        if k == 0:
            last_idx = i + 1
            break

    return "".join(list(map(str, number_stack))) + number[last_idx:]
