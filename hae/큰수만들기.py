"""https://school.programmers.co.kr/learn/courses/30/lessons/42883

1. DFS, Greedy: 3 runtime error, 1 timeout
2. Stack, Greedy: Fail for last test case
3. Stack, Greedy: Handle edge case (k > 0)
"""

from collections import deque


def solution(number: str, k: int):
    number_stack = deque()
    last_idx = len(number)

    for i, n in enumerate(number):
        int_num = int(n)
        if not number_stack:
            number_stack.append(int_num)
            continue

        while number_stack and number_stack[-1] < int_num and k > 0:
            number_stack.pop()
            k -= 1
        number_stack.append(int_num)

        if k == 0:
            last_idx = i + 1
            break

    result = "".join(list(map(str, number_stack))) + number[last_idx:]

    if k > 0:
        return result[:-k]

    return result
