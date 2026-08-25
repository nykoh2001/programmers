# https://school.programmers.co.kr/learn/courses/30/lessons/43105
# 3:56 ~ 4:09

from collections import defaultdict


def solution(triangle: list[list[int]]) -> int:
    sum_dict = defaultdict(int)

    for height, numbers in enumerate(triangle):
        if not sum_dict:
            sum_dict[0] = triangle[0][0]
            continue

        new_sum_dict = defaultdict(int)

        for num_idx, number in enumerate(numbers):
            if num_idx > 0:
                new_sum_dict[num_idx] = sum_dict[num_idx - 1] + number
            if num_idx < height:
                new_sum_dict[num_idx] = max(
                    new_sum_dict[num_idx], sum_dict[num_idx] + number)

        sum_dict = new_sum_dict

    return max(sum_dict.values())
