# 12:08 ~ 12:16
# 91.7/100

# 모든 연산 이후 k가 아직 남은 경우

from collections import deque


def solution(number: str, k: int):
    stack = deque([int(number[0])])

    for digit_str in number[1:]:
        digit = int(digit_str)

        while stack and k > 0 and digit > stack[-1]:
            stack.pop()
            k -= 1

        stack.append(digit)

    while k:
        stack.pop()
        k -= 1

    return "".join(map(str, stack))
